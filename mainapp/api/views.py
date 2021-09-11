from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView

from .classes import BuyingCourseManager
from .mixins import PhotoManagerMixin, AddFriendMixin, MessageMixin
from .renders import CustomBrowsableAPIRenderer
from .serializers import (
    ProfileSerializer,
    StudentDetailSerializer,
    TeacherDetailSerializer,
    EducationalManagerDetailSerializer,
    GroupSerializer,
    DialogSerializer,
    DialogAttachmentSerializer,
    MessageViewSerializer,
    CategorySerializer,
    CourseSerializer,
    LessonSerializer,
    LessonRetrieveSerializer,
    CreateProfileSerializer,
    TimetableSerializer,
    TimetableCreateSerializer,
    CertificateSerializer,
    AcademicPerformanceSerializer,
    PhotoSerializer,
    UploadPhotoSerializer,
)
from .utils import (
    get_serializer_to_display_the_profile,
    check_correct_data_for_add_in_timetable, delete_file,
    get_student_group_name_list,
)
from ..models import (
    Student,
    Teacher,
    EducationalManager,
    Group,
    DialogAttachment,
    Message,
    Category,
    Course,
    Lesson,
    Timetable,
    Certificate,
    AcademicPerformance,
    Photo,
)


class BaseProfileViewSet(viewsets.ModelViewSet):
    """ Базовый класс для отображения профилей
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    detail_serializer_class = None  # Сериализатор для детального отображения информации

    def retrieve(self, request, pk=None, *args, **kwargs):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = get_serializer_to_display_the_profile(request, obj, self.detail_serializer_class)
        return Response(serializer.data)


class StudentsViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех обучающихся
    """
    queryset = Student.objects.all()
    detail_serializer_class = StudentDetailSerializer


class TeachersViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех преподавателей
    """
    queryset = Teacher.objects.all()
    detail_serializer_class = TeacherDetailSerializer


class EducationalManagerViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех менеджеров учебного процесса
    """
    permission_classes = [IsAdminUser]
    queryset = EducationalManager.objects.all()
    detail_serializer_class = EducationalManagerDetailSerializer


class ProfileCreateView(CreateAPIView):
    """ Эндпоинт регистрации нового обучающегося
    """
    permission_classes = [AllowAny]
    serializer_class = CreateProfileSerializer


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
    @staticmethod
    def get_queryset(user):
        if user.profile.user_group == 'student':
            return Student.objects.filter(user=user)
        elif user.profile.user_group == 'teacher':
            return Teacher.objects.filter(user=user)
        elif user.profile.user_group == 'manager':
            return EducationalManager.objects.filter(user=user)
        else:
            return None

    def get(self, request, format=None):
        user = self.request.user
        obj = self.get_queryset(user)
        if user.profile.user_group == 'student':
            serializer = StudentDetailSerializer(obj, many=True)
        elif user.profile.user_group == 'teacher':
            serializer = TeacherDetailSerializer(obj, many=True)
        elif user.profile.user_group == 'manager':
            serializer = EducationalManagerDetailSerializer(obj, many=True)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """ Редактировать профиль """
        data = request.data
        user = self.request.user
        if user.profile.user_group == 'student':
            student = Student.objects.get(user=user)
            student.hobbies = data.get('hobbies')
            student.dream = data.get('dream')
            student.save()
        elif user.profile.user_group == 'teacher':
            teacher = Teacher.objects.get(user=user)
            teacher.education = data.get('education')
            teacher.professional_activity = data.get('professional_activity')
            teacher.save()
        return Response(status=status.HTTP_201_CREATED)


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


class GroupViewSet(viewsets.ModelViewSet):
    """ Эндроинт списка групп (Мои группы)
    """
    serializer_class = GroupSerializer

    def get_queryset(self):
        item_profile = self.request.user.profile
        if item_profile.user_group == 'student':
            student_group_name_lest = get_student_group_name_list(item_profile.student)
            queryset = Group.objects.filter(name__in=student_group_name_lest)
        elif item_profile.user_group == 'teacher':
            teacher = item_profile.teacher
            queryset = Group.objects.filter(teacher=teacher)
        elif item_profile.user_group == 'manager':
            manager = item_profile.educationalmanager
            queryset = Group.objects.filter(manager=manager)
        else:
            return None
        return queryset


