from django.contrib.auth.models import User
from rest_framework import serializers

from mainapp import models
from management.models import Staff, Request, Client
from ..tasks import send_mail_task


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
    friends = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
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

    @staticmethod
    def get_friends(obj):
        query_set = models.User.objects.filter(profile__friends=obj.user)
        friends_serializer = UserSerializer(query_set, many=True)
        return friends_serializer.data


class AvatarSerializer(serializers.ModelSerializer):
    """ Серилизация аватарки
    """
    class Meta:
        model = models.Photo
        fields = [
            'id', 'image',
        ]


class AchievementSerializer(serializers.ModelSerializer):
    """ Серилизация ачивки
    """
    class Meta:
        model = models.Achievement
        fields = [
            'id', 'name', 'description', 'image_disable', 'image_enable'
        ]


class ProfileSerializer(ProfileSerializerBase):
    """ Сериализация модели профиля
        Для отображения пользователя в общем списке (не друзей)
    """
    avatar = AvatarSerializer()
    achievement = AchievementSerializer(many=True)

    class Meta:
        model = models.Profile
        fields = [
            'id', 'user', 'username', 'first_name', 'last_name', 'middle_name', 'gender', 'avatar', 'user_group',
            'friends', 'followers', 'friend_request_in', 'friend_request_out', 'is_active', 'about', 'is_show',
            'achievement'
        ]


class ProfileCreateSerializer(serializers.ModelSerializer):
    """ Серилизатор полей модели профиля необходимых для регистрации пользователя
    """

    class Meta:
        model = models.Profile
        fields = [
            'middle_name', 'gender', 'phone',
        ]


class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class PhotoSerializer(serializers.ModelSerializer):
    """ Серилизация модели фотографий
    """
    likes = ProfileSerializer(read_only=False, many=True)

    class Meta:
        model = models.Photo
        fields = [
            'id', 'image', 'date', 'likes', 'for_profile', 'description'
        ]


class PhotoUpdateDescriptionSerializer(serializers.ModelSerializer):
    """ Серилизация обновления описания к фотографии
    """

    class Meta:
        model = models.Photo
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
        model = models.Profile
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
        new_user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        new_user.set_password(validated_data['password'])
        new_user.save()
        profile_data = validated_data.pop('profile')
        models.Student.objects.create(
            user=new_user,
            middle_name=profile_data['middle_name'],
            phone=profile_data['phone'],
            gender=profile_data['gender'],
        )
        # send_mail_task.delay(
        #     theme='Регистрация на Future Academy',
        #     message='Благодарим за регистрацию',
        #     email_to=new_user.email,
        # )
        return new_user


class EducationalManagerSerializer(ProfileSerializerBase):
    """ Сериализация модели менеджера учебного процесса
        Для отображения менеджера группы
    """

    class Meta:
        model = Staff
        fields = [
            'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone', 'user_group',
        ]


class LessonSerializerFromTeacher(serializers.ModelSerializer):
    """ Серилизация модели всех уроков (для отоброажения в курсе). Для формирования рассписания и выставления оценок
    """

    class Meta:
        model = models.Lesson
        fields = [
            'id', 'theme', 'lesson_number', 'material_link', 'materials'
        ]


class CourseSerializerFromTeacher(serializers.ModelSerializer):
    """ Серилизация моделей курсов для преподавателей (выставление оценок, формирование рассписания)
    """
    teachers = ProfileSerializer(many=True)
    lessons = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = [
            'id', 'category', 'name', 'teachers', 'price', 'description', 'poster', 'video_presentation', 'is_finished',
            'is_active', 'lessons', 'students'
        ]

    @staticmethod
    def get_lessons(obj):
        query_set = models.Lesson.objects.filter(course=obj)
        lessons_serializer = LessonSerializerFromTeacher(query_set, many=True)
        return lessons_serializer.data

    @staticmethod
    def get_students(obj):
        students = obj.student_courses
        students_serializer = ProfileSerializer(students, many=True)
        return students_serializer.data


