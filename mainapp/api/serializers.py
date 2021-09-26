from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import (
    Profile,
    Photo,
    Student,
    Teacher,
    EducationalManager,
    Group,
    Dialog,
    DialogAttachment,
    Message,
    Category,
    Course,
    Lesson,
    Timetable,
    Certificate,
    AcademicPerformance,
)


class UserSerializer(serializers.ModelSerializer):
    """ Серилиазация базовой модели User
        Для отображения заявок в друзья и подписчиков
    """
    profile_id = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    date_of_birthday = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    user_group = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'profile_id', 'username', 'first_name', 'last_name', 'email', 'gender', 'date_of_birthday', 'avatar',
            'user_group', 'is_active'
        ]
        read_only_fields = (
            'profile_id', 'gender', 'date_of_birthday', 'avatar'
        )

    @staticmethod
    def get_profile_id(obj):
        return obj.profile.id

    @staticmethod
    def get_gender(obj):
        return obj.profile.gender

    @staticmethod
    def get_date_of_birthday(obj):
        return obj.profile.date_of_birthday

    @staticmethod
    def get_user_group(obj):
        return obj.profile.user_group

    @staticmethod
    def get_avatar(obj):
        if obj.profile.avatar:
            return obj.profile.avatar.image.url
        else:
            return None

    @staticmethod
    def get_is_active(obj):
        return obj.profile.is_active


class ProfileSerializerBase(serializers.ModelSerializer):
    """ Базовый класс сериализации модели пользователей
        Родительский класс сериализации
    """
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


class AvatarSerializer(serializers.ModelSerializer):
    """ Серилизация аватарки
    """
    class Meta:
        model = Photo
        fields = [
            'id', 'image',
        ]


class ProfileSerializer(ProfileSerializerBase):
    """ Сериализация модели профиля
        Для отображения пользователя в общем списке (не друзей)
    """
    avatar = AvatarSerializer()

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'username', 'first_name', 'last_name', 'middle_name', 'gender', 'avatar', 'user_group',
            'friends', 'followers', 'friend_request_in', 'friend_request_out', 'is_active'
        ]


class ProfileCreateSerializer(serializers.ModelSerializer):
    """ Серилизатор полей модели профиля необходимых для регистрации пользователя
    """
    class Meta:
        model = Profile
        fields = [
            'middle_name', 'gender', 'phone', 'date_of_birthday',
        ]


class PhotoSerializer(serializers.ModelSerializer):
    """ Серилизация модели фотографий
    """
    likes = ProfileSerializer(read_only=False, many=True)

    class Meta:
        model = Photo
        fields = [
            'id', 'image', 'date', 'likes', 'for_profile', 'description'
        ]


class PhotoUpdateDescriptionSerializer(serializers.ModelSerializer):
    """ Серилизация модели фотографий
    """

    class Meta:
        model = Photo
        fields = [
            'id', 'description'
        ]

    def update(self, instance, validated_data):
        instance.description = validated_data['description']
        instance.save()
        return instance


class GallerySerializer(serializers.ModelSerializer):
    """ Серилизация галереи пользователя
    """
    photos = PhotoSerializer(read_only=False, many=True)

    class Meta:
        model = Profile
        fields = [
            'photos',
        ]


class UploadPhotoSerializer(serializers.Serializer):
    """ Серилизация загрузки фото в галерею
    """
    image = serializers.ImageField()


class CreateProfileSerializer(serializers.Serializer):
    """ Серилизатор регистрации пользователя
    """
    username = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    profile = ProfileCreateSerializer()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        print(1)
        new_user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        print(2)
        new_user.set_password(validated_data['password'])
        new_user.save()
        print(3)
        profile_data = validated_data.pop('profile')
        Student.objects.create(
            user=new_user,
            middle_name=profile_data['middle_name'],
            phone=profile_data['phone'],
            gender=profile_data['gender'],
            date_of_birthday=profile_data['date_of_birthday']
        )
        print(4)

        return new_user


class EducationalManagerSerializer(ProfileSerializerBase):
    """ Сериализация модели менеджера учебного процесса
        Для отображения менеджера группы
    """
    class Meta:
        model = EducationalManager
        fields = [
            'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone', 'user_group',
            'is_active'
        ]


class EducationalManagerDetailSerializer(ProfileSerializerBase):
    """ Сериализация детальной модели менеджера учебного процесса
        Для отображения в друзьях
    """
    photos = PhotoSerializer(read_only=False, many=True)
    friends = UserSerializer(read_only=True, many=True)
    friend_request_in = UserSerializer(read_only=True, many=True)
    friend_request_out = UserSerializer(read_only=True, many=True)
    avatar = PhotoSerializer()

    class Meta:
        model = EducationalManager
        fields = [
            'id', 'user', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone', 'city',
            'date_of_birthday', 'photos', 'avatar', 'friends', 'followers', 'friend_request_in', 'friend_request_out',
            'user_group', 'is_active'
        ]


class GroupSerializer(serializers.ModelSerializer):
    """ Сериализация модели групп
    """
    teacher = ProfileSerializer()

    class Meta:
        model = Group
        fields = [
            'id', 'name', 'teacher'
        ]


class GroupRetrieveSerializer(serializers.ModelSerializer):
    """ Детальная сериализация модели групп (со списком одногруппников)
    """
    teacher = ProfileSerializer()
    manager = EducationalManagerSerializer()
    students = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = [
            'id', 'name', 'teacher', 'manager', 'students'
        ]

    @staticmethod
    def get_students(obj):
        students = obj.student_groups.all()
        serializer = ProfileSerializer(students, many=True)
        return serializer.data


