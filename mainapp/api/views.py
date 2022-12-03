from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView

from .classes import BuyingCourseManager
from .methods import get_normalize_phone
from .mixins import PhotoManagerMixin, AddFriendMixin, MessageMixin
from . import serializers
from .utils import (
    get_serializer_to_display_the_profile,
    check_correct_data_for_add_in_timetable, delete_file,
)
from mainapp import models

from management.models import Staff, Request, Client


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
        item_profile = models.Profile.objects.get(user=self.request.user)
        serializer = serializers.ProfileSerializer(item_profile, many=False)
        return Response(serializer.data)


class StudentsViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех обучающихся
    """
    queryset = models.Student.objects.all()
    detail_serializer_class = serializers.ProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__first_name', 'middle_name', 'user__last_name')


class TeachersViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех преподавателей
    """
    permission_classes = [AllowAny]
    queryset = models.Teacher.objects.all()
    detail_serializer_class = serializers.ProfileSerializer


class EducationalManagerViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех менеджеров учебного процесса
    """
    permission_classes = [IsAdminUser]
    queryset = Staff.objects.filter(user_group='education_manager')
    detail_serializer_class = serializers.ProfileSerializer


class ProfileCreateView(CreateAPIView):
    """ Эндпоинт регистрации нового обучающегося
    """
    permission_classes = [AllowAny]
    serializer_class = serializers.CreateProfileSerializer

    def create(self, request, *args, **kwargs):
        try:
            super(ProfileCreateView, self).create(request, *args, **kwargs)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'message': f'{e}'})


class PersonalProfileView(viewsets.ModelViewSet):
    """ Эндпоинт личного кабинета
    Request data for students: hobbies - увлечения
                               dreams - мечта
    Request data for teachers: education - образование
                               professional_activity - профессиональная деятельность
    """
    serializer_classes = {
        'student': serializers.StudentDetailSerializer,
        'teacher': serializers.TeacherDetailSerializer,
    }

    serializer_updated_classes = {
        'student': serializers.StudentUpdateSerializer,
        'teacher': serializers.TeacherUpdateSerializer,
    }

    def get_queryset(self, *args, **kwargs):
        profile = kwargs.get('profile')
        if profile.user_group == 'student':
            return profile.student
        elif profile.user_group == 'teacher':
            return profile.teacher
        else:
            return None

    def retrieve(self, request, *args, **kwargs):
        profile = models.Profile.objects.get(pk=kwargs.get('pk'))
        queryset = self.get_queryset(profile=profile)
        if not queryset:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if profile.user == self.request.user or profile.user in self.request.user.profile.friends.all():
            serializer = self.serializer_classes[profile.user_group](queryset, many=False)
        else:
            serializer = serializers.ProfileSerializer(queryset, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """ Редактировать профиль """
        queryset = self.get_queryset(profile=self.request.user.profile)
        if not queryset:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_updated_classes[self.request.user.profile.user_group]
        serializer.update(instance=queryset, validated_data=request.data)
        return Response(status=status.HTTP_201_CREATED)


# FRIENDS FOLLOWERS SUBSCRIPTIONS

class FriendsListView(ListAPIView):
    """ Эндпоинт друзей профиля """
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.FriendsSerializer

    def list(self, request, *args, **kwargs):
        profile = self.get_queryset(pk=kwargs.get('pk'))
        if self.request.user.profile != profile and self.request.user not in profile.friends.all():
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        try:
            return models.Profile.objects.get(pk=kwargs.get('pk'))
        except models.Profile.DoesNotExist:
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
        except models.Profile.DoesNotExist:
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
        answer = self.request.data.get('answer')
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


class AchievementListView(ListAPIView):
    """ Эндпоинт списка всех ачивок
    """
    permission_classes = [IsAuthenticated]
    queryset = models.Achievement.objects.all()
    serializer_class = serializers.AchievementSerializer


class StudentAchievementListView(FriendsListView):
    """ Эндпоинт списка ачивок студента
    """
    serializer_class = serializers.ProfileAchievementSerializer


# GROUPS

class GroupViewSet(viewsets.ModelViewSet):
    """ Эндроинт списка групп (Мои группы)
        В retrieve action доступен список одногруппников
    """
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GroupSerializer
    serializer_class_by_action = {'retrieve': serializers.GroupRetrieveSerializer}
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_queryset(self):
        item_profile = self.request.user.profile
        if item_profile.user_group == 'student':
            queryset = item_profile.student.group_list.all()
        elif item_profile.user_group == 'teacher':
            queryset = item_profile.teacher.group_list.all()
        elif item_profile.user_group == 'manager':
            queryset = item_profile.educationalmanager.group_list.all()
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
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CoursesViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка всех курсов
    """
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {
        'list': [IsAuthenticatedOrReadOnly],
        'retrieve': [IsAuthenticatedOrReadOnly],
        'lessons': [IsAuthenticatedOrReadOnly],
        'delete': [IsAdminUser],
        'create': [IsAdminUser],
    }
    lookup_field = 'id'

    @action(detail=True, renderer_classes=[JSONRenderer])
    def lessons(self, request, *args, **kwargs):
        """ Уроки в курсе """
        course = self.get_object()
        lesson_objects = models.Lesson.objects.filter(course=course.pk).order_by('lesson_number')
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
        course = models.Course.objects.get(pk=kwargs.get('course_pk'))

        if item_profile.user_group == 'student':
            if course not in item_profile.student.courses.all():
                return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
        elif item_profile.user_group == 'teacher':
            if course not in item_profile.teacher.courses.all():
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        lesson_objects = models.Lesson.objects.get(
            pk=kwargs.get('pk'),
            course=kwargs.get('course_pk')
        )
        if not lesson_objects.is_active:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = serializers.LessonRetrieveSerializer(lesson_objects, many=False)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        try:
            lesson_objects = models.Lesson.objects.get(
                pk=kwargs.get('pk'),
                course=kwargs.get('course_pk')
            )
        except models.Lesson.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            student = models.Student.objects.get(pk=self.request.data.get('user'))
        except models.Student.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        new_comment = models.LessonComment.objects.create(student=student, comment=self.request.data.get('comment'))
        lesson_objects.comments.add(new_comment)

        return Response(status=status.HTTP_201_CREATED)

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
            return models.Timetable.objects.filter(group__in=item_profile.student.group_list.all())
        elif item_profile.user_group == 'teacher':
            return models.Timetable.objects.filter(group__in=item_profile.teacher.group_list.all())

    def create(self, request, *args, **kwargs):
        """ Добавить урок в расписание """
        if request.user.profile.user_group == 'teacher' or request.user.profile.user_group == 'manager':
            data_check_status = check_correct_data_for_add_in_timetable(request.user.profile, request.data)
            if data_check_status != 202:
                return Response(status=data_check_status)
            serializer = serializers.TimetableCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        elif request.user.profile.user_group == 'student':
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
            return models.AcademicPerformance.objects.filter(student=item_profile)
        elif item_profile.user_group == 'teacher':
            teacher_students = models.Student.objects.filter(group_list__in=item_profile.teacher.group_list.all())
            return models.AcademicPerformance.objects.filter(student__in=teacher_students)

    def create(self, request, *args, **kwargs):
        """ Поставить оценку """
        if request.user.profile.user_group == 'teacher':
            request.data['teacher'] = request.user.profile.pk
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
        return models.Certificate.objects.filter(profile=item_profile)


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
        if request.user.profile != photo.for_profile:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = serializers.PhotoUpdateDescriptionSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.update(instance=photo, validated_data=self.request.data)
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self, *args, **kwargs):
        try:
            return models.Photo.objects.get(pk=self.request.data.get('id'))
        except models.Photo.DoesNotExist:
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
        queryset = models.Photo.objects.filter(pk=self.kwargs.get('pk'))
        return queryset

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except models.Photo.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if instance.for_profile == self.request.user.profile:
            if instance == self.request.user.profile.avatar:
                self.request.user.profile.avatar = None
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
        http_status = self.like_photo(request, self.request.data.get('id'))
        return Response(status=http_status)


