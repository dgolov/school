from django.contrib.auth import authenticate, login
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView

from .mixins import ProfileManagerMixin
from .renders import CustomBrowsableAPIRenderer
from .serializers import (
    StudentSerializer,
    TeacherSerializer,
    ManagerSerializer,
    CourseSerializer,
    LessonSerializer,
    LessonRetrieveSerializer,
    CreateProfileSerializer,
    TimetableSerializer,
    CertificateSerializer,
    AcademicPerformanceSerializer,
    UploadPhotoSerializer,
)
from ..models import (
    Student, Teacher, Manager, Group, Course, Lesson, Timetable, Certificate, AcademicPerformance
)


class AllStudentsViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка всех обучающихся """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AllTeachersViewSet(viewsets.ModelViewSet):
    """ Эндпоинт списка всех преподавателей """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProfileCreateView(CreateAPIView):
    """ Эндпоинт регистрации нового обучающегося """
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
            return Manager.objects.filter(user=user)
        else:
            return None

    def get(self, request, format=None):
        user = self.request.user
        obj = self.get_queryset(user)
        if user.profile.user_group == 'student':
            serializer = StudentSerializer(obj, many=True)
        elif user.profile.user_group == 'teacher':
            serializer = TeacherSerializer(obj, many=True)
        elif user.profile.user_group == 'manager':
            serializer = ManagerSerializer(obj, many=True)
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


class AllCoursesViewSet(viewsets.ModelViewSet):
    """  Эндпоинт списка всех курсов """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