class GroupRetrieveSerializer(serializers.ModelSerializer):
    """ Детальная сериализация модели групп (со списком одногруппников)
    """
    manager = EducationalManagerSerializer()
    students = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.Group
        fields = [
            'id', 'name', 'manager', 'students', 'teachers', 'description', 'created_at', 'updated_at', 'image'
        ]

    @staticmethod
    def get_students(obj):
        students = obj.student_groups.all()
        serializer = ProfileSerializer(students, many=True)
        return serializer.data

    @staticmethod
    def get_teachers(obj):
        teachers = obj.teacher_groups.all()
        serializer = ProfileSerializer(teachers, many=True)
        return serializer.data


class TeacherUpdateSerializer(ProfileSerializerBase):
    """ Сериализация обновления настроек личного кабинета преподавателя
    """

    class Meta:
        model = models.Teacher
        fields = [
            'first_name', 'middle_name', 'last_name', 'email', 'phone', 'city', 'vk_slug', 'instagram_slug',
            'date_of_birthday', 'education', 'professional_activity', 'about'
        ]

    @staticmethod
    def update(instance, validated_data):
        # TODO fix user update
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class StudentDetailSerializer(ProfileSerializerBase):
    """ Сериализация детальной модели студентов (видит пользователь и друзья)
    """
    avatar = PhotoSerializer()

    class Meta:
        model = models.Student
        fields = [
            'id', 'user', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone', 'city',
            'vk_slug', 'instagram_slug', 'hobbies', 'dream', 'about', 'date_of_birthday',  'courses', 'group_list',
            'photos', 'avatar', 'friends', 'followers', 'friend_request_in', 'friend_request_out', 'user_group',
            'is_active'
        ]


class StudentUpdateSerializer(ProfileSerializerBase):
    """ Сериализация настроек личного кабинета студентов
    """

    class Meta:
        model = models.Student
        fields = [
            'first_name', 'middle_name', 'last_name', 'email', 'phone', 'city', 'vk_slug', 'instagram_slug', 'hobbies',
            'dream', 'about', 'date_of_birthday',
        ]

    @staticmethod
    def update(instance, validated_data):
        user_model_fields = ['first_name', 'last_name', 'email']
        for key, value in validated_data.items():
            setattr(instance.user, key, value) if key in user_model_fields else setattr(instance, key, value)
        instance.user.save()
        instance.save()
        return instance


class FriendsSerializer(serializers.ModelSerializer):
    """ Серилизация друзей профиля """
    friends = UserSerializer(read_only=True, many=True)

    class Meta:
        model = models.Profile
        fields = [
            'friends',
        ]


class FollowersSerializer(serializers.ModelSerializer):
    """ Серилизация подписчиков профиля """
    followers = UserSerializer(read_only=True, many=True)

    class Meta:
        model = models.Profile
        fields = [
            'followers',
        ]


class FriendsRequestInSerializer(serializers.ModelSerializer):
    """ Серилизация входящих заявок в друзья """
    friend_request_in = UserSerializer(read_only=True, many=True)

    class Meta:
        model = models.Profile
        fields = [
            'friend_request_in',
        ]


class FriendsRequestOutSerializer(serializers.ModelSerializer):
    """ Серилизация исходящих заявок в друзья (подписок)"""
    friend_request_out = UserSerializer(read_only=True, many=True)

    class Meta:
        model = models.Profile
        fields = [
            'friend_request_out',
        ]


class CitySerializer(serializers.ModelSerializer):
    """ Серилизация городов
    """
    class Meta:
        model = models.City
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """ Серилизация модели категирий курса
    """

    class Meta:
        model = models.Category
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    """ Серилизация модели ачивок
    """
    class Meta:
        model = models.Achievement
        fields = '__all__'


class ProfileAchievementSerializer(serializers.ModelSerializer):
    """ Серилизация модели ачивок пользователя
    """
    class Meta:
        model = models.Profile
        fields = ['achievement']


