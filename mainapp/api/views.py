from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView

from .mixins import ProfileManagerMixin, AddFriendMixin
from .renders import CustomBrowsableAPIRenderer
from .serializers import (
    ProfileSerializer,
    StudentDetailSerializer,
    TeacherDetailSerializer,
    EducationalManagerDetailSerializer,
    CategorySerializer,
    CourseSerializer,
    LessonSerializer,
    LessonRetrieveSerializer,
    CreateProfileSerializer,
    TimetableSerializer,
    CertificateSerializer,
    AcademicPerformanceSerializer,
    UploadPhotoSerializer,
)
from .utils import get_serializer_to_display_the_profile
from ..models import (
    Profile,
    Student,
    Teacher,
    EducationalManager,
    Group,
    Category,
    Course,
    Lesson,
    Timetable,
    Certificate,
    AcademicPerformance,
)


class BaseProfileViewSet(viewsets.ModelViewSet):
    """ Базовый класс для отображения профилей """
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    detail_serializer_class = None  # Сериализатор для детального отображения информации

    def retrieve(self, request, pk=None, *args, **kwargs):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = get_serializer_to_display_the_profile(request, obj, self.detail_serializer_class)
        return Response(serializer.data)


class StudentsViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех обучающихся """
    queryset = Student.objects.all()
    detail_serializer_class = StudentDetailSerializer


class TeachersViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех преподавателей """
    queryset = Teacher.objects.all()
    detail_serializer_class = TeacherDetailSerializer


class EducationalManagerViewSet(BaseProfileViewSet):
    """ Эндпоинт списка всех менеджеров учебного процесса """
    permission_classes = [IsAdminUser]
    queryset = EducationalManager.objects.all()
    detail_serializer_class = EducationalManagerDetailSerializer


class ProfileCreateView(CreateAPIView):
    """ Эндпоинт регистрации нового обучающегося """
    permission_classes = [AllowAny]
    serializer_class = CreateProfileSerializer


class LoginView(APIView):
    """ Эндпоинт входа в систему """
    @staticmethod
    def post(request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=201)
            else:
                return Response(status=404)
        else:
            return Response(status=404)


class PersonalProfileView(APIView):
    """ Эндпоинт личного кабинета """
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
            return Response(status=404)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
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
        return Response(status=201)


class FriendRequestView(APIView, AddFriendMixin):
    """ Эндпоинт обработки исходящей заявки на добавление в друзья """
    def post(self, *args, **kwargs):
        status = self.add_request_friend(data=self.request.data, item_profile=self.request.user.profile)
        return Response(status=status)


class FriendResponseView(APIView, AddFriendMixin):
    """ Эндпоинт обработки входящей заявки на добавление в друзья """
    def post(self, *args, **kwargs):
        status = self.add_response_friend(data=self.request.data, item_profile=self.request.user.profile)
        return Response(status=status)


class CategoryListView(ListAPIView):
    """ Эндпоинт списка категорий курсов """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CoursesViewSet(viewsets.ModelViewSet):
    """  Эндпоинт списка всех курсов """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    @action(detail=True, renderer_classes=[CustomBrowsableAPIRenderer])
    def lessons(self, request, *args, **kwargs):
        course = self.get_object()
        lesson_objects = Lesson.objects.filter(course=course.pk).order_by('lesson_number')
        serializer = LessonSerializer(lesson_objects, many=True)
        return Response(serializer.data)


class LessonsDetailView(ProfileManagerMixin):
    """ Эндпоинт списка доступных уроков относящихся к курсу """
    def get(self, *args, **kwargs):
        item_profile = self.get_profile()   # get_profile - метод миксина ProfileAPIViewMixin
        course_pk = kwargs.get('course_pk')
        lesson_pk = kwargs.get('pk')
        course = Course.objects.get(pk=course_pk)

        if item_profile.user_group == 'student':
            if course in item_profile.student.courses.all():
                lesson_objects = Lesson.objects.get(pk=lesson_pk, course=course_pk)
                serializer = LessonRetrieveSerializer(lesson_objects, many=False)
                return Response(serializer.data)
            else:
                return Response(status=400)

        elif item_profile.user_group == 'teacher':
            if course in item_profile.teacher.courses.all():
                lesson_objects = Lesson.objects.get(course=course_pk)
                serializer = LessonRetrieveSerializer(lesson_objects, many=False)
                return Response(serializer.data)
            else:
                return Response(status=400)


class TimetableViewSet(viewsets.ModelViewSet, ProfileManagerMixin):
    """ Эндпоинт учебного рассписания """
    serializer_class = TimetableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        item_profile = self.get_profile()
        if item_profile.user_group == 'student':
            return Timetable.objects.filter(group__in=item_profile.student.group.all())
        elif item_profile.user_group == 'teacher':
            return Timetable.objects.filter(group__in=item_profile.teacher.group.all())


class CertificateViewSet(viewsets.ModelViewSet, ProfileManagerMixin):
    """ Эндпоинт списка полученных сертификатов """
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        item_profile = self.get_profile()
        return Certificate.objects.filter(profile=item_profile)


class AcademicPerformanceViewSet(viewsets.ModelViewSet, ProfileManagerMixin):
    """ Эндпоинт успеваемости обучающегося """
    serializer_class = AcademicPerformanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        item_profile = self.get_profile()
        if item_profile.user_group == 'student':
            return AcademicPerformance.objects.filter(student=item_profile)
        elif item_profile.user_group == 'teacher':
            teacher_groups = Group.objects.filter(teacher=item_profile)
            teacher_students = Student.objects.filter(group__in=teacher_groups)
            return AcademicPerformance.objects.filter(student__in=teacher_students)

    def create(self, request, *args, **kwargs):
        item_profile = self.get_profile()
        if item_profile.user_group == 'teacher':
            serializer = AcademicPerformanceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(status=201)
        else:
            return Response(status=404)


class UploadPhotoView(ProfileManagerMixin):
    """ Эндпоинт загрузки фотографии """
    def post(self, request, *args, **kwargs):
        file_serializer = UploadPhotoSerializer(data=request.data)
        if file_serializer.is_valid():
            self.add_photo(request)
            return Response(status=201)
        else:
            return Response(status=400)


class LikePhotoView(ProfileManagerMixin):
    """ Эндпоинт лайка фото """
    parser_classes = [JSONParser]

    def post(self, *args, **kwargs):
        data = self.request.data
        photo_id = data.get('id')
        status = self.like_photo(photo_id)
        return Response(status=status)


class UploadAvatarView(ProfileManagerMixin):
    """ Эндпоинт загрузки аватарки """
    def post(self, request, *args, **kwargs):
        item_profile = self.get_profile()
        file_serializer = UploadPhotoSerializer(data=request.data)
        if file_serializer.is_valid():
            new_avatar = self.add_photo(request)
            item_profile.avatar = new_avatar.image.url
            item_profile.save()
            return Response(status=201)
        else:
            return Response(status=400)
