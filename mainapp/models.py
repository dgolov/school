from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


USER_GROUP_CHOICES = (
    'teacher',
    'student'
)
USER_GROUP_CHOICES_RUS = (
    'Преподаватель',
    'Студент'
)
USER_GROUP_CHOICES = list(zip(USER_GROUP_CHOICES, USER_GROUP_CHOICES_RUS))


class IntegerRangeField(models.IntegerField):
    """ Числовое поле с максимальным и минимальным значением
    """
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Group(models.Model):
    """ Модель группы обучающихся
    """
    name = models.CharField(max_length=50, verbose_name='Название группы')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name='Преподаватель')
    manager = models.ForeignKey(
        'management.Staff',
        on_delete=models.SET_NULL,
        related_name='manager',
        verbose_name='Менеджер учебного процесса',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = '01. Пользователи - Группы'


class Photo(models.Model):
    """ Модель галереи пользователей
    """
    image = models.ImageField(upload_to='images/photos', verbose_name='Изображение', max_length=None)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    likes = models.ManyToManyField('Profile', verbose_name='Лайки', blank=True, related_name='likes')
    for_profile = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = '04. Фотографии'


class Profile(models.Model):
    """ Модель профиля пользователей
    """
    GENDER_CHOICES = ('m', 'f')
    GENDER_CHOICES_RUS = ('Мужской', 'Женский')
    GENDER_CHOICES = list(zip(GENDER_CHOICES, GENDER_CHOICES_RUS))

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    gender = models.CharField(max_length=50, verbose_name='Пол', choices=GENDER_CHOICES)
    phone = PhoneNumberField(verbose_name='Номер телефона', unique=True)
    city = models.CharField(max_length=50, verbose_name='Город', blank=True, null=True)
    vk_slug = models.CharField(max_length=50, verbose_name='Ссылка на профиль vk.com', blank=True, null=True)
    instagram_slug = models.CharField(max_length=50, verbose_name='Ссылка на профиль instagram', blank=True, null=True)
    date_of_birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    about = models.TextField(verbose_name='О себе', blank=True, null=True)
    avatar = models.ForeignKey(
        Photo,
        verbose_name='Аватарка',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='avatar'
    )
    photos = models.ManyToManyField(Photo, verbose_name='Фотографии', blank=True, related_name='photo_list')
    friends = models.ManyToManyField(User, blank=True, verbose_name='Друзья', related_name='friends')
    friend_request_in = models.ManyToManyField(
        User,
        blank=True,
        verbose_name='Входящие заявки в друзья',
        related_name='in_friends')
    friend_request_out = models.ManyToManyField(
        User,
        blank=True,
        verbose_name='Исходящие заявки в друзья',
        related_name='out_friends'
    )
    followers = models.ManyToManyField(User, blank=True, verbose_name='Пописчики', related_name='followers')
    user_group = models.CharField(
        max_length=50,
        verbose_name='Группа пользователей',
        choices=USER_GROUP_CHOICES,
        default='student'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активный пользователь')
    is_show = models.BooleanField(default=False, verbose_name='Виден всем')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_fio(self):
        return f'{self.user.last_name} {self.user.first_name} {self.middle_name}'


class StudentAgeGroup(models.Model):
    """ Модель возрастных категорий студентов
    """
    AGE_GROUP_CHOICES = ('children', 'teens', 'adults')
    AGE_GROUP_CHOICES_RUS = ('Дети', 'Подростки', 'Взрослые')
    AGE_GROUP_CHOICES = list(zip(AGE_GROUP_CHOICES, AGE_GROUP_CHOICES_RUS))

    age_group = models.CharField(max_length=50, verbose_name='Возрастная категория', choices=AGE_GROUP_CHOICES)

    def __str__(self):
        return self.age_group

    class Meta:
        verbose_name = 'Возрастные группы студентов'
        verbose_name_plural = '01. Пользователи - Возрастные группы'


class Student(Profile):
    """ Модель обучающихся
    """
    group_list = models.ManyToManyField(Group, verbose_name='Группы', blank=True, related_name='student_groups')
    hobbies = models.TextField(verbose_name='Увлечения', blank=True, null=True)
    dream = models.TextField(verbose_name='Мечта', blank=True, null=True)
    verification = models.BooleanField(default=False, verbose_name='Верификация пройдена')
    age_group_access = models.ManyToManyField(
        StudentAgeGroup,
        blank=True,
        verbose_name='Доступы по возрастным категориям',
        related_name='student_age_group_access'
    )
    courses = models.ManyToManyField(
        'Course',
        blank=True,
        verbose_name='Доступные курсы',
        related_name='student_courses'
    )

    class Meta:
        verbose_name = 'Обучающийся'
        verbose_name_plural = '01. Пользователи - Обучающиеся'


class Teacher(Profile):
    """ Модель преподавателей
    """
    group_list = models.ManyToManyField(Group, verbose_name='Группы', blank=True, related_name='teacher_groups')
    education = models.CharField(max_length=100, verbose_name='Образование', blank=True, null=True)
    professional_activity = models.CharField(
        max_length=150,
        verbose_name='Профессиональная деятельность',
        blank=True,
        null=True
    )
    courses = models.ManyToManyField(
        'Course',
        blank=True,
        verbose_name='Курсы проводимые преподователем',
        related_name='teacher_courses'
    )

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = '01. Пользователи - Преподаватели'


class Dialog(models.Model):
    """ Модель диалога
    """
    name = models.CharField(max_length=100, verbose_name='Название диалога')
    participants = models.ManyToManyField(
        Profile,
        blank=True,
        verbose_name='Участники диалога',
        related_name='participants'
    )
    is_group = models.BooleanField(default=False, verbose_name='Беседа')
    last_message = models.ForeignKey(
        'Message',
        on_delete=models.CASCADE,
        verbose_name='Последнее сообщение',
        related_name='last_message',
        blank=True,
        null=True
    )
    group_founder = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        verbose_name='Основатель беседы',
        blank=True,
        null=True,
        related_name='group_founder'
    )
    image = models.ForeignKey(
        'DialogAttachment',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Изображение диалога',
        related_name='dialog_image'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Диалог'
        verbose_name_plural = '03. Личные сообщения - Диалоги'


class DialogAttachment(models.Model):
    """ Модель вложений диалога
    """
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE, verbose_name='Диалог')
    file = models.FileField(upload_to='files/messages_files', verbose_name='Файл')
    from_user = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Пользователь'
    )

    def __str__(self):
        return f'{self.file} - {self.dialog}'

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = '03. Личные сообщения - Вложения в диалогах'