class UploadAvatarView(APIView, PhotoManagerMixin):
    """ Эндпоинт загрузки аватарки
    Request data: image - Файл изображения
    """
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = serializers.UploadPhotoSerializer(data=request.data)
        if file_serializer.is_valid():
            new_avatar = self.add_photo(request)
            request.user.profile.avatar = new_avatar
            request.user.profile.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SetAvatarView(APIView):
    """ Эндпоинт установки аватарки из существующих фото
    Request data: id - id фотографии
    """
    def put(self, *args, **kwargs):
        photo = models.Photo.objects.get(pk=self.request.data['id'])
        if photo in self.request.user.profile.photos.all():
            self.request.user.profile.avatar = photo
            self.request.user.profile.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        """ Удаление аватарки с сохранением фото в галереи """
        if not self.request.user.profile.avatar:
            return Response(status=status.HTTP_204_NO_CONTENT)
        self.request.user.profile.avatar = None
        self.request.user.profile.save()
        return Response(status=status.HTTP_202_ACCEPTED)


# MESSAGES

class DialogViewSet(viewsets.ModelViewSet, MessageMixin):
    """ Эндпоинт списка диалогов
    """
    serializer_class = serializers.DialogSerializer

    def get_queryset(self):
        return self.request.user.profile.participants.all().order_by('-last_message')

    def list(self, request, *args, **kwargs):
        dialogs_list = self.get_queryset()

        serializer = serializers.DialogSerializer(dialogs_list, many=True)
        serializer.is_new_messages = False
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        message_list = models.Message.objects.filter(dialog=instance)
        # self.read_messages(request, message_list=message_list)
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


# EVENTS

class EventViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка мероприятий
    """
    serializer_class = serializers.EventSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        return models.Event.objects.all().order_by('date')


# NEWS

class NewsViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка новостей
    """
    serializer_class = serializers.NewsSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        return models.News.objects.all()


# REQUESTS
class RequestsViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка заявок
    """
    serializer_class = serializers.RequestSerializer
    permission_classes_by_action = {
        'list': [IsAdminUser],
        'retrieve': [IsAdminUser],
        'delete': [IsAdminUser],
        'create': [AllowAny],
    }

    def get_queryset(self):
        return Request.objects.all()

    def create(self, request, *args, **kwargs):
        """ Добавить заявку """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            new_request = serializer.save()
            phone = get_normalize_phone(request.data.get('request_phone'))
            try:
                client = Client.objects.get(phone=phone)
                new_request.client = client
            except Client.DoesNotExist:
                comment = '-- Система: Клиент не найден по введенному номеру телефону'
                new_request.comment = comment
            new_request.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return IsAdminUser()