class SkillSerializer(serializers.ModelSerializer):
    """ Серилизация модели скиллов
    """

    class Meta:
        model = models.Skill
        fields = '__all__'


class ProfessionSkillSerializer(serializers.ModelSerializer):
    """ Серилизация модели скиллов для профессий
    """

    class Meta:
        model = models.ProfessionSkill
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    """ Серилизация модели профессий
    """
    skills = serializers.SerializerMethodField()

    class Meta:
        model = models.Profession
        fields = '__all__'

    @staticmethod
    def get_skills(obj):
        days = obj.skills.all()
        serializer = ProfessionSkillSerializer(days, many=True)
        return serializer.data


class CourseSerializer(serializers.ModelSerializer):
    """ Серилизация моделей курсов
    """
    category = CategorySerializer()
    teachers = ProfileSerializer(many=True)
    profession = ProfessionSerializer()
    skills = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    city = CitySerializer()
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }

    class Meta:
        model = models.Course
        fields = [
            'id', 'category', 'name', 'teachers', 'price', 'description', 'poster', 'video_presentation', 'is_finished',
            'is_active', 'education_type', 'duration', 'complexity', 'color_hex', 'activity_mode', 'who_is', 'content',
            'profession', 'skills', 'in_main_page', 'slug', 'html_desc', 'title', 'city', 'start_date', 'end_date',
            'lesson_count', 'lessons', 'students'
        ]

    @staticmethod
    def get_lessons(obj):
        query_set = models.Lesson.objects.filter(course=obj)
        lessons_serializer = LessonSerializerFromTeacher(query_set, many=True)
        return lessons_serializer.data

    @staticmethod
    def get_students(obj):
        students = obj.student_courses
        students_serializer = ProfileSerializer(students, many=True)
        return students_serializer.data

    @staticmethod
    def get_skills(obj):
        days = obj.skills.all()
        serializer = SkillSerializer(days, many=True)
        return serializer.data


class GroupSerializer(serializers.ModelSerializer):
    """ Сериализация модели групп
    """
    courses = CourseSerializer(read_only=False, many=True)
    students = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.Group
        fields = [
            'id', 'name', 'courses', 'students', 'teachers'
        ]

    @staticmethod
    def get_students(obj):
        students = obj.student_groups.all()
        serializer = ProfileSerializer(students, many=True)
        return serializer.data

    @staticmethod
    def get_teachers(obj):
        teachers = obj.teacher_groups.all()
        serializer = ProfileSerializer(teachers, many=True)
        return serializer.data


class TeacherDetailSerializer(ProfileSerializerBase):
    """ Сериализация модели преподавателей (видит потзователь и друзья)
    """
    avatar = PhotoSerializer()
    courses = CourseSerializerFromTeacher(many=True, read_only=True)
    group_list = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = models.Teacher
        fields = [
            'id', 'user', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'phone', 'city',
            'vk_slug', 'instagram_slug', 'date_of_birthday', 'education', 'professional_activity', 'about', 'courses',
            'group_list', 'photos', 'avatar', 'friends', 'followers', 'friend_request_in', 'friend_request_out',
            'user_group', 'is_active'
        ]


class LessonCommentSerializer(serializers.ModelSerializer):
    """ Серилизация модели комментариев к урокам
    """
    student = ProfileSerializer()

    class Meta:
        model = models.LessonComment
        fields = [
            'id', 'student', 'comment', 'created_at'
        ]


class LessonSerializer(serializers.ModelSerializer):
    """ Серилизация модели всех уроков (только список без подробностей, видео и тд)
    """
    course = CourseSerializer()

    class Meta:
        model = models.Lesson
        fields = [
            'id', 'course', 'theme', 'lesson_number', 'is_active'
        ]


