from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import (
    Profile,
    Student,
    Teacher,
    Manager,
    Group,
    Course,
    Lesson,
    Timetable,
    Certificate,
    AcademicPerformance
)


class ProfileSerializer(serializers.ModelSerializer):
    """ Сериализация модели пользователей """
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'

    @staticmethod
    def get_username(obj):
        return obj.user.username

    @staticmethod
    def get_first_name(obj):
        return obj.user.first_name

    @staticmethod
    def get_last_name(obj):
        return obj.user.last_name

    @staticmethod
    def get_email(obj):
        return obj.user.email


class ProfileCreateSerializer(serializers.ModelSerializer):
    """ Серилизатор полей модели профиля необходимых для регистрации """
    class Meta:
        model = Profile
        fields = ['middle_name', 'gender', 'phone', 'date_of_birthday']


class CreateProfileSerializer(serializers.Serializer):
    """ Серилизатор регистрации сотрудника """
    username = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    profile = ProfileCreateSerializer()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        new_user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        new_user.set_password(validated_data['password'])
        new_user.save()

        profile_data = validated_data.pop('profile')
        Student.objects.create(
            user=new_user,
            middle_name=profile_data['middle_name'],
            phone=profile_data['phone'],
            gender=profile_data['gender'],
            date_of_birthday=profile_data['date_of_birthday']
        )

        return new_user


class TeacherSerializer(ProfileSerializer):
    """ Сериализация модели студентов """
    class Meta:
        model = Teacher
        fields = [
            'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone',
            'date_of_birthday', 'education', 'professional_activity'
        ]


class GroupSerializer(serializers.ModelSerializer):
    """ Сериализация модели групп """
    teacher = TeacherSerializer()

    class Meta:
        model = Group
        fields = ['id', 'name', 'teacher']


class StudentSerializer(ProfileSerializer):
    """ Сериализация модели студентов """
    group = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = Student
        fields = [
            'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone',
            'hobbies', 'dream', 'date_of_birthday', 'group'
        ]


class ManagerSerializer(ProfileSerializer):
    """ Сериализация модели менеджера учебного процесса """
    class Meta:
        model = Manager
        fields = [
            'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone',
            'date_of_birthday'
        ]


class CourseSerializer(serializers.ModelSerializer):
    """ Серилизация моделей курсов """
    teacher = TeacherSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """ Серилизация модели уроков """
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'theme', 'lesson_number']


class LessonRetrieveSerializer(LessonSerializer):
    """ Серилизация модели доступных уроков """
    class Meta:
        model = Lesson
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    """ Серилизация модели рассписания занятий """
    group = GroupSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Timetable
        fields = ['date', 'lesson', 'group', 'is_finished']


class CertificateSerializer(serializers.ModelSerializer):
    """ Серилизация модели сертификатов """
    profile = ProfileSerializer()
    course = CourseSerializer()

    class Meta:
        model = Certificate
        fields = ['profile', 'course', 'image', 'date']


class AcademicPerformanceSerializer(serializers.ModelSerializer):
    """ Серилизация модели успеваемости """
    pass