class TeacherDetailSerializer(ProfileSerializerBase):
    """ Сериализация модели преподавателей (видят друзья)
    """
    photos = PhotoSerializer(read_only=False, many=True)
    friends = UserSerializer(read_only=True, many=True)
    friend_request_in = UserSerializer(read_only=True, many=True)
    friend_request_out = UserSerializer(read_only=True, many=True)
    group_list = GroupSerializer(read_only=True, many=True)
    avatar = PhotoSerializer()

    class Meta:
        model = Teacher
        fields = [
            'id', 'user', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone', 'city',
            'vk_slug', 'instagram_slug', 'date_of_birthday', 'education', 'professional_activity', 'about', 'courses',
            'group_list', 'photos', 'avatar', 'friends', 'followers', 'friend_request_in', 'friend_request_out',
            'user_group', 'is_active'
        ]


class StudentDetailSerializer(ProfileSerializerBase):
    """ Сериализация детальной модели студентов (видят друзья)
    """
    avatar = PhotoSerializer()

    class Meta:
        model = Student
        fields = [
            'id', 'user', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone', 'city',
            'vk_slug', 'instagram_slug', 'hobbies', 'dream', 'about', 'date_of_birthday',  'courses', 'group_list',
            'photos', 'avatar', 'friends', 'followers', 'friend_request_in', 'friend_request_out', 'user_group',
            'is_active'
        ]


class FriendsSerializer(serializers.ModelSerializer):
    """ Серилизация друзей профиля """
    friends = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = [
            'friends',
        ]


class FollowersSerializer(serializers.ModelSerializer):
    """ Серилизация подписчиков профиля """
    followers = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = [
            'followers',
        ]


class FriendsRequestInSerializer(serializers.ModelSerializer):
    """ Серилизация входящих заявок в друзья """
    friend_request_in = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = [
            'friend_request_in',
        ]


class FriendsRequestOutSerializer(serializers.ModelSerializer):
    """ Серилизация исходящих заявок в друзья (подписок)"""
    friend_request_out = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = [
            'friend_request_out',
        ]


class CategorySerializer(serializers.ModelSerializer):
    """ Серилизация модели категирий курса
    """
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """ Серилизация моделей курсов
    """
    category = CategorySerializer()
    teacher = ProfileSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """ Серилизация модели всех уроков (только список без подробностей, видео и тд)
    """
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = [
            'id', 'course', 'theme', 'lesson_number', 'is_active'
        ]


class LessonRetrieveSerializer(LessonSerializer):
    """ Серилизация модели доступных уроков
    Для открытия конкретного урока доступного пользователю
    """
    class Meta:
        model = Lesson
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    """ Серилизация модели рассписания занятий
    """
    lesson = LessonSerializer()
    group = GroupSerializer()

    class Meta:
        model = Timetable
        fields = [
            'id', 'date', 'lesson', 'group', 'is_finished'
        ]


class TimetableCreateSerializer(serializers.ModelSerializer):
    """ Серилизация добавления урока рассписание занятий
    """
    class Meta:
        model = Timetable
        fields = [
            'date', 'lesson', 'group'
        ]

    def create(self, validated_data):
        return super().create(validated_data)


class CertificateSerializer(serializers.ModelSerializer):
    """ Серилизация модели сертификатов
    """
    profile = ProfileSerializerBase()
    course = CourseSerializer()

    class Meta:
        model = Certificate
        fields = [
            'profile', 'course', 'image', 'date'
        ]


class AcademicPerformanceSerializer(serializers.ModelSerializer):
    """ Серилизация модели успеваемости
    """
    lesson = LessonSerializer()

    class Meta:
        model = AcademicPerformance
        fields = [
            'id', 'student', 'lesson', 'teacher', 'date', 'grade', 'type_grade', 'late', 'absent'
        ]

    def create(self, validated_data):
        return super().create(validated_data)


class LastMessageSerializer(serializers.ModelSerializer):
    """ Серилизация чтения личных сообщений
    """

    class Meta:
        model = Message
        fields = [
            'text', 'date_and_time', 'is_read', 'from_user'
        ]


class DialogImageSerializer(serializers.ModelSerializer):
    """ Серилизация аватара диалога
    """
    class Meta:
        model = DialogAttachment
        fields = [
            'file'
        ]


class DialogSerializer(serializers.ModelSerializer):
    """ Серилизация модели диалогов
    """
    participants = ProfileSerializer(read_only=False, many=True)
    last_message = LastMessageSerializer()
    image = DialogImageSerializer()

    class Meta:
        model = Dialog
        fields = [
            'id', 'name', 'participants', 'is_group', 'group_founder', 'image', 'last_message',
        ]


class GroupDialogUpdateSerializer(serializers.ModelSerializer):
    """ Серилизация модели диалогов для обновления названия групповой беседы
    """
    class Meta:
        model = Dialog
        fields = [
            'name'
        ]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()


class DialogAttachmentSerializer(serializers.ModelSerializer):
    """ Серилизация модели вложений к диалогу
    """
    dialog = DialogSerializer()

    class Meta:
        model = DialogAttachment
        fields = [
            'dialog', 'file'
        ]


class MessageSerializer(serializers.ModelSerializer):
    """ Серилизация отправки личных сообщений
    """

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        dialog_id = self.data.get('dialog')
        dialog = Dialog.objects.get(pk=dialog_id)
        new_message = super().create(validated_data)
        # Помещаем последнее сообщение в объект диалога
        dialog.last_message = new_message
        dialog.save()
        return new_message


class MessageViewSerializer(MessageSerializer):
    """ Серилизация чтения личных сообщений
    """
    from_user = ProfileSerializer()
    attachment = DialogAttachmentSerializer()
    dialog = DialogSerializer()

    class Meta:
        model = Message
        fields = [
            'id', 'dialog', 'from_user', 'attachment', 'text', 'date_and_time', 'is_read', 'system_message'
        ]