class Message(models.Model):
    """ Модель личных сообщений
    """
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE, verbose_name='Диалог', related_name='dialog')
    from_user = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        verbose_name='От кого',
        related_name='from_user',
        blank=True,
        null=True   # На случай удаления пользователя
    )
    text = models.TextField(verbose_name='Текст сообщения', blank=True, null=True)
    date_and_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время сообщения')
    attachment = models.ForeignKey(
        DialogAttachment,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Вложение'
    )
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    system_message = models.BooleanField(default=False, verbose_name='Системное сообщение')

    def __str__(self):
        return f'{self.from_user} - {self.text}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = '03. Личные сообщения - Сообщения'


class Category(models.Model):
    """ Модель категории курса
    """
    AGE_GROUP_CHOICES = ('children', 'teens', 'adults')
    AGE_GROUP_CHOICES_RUS = ('Дети', 'Подростки', 'Взрослые')
    AGE_GROUP_CHOICES = list(zip(AGE_GROUP_CHOICES, AGE_GROUP_CHOICES_RUS))

    name = models.CharField(max_length=100, verbose_name='Название Категории')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    age_group = models.CharField(max_length=50, verbose_name='Возрастная категория', choices=AGE_GROUP_CHOICES)
    how_is_the_training = models.TextField(verbose_name='Как проходит обучение', blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.age_group})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = '02. Обучение - Категории'
        ordering = ['id']