class CategoryListView(ListAPIView):
    """ Эндпоинт списка категорий курсов
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CoursesViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка всех курсов
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    @action(detail=True, renderer_classes=[CustomBrowsableAPIRenderer])
    def lessons(self, request, *args, **kwargs):
        """ Уроки в курсе """
        course = self.get_object()
        lesson_objects = Lesson.objects.filter(course=course.pk).order_by('lesson_number')
        serializer = LessonSerializer(lesson_objects, many=True)
        return Response(serializer.data)


class BuyingACourseView(APIView):
    """ Эндпоинт покупки курса
    Request data: id - id курса
    """
    def put(self, *args, **kwargs):
        buy_manager = BuyingCourseManager()
        http_status = buy_manager.get_buy_status(self.request)
        return Response(status=http_status)


class LessonsDetailView(APIView):
    """ Эндпоинт списка доступных уроков относящихся к курсу
    """
    def get(self, *args, **kwargs):
        item_profile = self.request.user.profile
        course_pk = kwargs.get('course_pk')
        lesson_pk = kwargs.get('pk')
        course = Course.objects.get(pk=course_pk)

        if item_profile.user_group == 'student':
            if course in item_profile.student.courses.all():
                lesson_objects = Lesson.objects.get(pk=lesson_pk, course=course_pk)
                serializer = LessonRetrieveSerializer(lesson_objects, many=False)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_402_PAYMENT_REQUIRED)

        elif item_profile.user_group == 'teacher':
            if course in item_profile.teacher.courses.all():
                lesson_objects = Lesson.objects.get(course=course_pk)
                serializer = LessonRetrieveSerializer(lesson_objects, many=False)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)


class TimetableViewSet(viewsets.ModelViewSet):
    """ Эндпоинт учебного рассписания
    Request data: date - дата,
                  lesson - id урока,
                  group - id группы
    """
    serializer_class = TimetableSerializer
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
            serializer = TimetableCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        elif item_profile.user_group == 'student':
            return Response(status=status.HTTP_403_FORBIDDEN)


class CertificateViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка полученных сертификатов
    """
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        item_profile = self.request.user.profile
        return Certificate.objects.filter(profile=item_profile)


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
    serializer_class = AcademicPerformanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
            serializer = AcademicPerformanceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class UploadPhotoView(APIView, PhotoManagerMixin):
    """ Эндпоинт загрузки фотографии
    Request data: image - Файл изображения
    """
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = UploadPhotoSerializer(data=request.data)
        if file_serializer.is_valid():
            self.add_photo(request)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeletePhotoView(DestroyAPIView):
    """ Эндпоинт удаления фото
    Kwargs url data: pk - id фотографии
    """
    serializer_class = PhotoSerializer

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
        file_serializer = UploadPhotoSerializer(data=request.data)
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


class DialogViewSet(viewsets.ModelViewSet, MessageMixin):
    """ Эндпоинт списка диалогов
    """
    serializer_class = DialogSerializer

    def get_queryset(self):
        item_profile = self.request.user.profile
        return item_profile.participants.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        message_list = Message.objects.filter(dialog=instance)
        self.read_messages(message_list=message_list)
        serializer = MessageViewSerializer(message_list, many=True)
        return Response(serializer.data)


class CreateAGroupDialog(APIView, MessageMixin):
    """ Эндпоинт создания беседы
    Request data: name - Название беседы
                  participants - список участников
    """
    def post(self, request, *args, **kwargs):
        http_status = self.create_group_dialog(self.request)
        return Response(status=http_status)


class SendMessageView(APIView, MessageMixin):
    """ Эндпоинт отправки сообщений
    Request data: user_id - Пользователь которому отправляем сообщение
                  dialog - id диалога (если уже есть существующий)
                  text - текст сообщения
    """
    def post(self, request, *args, **kwargs):
        http_status = self.send_message(self.request)
        return Response(status=http_status)
