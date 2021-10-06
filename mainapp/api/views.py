import json
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, decorators
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

from .classes import BuyingCourseManager
from .mixins import PhotoManagerMixin, AddFriendMixin, MessageMixin
from . import serializers
from .utils import (
    get_serializer_to_display_the_profile,
    check_correct_data_for_add_in_timetable, delete_file,
)
from ..models import (
    Profile,
    Student,
    Teacher,
    EducationalManager,
    Group,
    Message,
    Category,
    Course,
    Lesson,
    Timetable,
    Certificate,
    AcademicPerformance,
    Photo,
)


# USERS

class BaseProfileViewSet(viewsets.ModelViewSet):
    """ Базовый класс для отображения профилей
    """
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]
    detail_serializer_class = None  # Сериализатор для детального отображения информации

    def retrieve(self, request, pk=None, *args, **kwargs):
        """ Если пользователь в друзьях, то отображается подробная информация """
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = get_serializer_to_display_the_profile(request, obj, self.detail_serializer_class)
        return Response(serializer.data)


class UserRetrieveView(APIView):
    """ Эндпоинт получения данных о текущем пользователе
    """
    def get(self, *args, **kwargs):
        item_profile = Profile.objects.get(user=self.request.user)
        serializer = serializers.ProfileSerializer(item_profile, many=False)
        return Response(serializer.data)


class StudentsViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех обучающихся
    """
    queryset = Student.objects.all()
    detail_serializer_class = serializers.ProfileSerializer


class TeachersViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех преподавателей
    """
    queryset = Teacher.objects.all()
    detail_serializer_class = serializers.ProfileSerializer


class EducationalManagerViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех менеджеров учебного процесса
    """
    permission_classes = [IsAdminUser]
    queryset = EducationalManager.objects.all()
    detail_serializer_class = serializers.ProfileSerializer


class ProfileCreateView(CreateAPIView):
    """ Эндпоинт регистрации нового обучающегося
    """
    permission_classes = [AllowAny]
    serializer_class = serializers.CreateProfileSerializer


class LoginView(APIView):
    """ Эндпоинт входа в систему
    Request data: username, password
    """
    @staticmethod
    def post(request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class PersonalProfileView(APIView):
    """ Эндпоинт личного кабинета
    Request data for students: hobbies - увлечения
                               dreams - мечта
    Request data for teachers: education - образование
                               professional_activity - профессиональная деятельность
    """
    serializer_classes = {
        'student': serializers.StudentDetailSerializer,
        'teacher': serializers.TeacherDetailSerializer,
        'manager': serializers.EducationalManagerDetailSerializer
    }

    serializer_updated_classes = {
        'student': serializers.StudentUpdateSerializer,
        'teacher': serializers.TeacherUpdateSerializer,
        'manager': serializers.EducationalManagerUpdateSerializer
    }

    @staticmethod
    def get_queryset(user, *args, **kwargs):
        if user.profile.user_group == 'student':
            return Student.objects.get(user=user)
        elif user.profile.user_group == 'teacher':
            return Teacher.objects.get(user=user)
        elif user.profile.user_group == 'manager':
            return EducationalManager.objects.get(user=user)
        else:
            return None

    def get(self, request, *args, **kwargs):
        item_user = self.request.user
        user = Profile.objects.get(pk=kwargs.get('pk')).user
        queryset = self.get_queryset(user)
        if not queryset:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if user == item_user or user in item_user.profile.friends.all():
            serializer = self.serializer_classes[user.profile.user_group]
            serializer = serializer(queryset, many=False)
        else:
            serializer = serializers.ProfileSerializer(queryset, many=False)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """ Редактировать профиль """
        data = request.data
        user = self.request.user
        queryset = self.get_queryset(user)
        if not queryset:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_updated_classes[user.profile.user_group]
        serializer.update(instance=queryset, validated_data=data)
        return Response(status=status.HTTP_201_CREATED)


# FRIENDS FOLLOWERS SUBSCRIPTIONS

class FriendsListView(ListAPIView):
    """ Эндпоинт друзей профиля """
    serializer_class = serializers.FriendsSerializer

    def list(self, request, *args, **kwargs):
        profile = self.get_queryset(pk=kwargs.get('pk'))
        item_user = self.request.user
        if item_user.profile != profile and item_user not in profile.friends.all():
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        try:
            return Profile.objects.get(pk=kwargs.get('pk'))
        except Profile.DoesNotExist:
            return None


class FollowersListView(FriendsListView):
    """ Эндпоинт подписчиков профиля """
    serializer_class = serializers.FollowersSerializer


class OutRequestsListView(FriendsListView):
    """ Эндпоинт подписок профиля """
    serializer_class = serializers.FriendsRequestOutSerializer


class InRequestsListView(ListAPIView):
    """ Эндпоинт входящих заявок в друзья """
    serializer_class = serializers.FriendsRequestInSerializer

    def list(self, request, *args, **kwargs):
        profile = self.get_queryset()
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        try:
            return self.request.user.profile
        except Profile.DoesNotExist:
            return None


class FriendRequestView(APIView, AddFriendMixin):
    """ Эндпоинт обработки исходящей заявки на добавление в друзья
        Данные: id - id пользователя
    """
    def post(self, *args, **kwargs):
        """ Предложить дружбу """
        http_status = self.add_request_friend(data=self.request.data, item_profile=self.request.user.profile)
        return Response(status=http_status)

    def delete(self, *args, **kwargs):
        """ Отписаться """
        http_status = self.unsubscribe(data=self.request.data, item_profile=self.request.user.profile)
        return Response(status=http_status)


class FriendResponseView(APIView, AddFriendMixin):
    """ Эндпоинт обработки входящей заявки на добавление в друзья
    Ожидается в запросе "answer" содержащий значение ответа
    Значения ключа "answer":
    "refuse" - отказ от дружбы
    "add" - добавление в друзья
    """
    def post(self, *args, **kwargs):
        """ Принять предложение дружбы (либо отказать в зависимости от ключа answer) """
        data = self.request.data
        answer = data.get('answer')
        if answer == 'add':
            http_status = self.add_response_friend(data=self.request.data, item_profile=self.request.user.profile)
        elif answer == 'refuse':
            http_status = self.refuse_response_friend(data=self.request.data, item_profile=self.request.user.profile)
        else:
            http_status = 400
        return Response(status=http_status)

    def delete(self, *args, **kwargs):
        """ Удалить из друзей """
        http_status = self.delete_friend(data=self.request.data, item_profile=self.request.user.profile)
        return Response(status=http_status)


# GROUPS

class GroupViewSet(viewsets.ModelViewSet):
    """ Эндроинт списка групп (Мои группы)
        В retrieve action доступен список одногруппников
    """
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GroupSerializer
    serializer_class_by_action = {'retrieve': serializers.GroupRetrieveSerializer}

    def get_queryset(self):
        item_profile = self.request.user.profile
        if item_profile.user_group == 'student':
            queryset = item_profile.student.group_list.all()
        elif item_profile.user_group == 'teacher':
            teacher = item_profile.teacher
            queryset = Group.objects.filter(teacher=teacher)
        elif item_profile.user_group == 'manager':
            manager = item_profile.educationalmanager
            queryset = Group.objects.filter(manager=manager)
        else:
            return None
        return queryset

    def get_serializer_class(self):
        try:
            return self.serializer_class_by_action[self.action]
        except KeyError:
            return self.serializer_class


# COURSES AND LESSONS

class CategoryListView(ListAPIView):
    """ Эндпоинт списка категорий курсов
    """
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CoursesViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка всех курсов
    """
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {'list': [IsAuthenticatedOrReadOnly],
                                    'retrieve': [IsAuthenticatedOrReadOnly],
                                    'lessons': [IsAuthenticatedOrReadOnly], }

    @action(detail=True, renderer_classes=[JSONRenderer])
    def lessons(self, request, *args, **kwargs):
        """ Уроки в курсе """
        course = self.get_object()
        lesson_objects = Lesson.objects.filter(course=course.pk).order_by('lesson_number')
        serializer = serializers.LessonSerializer(lesson_objects, many=True)
        return Response(serializer.data)

    @action(detail=False, renderer_classes=[JSONRenderer])
    def available(self, request, *args, **kwargs):
        """ Список доступных курсов """
        item_profile = self.request.user.profile

        if item_profile.user_group == 'student':
            available_courses_qs = item_profile.student.courses.all()
        elif item_profile.user_group == 'teacher':
            available_courses_qs = item_profile.teacher.courses.all()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = serializers.CourseSerializer(available_courses_qs, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class BuyingACourseView(APIView):
    """ Эндпоинт покупки курса
    Request data: id - id курса
    """
    def post(self, *args, **kwargs):
        buy_manager = BuyingCourseManager(self.request)
        response_data, http_status = buy_manager.pay()
        return Response(data=response_data, status=http_status)


class LessonsDetailView(APIView):
    """ Эндпоинт списка доступных уроков относящихся к курсу
    """
    def get(self, *args, **kwargs):
        item_profile = self.request.user.profile
        course_pk = kwargs.get('course_pk')
        lesson_pk = kwargs.get('pk')
        course = Course.objects.get(pk=course_pk)

        if item_profile.user_group == 'student':
            if course not in item_profile.student.courses.all():
                return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
        elif item_profile.user_group == 'teacher':
            if course not in item_profile.teacher.courses.all():
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        lesson_objects = Lesson.objects.get(pk=lesson_pk, course=course_pk)
        if not lesson_objects.is_active:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = serializers.LessonRetrieveSerializer(lesson_objects, many=False)
        return Response(serializer.data)


# TIMETABLE AND ACADEMIC PERFORMANCE

class TimetableViewSet(viewsets.ModelViewSet):
    """ Эндпоинт учебного рассписания
    Request data: date - дата,
                  lesson - id урока,
                  group - id группы
    """
    serializer_class = serializers.TimetableSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        item_profile = self.request.user.profile
        if item_profile.user_group == 'student':
            return Timetable.objects.filter(group__in=item_profile.student.group_list.all())
        elif item_profile.user_group == 'teacher':
            return Timetable.objects.filter(group__in=item_profile.teacher.group_list.all())

    def create(self, request, *args, **kwargs):
        """ Добавить урок в рассписание """
        item_profile = self.request.user.profile
        if item_profile.user_group == 'teacher' or item_profile.user_group == 'manager':
            data = request.data
            data_check_status = check_correct_data_for_add_in_timetable(item_profile, data)
            if data_check_status != 202:
                return Response(status=data_check_status)
            serializer = serializers.TimetableCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        elif item_profile.user_group == 'student':
            return Response(status=status.HTTP_403_FORBIDDEN)


class AcademicPerformanceViewSet(viewsets.ModelViewSet):
    """ Эндпоинт успеваемости обучающегося
    Request data: student - id студента,
                  lesson - id урока,
                  teacher - id преподавателя,
                  date - дата оценки,
                  homework_grade - домашняя работа,
                  classwork_grade - классная работа,
                  test_grade - контрольная работа,
                  examination_grade - экзамен,
                  late - опоздание,
                  absent - отсутствие
    """
    serializer_class = serializers.AcademicPerformanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        item_profile = self.request.user.profile
        if item_profile.user_group == 'student':
            return AcademicPerformance.objects.filter(student=item_profile)
        elif item_profile.user_group == 'teacher':
            teacher_groups = Group.objects.filter(teacher=item_profile)
            teacher_students = Student.objects.filter(group_list__in=teacher_groups)
            return AcademicPerformance.objects.filter(student__in=teacher_students)

    def create(self, request, *args, **kwargs):
        """ Поставить оценку """
        item_profile = request.user.profile
        if item_profile.user_group == 'teacher':
            data = request.data
            data['teacher'] = item_profile.pk
            data['date'] = datetime.date(datetime.now())
            serializer = serializers.AcademicPerformanceCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


# CERTIFICATES

class CertificateViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка полученных сертификатов
    """
    serializer_class = serializers.CertificateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        item_profile = self.request.user.profile
        return Certificate.objects.filter(profile=item_profile)


# PHOTOS

class GalleryListView(FriendsListView):
    """ Эндпоинт галереи профиля
    """
    serializer_class = serializers.GallerySerializer


class EditPhotoDescription(APIView):
    """ Эндпоинт добавления описания к фото
    Request data: id - id изображения
                  description - Новое описание к изображению
    """
    def put(self, request, *args, **kwargs):
        photo = self.get_queryset()
        item_user = request.user.profile
        if item_user != photo.for_profile:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = serializers.PhotoUpdateDescriptionSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.update(instance=photo, validated_data=self.request.data)
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self, *args, **kwargs):
        data = self.request.data
        try:
            return Photo.objects.get(pk=data.get('id'))
        except Photo.DoesNotExist:
            return None


class UploadPhotoView(APIView, PhotoManagerMixin):
    """ Эндпоинт загрузки фотографии
    Request data: image - Файл изображения
    """
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = serializers.UploadPhotoSerializer(data=request.data)
        if file_serializer.is_valid():
            self.add_photo(request)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeletePhotoView(DestroyAPIView):
    """ Эндпоинт удаления фото
    Kwargs url data: pk - id фотографии
    """
    serializer_class = serializers.PhotoSerializer

    def get_queryset(self):
        queryset = Photo.objects.filter(pk=self.kwargs.get('pk'))
        return queryset

    def destroy(self, request, *args, **kwargs):
        profile = self.request.user.profile
        try:
            instance = self.get_object()
        except Photo.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if instance.for_profile == profile:
            if instance == profile.avatar:
                profile.avatar = None
            delete_file(instance.image.url)
            self.perform_destroy(instance)
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LikePhotoView(APIView, PhotoManagerMixin):
    """ Эндпоинт лайка фото
    Request data: id - id фотографии
    """
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        data = self.request.data
        photo_id = data.get('id')
        http_status = self.like_photo(request, photo_id)
        return Response(status=http_status)


class UploadAvatarView(APIView, PhotoManagerMixin):
    """ Эндпоинт загрузки аватарки
    Request data: image - Файл изображения
    """
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request, *args, **kwargs):
        item_profile = request.user.profile
        file_serializer = serializers.UploadPhotoSerializer(data=request.data)
        if file_serializer.is_valid():
            new_avatar = self.add_photo(request)
            item_profile.avatar = new_avatar
            item_profile.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SetAvatarView(APIView):
    """ Эндпоинт установки аватарки из существующих фото
    Request data: id - id фотографии
    """
    def put(self, *args, **kwargs):
        data = self.request.data
        profile = self.request.user.profile
        photo = Photo.objects.get(pk=data['id'])
        if photo in profile.photos.all():
            profile.avatar = photo
            profile.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        """ Удаление аватарки с сохранением фото в галереи """
        profile = self.request.user.profile
        if not profile.avatar:
            return Response(status=status.HTTP_204_NO_CONTENT)
        profile.avatar = None
        profile.save()
        return Response(status=status.HTTP_202_ACCEPTED)


# MESSAGES

class DialogViewSet(viewsets.ModelViewSet, MessageMixin):
    """ Эндпоинт списка диалогов
    """
    serializer_class = serializers.DialogSerializer

    def get_queryset(self):
        item_profile = self.request.user.profile
        return item_profile.participants.all().order_by('-last_message')

    def list(self, request, *args, **kwargs):
        dialogs_list = self.get_queryset()

        serializer = serializers.DialogSerializer(dialogs_list, many=True)
        serializer.is_new_messages = False
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        message_list = Message.objects.filter(dialog=instance)
        self.read_messages(request, message_list=message_list)
        serializer = serializers.MessageViewSerializer(message_list, many=True)
        return Response(serializer.data)


class CreateAGroupDialog(APIView, MessageMixin):
    """ Эндпоинт создания беседы и приглашения пользователей в беседу
    Request data POST: name - Название беседы
                       participants - список участников
    Request data PUT: id - id диалога
                      users - список с id приглашенных пользователей
    """
    def post(self, request, *args, **kwargs):
        # Создание групповой беседы
        message, http_status = self.create_group_dialog(self.request)
        return Response(data={"message": message}, status=http_status)

    def put(self, request, *args, **kwargs):
        # Приглашение новых участников в беседу
        message, http_status = self.add_user_in_dialog(self.request)
        return Response(data={"message": message}, status=http_status)


class UploadGroupDialogImage(APIView, MessageMixin):
    """ Эндпоинт установки изображения на аватар групового чата
    Request data: image - Файл изображения
    """
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = serializers.UploadPhotoSerializer(data=request.data)
        dialog_id = kwargs.get('pk')
        if file_serializer.is_valid():
            message, http_status = self.set_chat_image(request, pk=dialog_id)
            if http_status == 201:
                return Response(data=file_serializer.data, status=http_status)
            else:
                return Response(data={"message": message}, status=http_status)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateGroupDialogName(APIView, MessageMixin):
    """ Обновление названия беседы
    request data: name - Название диалога
    kwargs: pk - id диалога
    """
    def put(self, request, *args, **kwargs):
        message, http_status = self.set_dialog_name(request, dialog_id=kwargs.get('pk'))
        return Response(data={"message": message}, status=http_status)


class SendMessageView(APIView, MessageMixin):
    """ Эндпоинт отправки сообщений
    Request data: user_id - Пользователь которому отправляем сообщение
                  dialog - id диалога (если уже есть существующий)
                  text - текст сообщения
    """
    def post(self, request, *args, **kwargs):
        message, http_status = self.send_message(self.request)
        return Response(data={"message": message}, status=http_status)