class Course(models.Model):
    """ Модель курса
    """
    TYPE_CHOICES = ('course', 'profession')
    TYPE_CHOICES_RUS = ('Курс', 'Профессия')
    TYPE_CHOICES = list(zip(TYPE_CHOICES, TYPE_CHOICES_RUS))

    COMPLEXITY_CHOICES = ('newbie', 'user', 'professional', 'cheater')
    COMPLEXITY_CHOICES_RUS = ('Новичок', 'Пользователь', 'Профессионал', 'Читер')
    COMPLEXITY_CHOICES = list(zip(COMPLEXITY_CHOICES, COMPLEXITY_CHOICES_RUS))

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)
    education_type = models.CharField(
        max_length=50,
        verbose_name='Тип обучения',
        choices=TYPE_CHOICES,
        default='course'
    )
    duration = models.IntegerField(verbose_name='Длительность обучения')
    complexity = models.CharField(max_length=50, verbose_name='Сложность', choices=COMPLEXITY_CHOICES, default='newbie')
    name = models.CharField(max_length=100, verbose_name='Название курса')
    teachers = models.ManyToManyField(
        Teacher,
        verbose_name='Преподаватели курса',
        blank=True,
        related_name='course_teachers'
    )
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    content = models.TextField(verbose_name='Содержание', blank=True, null=True)
    activity_mode = models.CharField(max_length=50, verbose_name='Режим заниятий', blank=True, null=True)
    profession = models.ForeignKey(
        'Profession',
        on_delete=models.CASCADE,
        verbose_name='Профессия',
        blank=True,
        null=True
    )
    who_is = models.TextField(verbose_name='Блок кто такой', blank=True, null=True)
    # skills = models.ManyToManyField('Skill', blank=True, verbose_name='Вы научитесь', related_name='skills')
    poster = models.ImageField(upload_to='images/posters', verbose_name='Изображение курса', blank=True, null=True)
    video_presentation = models.SlugField(verbose_name='Ссылка на видеопрезентацию курса', blank=True, null=True)
    color_hex = models.CharField(max_length=10, verbose_name='Цвет блока курса (hex)', blank=True, null=True)
    is_finished = models.ManyToManyField(
        Student,
        blank=True,
        verbose_name='Обучающиеся завершившие курс',
        related_name='is_finished_course'
    )
    is_active = models.BooleanField(default=True, verbose_name='Доступный курс')
    in_main_page = models.BooleanField(default=False, verbose_name='На главной странице')
    slug = models.SlugField(max_length=50, verbose_name='Ссылка', unique=True, blank=True, null=True)
    title = models.CharField(max_length=50, verbose_name='Title', blank=True, null=True)
    html_desc = models.TextField(verbose_name='Описание для поисковиков', blank=True, null=True)
    header = models.CharField(max_length=50, verbose_name='Заголовок h1', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = '02. Обучение - Курсы'


class Skill(models.Model):
    """ Модель скиллов (Блок "Вы научитесь в курсе")
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='skills')
    text = models.TextField(verbose_name='Текс навыка')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = '02. Обучение - Навыки'


class Profession(models.Model):
    """ Модель професии
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    salary_resume = models.CharField(max_length=100, verbose_name='Зарплата в резюме')
    salary_junior = models.CharField(max_length=100, verbose_name='Зарплата Junior')
    salary_middle = models.CharField(max_length=100, verbose_name='Зарплата Middle')
    salary_senior = models.CharField(max_length=100, verbose_name='Зарплата Senior')
    junior_name = models.CharField(max_length=100, verbose_name='Junior название блока', default='Junior')
    middle_name = models.CharField(max_length=100, verbose_name='Middle название блока', default='Middle')
    senior_name = models.CharField(max_length=100, verbose_name='Senior название блока', default='Senior')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Провессия'
        verbose_name_plural = '02. Обучение - Провессии'


class ProfessionSkill(models.Model):
    """ Модель скиллов (Блок "Вы научитесь в курсе")
    """
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name='Проессия', related_name='skills')
    text = models.TextField(verbose_name='Текс навыка')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = '02. Обучение - Профессии - Навыки'


class Lesson(models.Model):
    """ Модель урока
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    theme = models.CharField(max_length=100, verbose_name='Тема урока')
    video_slug = models.CharField(max_length=100, verbose_name='Ссылка на видеозапись урока', blank=True, null=True)
    lesson_number = models.PositiveIntegerField(verbose_name='Номер урока в курсе', default=1)
    description = models.TextField(verbose_name='Описание урока', blank=True, null=True)
    materials = models.FileField(
        upload_to='files/courses/materials',
        verbose_name='Материалы курса',
        blank=True,
        null=True
    )
    is_finished = models.ManyToManyField(
        Student,
        blank=True,
        verbose_name='Обучающиеся завершившие урок',
        related_name='is_finished_lesson'
    )
    is_active = models.BooleanField(default=True, verbose_name='Доступный урок')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = '02. Обучение - Уроки'


class Timetable(models.Model):
    """ Модель рассписания занятий
    """
    date = models.DateTimeField(verbose_name='Дата и время урока')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    is_finished = models.BooleanField(default=False, verbose_name='Завершен')

    def __str__(self):
        return f'{self.lesson} - {self.date}'

    class Meta:
        verbose_name = 'Рассписание урока'
        verbose_name_plural = '02. Обучение - Рассписание занятий'
        ordering = ['-date']


class Certificate(models.Model):
    """ Модель сертификатов о прохождении/проведении обучения
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль пользователя')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Пройденный курс')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/certificates')
    date = models.DateField(auto_now_add=True, verbose_name='Дата вручения')

    def __str__(self):
        return f'{self.profile} - {self.course}'

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = '02. Обучение - Сертификаты'