class LessonRetrieveSerializer(LessonSerializer):
    """ Серилизация модели доступных уроков
    Для открытия конкретного урока доступного пользователю
    """
    comments = LessonCommentSerializer(many=True)

    class Meta:
        model = models.Lesson
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    """ Серилизация модели рассписания занятий
    """
    lesson = LessonSerializer()
    group = GroupSerializer()

    class Meta:
        model = models.Timetable
        fields = [
            'id', 'date', 'lesson', 'subject', 'group', 'is_finished', 'material', 'material_link'
        ]


class TimetableCreateSerializer(serializers.ModelSerializer):
    """ Серилизация добавления урока расписание занятий
    """

    class Meta:
        model = models.Timetable
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
        model = models.Certificate
        fields = [
            'profile', 'course', 'image', 'date'
        ]


class AcademicPerformanceSerializer(serializers.ModelSerializer):
    """ Серилизация отображения модели успеваемости
    """
    lesson = LessonSerializer()
    student = StudentDetailSerializer()

    class Meta:
        model = models.AcademicPerformance
        fields = [
            'id', 'student', 'lesson', 'teacher', 'date', 'grade', 'type_grade', 'late', 'absent', 'comment'
        ]


class AcademicPerformanceCreateSerializer(serializers.ModelSerializer):
    """ Серилизация новой оценки поставленной преподавателем
    """

    class Meta:
        model = models.AcademicPerformance
        fields = [
            'student', 'lesson', 'teacher', 'grade', 'type_grade', 'late', 'absent', 'comment'
        ]

    def create(self, validated_data):
        return super().create(validated_data)


class LastMessageSerializer(serializers.ModelSerializer):
    """ Серилизация чтения личных сообщений
    """

    class Meta:
        model = models.Message
        fields = [
            'text', 'date_and_time', 'is_read', 'from_user'
        ]


class DialogImageSerializer(serializers.ModelSerializer):
    """ Серилизация аватара диалога
    """

    class Meta:
        model = models.DialogAttachment
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
        model = models.Dialog
        fields = [
            'id', 'name', 'participants', 'is_group', 'group_founder', 'image', 'last_message',
        ]


class GroupDialogUpdateSerializer(serializers.ModelSerializer):
    """ Серилизация модели диалогов для обновления названия групповой беседы
    """

    class Meta:
        model = models.Dialog
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
        model = models.DialogAttachment
        fields = [
            'dialog', 'file'
        ]


class MessageSerializer(serializers.ModelSerializer):
    """ Серилизация отправки личных сообщений
    """

    class Meta:
        model = models.Message
        fields = '__all__'

    def create(self, validated_data):
        dialog_id = self.data.get('dialog')
        dialog = models.Dialog.objects.get(pk=dialog_id)
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
        model = models.Message
        fields = [
            'id', 'dialog', 'from_user', 'attachment', 'text', 'date_and_time', 'is_read', 'system_message'
        ]


class EventDaySerializer(serializers.ModelSerializer):
    """ Серилизация дней мероприятий
    """
    class Meta:
        model = models.EventDay
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    """ Серилизация мероприятий
    """
    speakers = ProfileSerializer(many=True)
    days = serializers.SerializerMethodField()
    city = CitySerializer()
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }

    class Meta:
        model = models.Event
        fields = [
            'id', 'name', 'signature', 'description', 'date', 'speakers', 'image', 'block_size', 'color_hex', 'slug',
            'block_image', 'days', 'text1', 'text2', 'text3', 'text_x', 'text_o', 'text_d', 'text_owl', 'content',
            'html_desc', 'title', 'open_doors_day', 'city'
        ]

    @staticmethod
    def get_days(obj):
        days = obj.event_days.all()
        serializer = EventDaySerializer(days, many=True)
        return serializer.data


class NewsSerializer(serializers.ModelSerializer):
    """ Серилизация новостей
    """
    city = CitySerializer()
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }

    class Meta:
        model = models.News
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    """ Серилизация клиентов
    """

    class Meta:
        model = Client
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    """ Серилизация заявок
    """

    class Meta:
        model = Request
        fields = '__all__'