class AcademicPerformance(models.Model):
    """ Модель успеваемости по 10 бальной шкале
    """
    TYPE_CHOICES = ('homework', 'classwork', 'test', 'examination')
    TYPE_CHOICES_RUS = ('Домашняя работа', 'Класная работа', 'Контрольная работа', 'Экзамен')
    TYPE_CHOICES = list(zip(TYPE_CHOICES, TYPE_CHOICES_RUS))

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Обучающийся')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата оценки')
    type_grade = models.CharField(max_length=50, verbose_name='Тип оценки', choices=TYPE_CHOICES)
    grade = IntegerRangeField(min_value=1, max_value=10, verbose_name='Оценка')
    late = models.BooleanField(default=False, verbose_name='Опоздание')
    absent = models.BooleanField(default=False, verbose_name='Отсутствие')

    def __str__(self):
        return f'{self.student} - {self.lesson} - {self.date}'

    class Meta:
        verbose_name = 'Успеваемость'
        verbose_name_plural = '02. Обучение - Успеваемость'
        ordering = ['-date']


class Event(models.Model):
    """ Модель мероприятия
    """
    SIZE_CHOICES = ('small', 'medium', 'big')
    SIZE_CHOICES_RUS = ('Маленький', 'Средний', 'Большой')
    SIZE_CHOICES = list(zip(SIZE_CHOICES, SIZE_CHOICES_RUS))

    name = models.CharField(max_length=100, verbose_name='Название')
    signature = models.CharField(max_length=100, verbose_name='Подпись к мероприятию')
    text1 = models.CharField(max_length=100, verbose_name='Текст 1 (в шапке)', blank=True, null=True)
    text2 = models.CharField(max_length=100, verbose_name='Текст 2 (в шапке)', blank=True, null=True)
    text3 = models.CharField(max_length=100, verbose_name='Текст 3 (в шапке)', blank=True, null=True)
    text_owl = models.CharField(max_length=100, verbose_name='Текст в сове', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    content = models.TextField(verbose_name='Содержание мероприятия', blank=True, null=True)
    text_x = models.CharField(max_length=100, verbose_name='Текст Х', blank=True, null=True)
    text_o = models.CharField(max_length=100, verbose_name='Текст О', blank=True, null=True)
    text_d = models.CharField(max_length=100, verbose_name='Текст Д', blank=True, null=True)
    date = models.DateTimeField(verbose_name='Дата и время')
    speakers = models.ManyToManyField(Teacher, verbose_name='Спикеры', blank=True, related_name='event_speakers')
    image = models.ImageField(upload_to='images/events', verbose_name='Изображение', blank=True, null=True)
    block_size = models.CharField(max_length=20, verbose_name='Размер блока', choices=SIZE_CHOICES, default='small')
    color_hex = models.CharField(max_length=10, verbose_name='Цвет блока мероприятия (hex)', blank=True, null=True)
    block_image = models.BooleanField(default=False, verbose_name='Обложка блока картинкой')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = '05. Мероприятия'
        ordering = ['-date']


class EventDay(models.Model):
    """ Модель дня мероприятия
    """
    number = models.IntegerField(verbose_name='День мероприятия')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие', related_name='event_days')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.event} - день {self.number}'

    class Meta:
        verbose_name = 'Дни мероприятий'
        verbose_name_plural = '05. Мероприятия - Дни'


class News(models.Model):
    """ Модель новости
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    introduction = models.TextField(verbose_name='Вступление новости', blank=True, null=True)
    text = models.TextField(verbose_name='Текст новости', blank=True, null=True)
    date = models.DateField(verbose_name='Дата публикации')
    image = models.ImageField(upload_to='images/news', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = '06. Новости'
        ordering = ['-date']
