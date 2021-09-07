from django.contrib.auth.models import User
from django.db import models
# from django_fsm import FSMField
from phonenumber_field.modelfields import PhoneNumberField


USER_GROUP_CHOICES = ('admin', 'teacher', 'student')
USER_GROUP_CHOICES_RUS = ('Админ', 'Преподаватель', 'Студент')
USER_GROUP_CHOICES = list(zip(USER_GROUP_CHOICES, USER_GROUP_CHOICES_RUS))


class Group(models.Model):
    """ Модель группы обучающихся """
    name = models.CharField(max_length=50, verbose_name='Название группы')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name='Преподаватель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Profile(models.Model):
    """ Модель профиля пользователей """
    GENDER_CHOICES = ('m', 'f')
    GENDER_CHOICES_RUS = ('Мужской', 'Женский')
    GENDER_CHOICES = list(zip(GENDER_CHOICES, GENDER_CHOICES_RUS))

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    gender = models.CharField(max_length=50, verbose_name='Пол', choices=GENDER_CHOICES)
    phone = PhoneNumberField(verbose_name='Номер телефона', unique=True)
    date_of_birthday = models.DateField(verbose_name='Дата рождения')
    avatar = models.ImageField(verbose_name='Аватарка', upload_to='images/avatars', blank=True, null=True)
    friends = models.ManyToManyField(User, blank=True, verbose_name='Друзья', related_name='friends')
    user_group = models.CharField(
        max_length=50,
        verbose_name='Группа пользователей',
        choices=USER_GROUP_CHOICES,
        default='student'
    )

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.middle_name}'


class Student(Profile):
    """ Модель обучающихся """
    group = models.ManyToManyField(Group, verbose_name='Группы', blank=True)
    hobbies = models.TextField(verbose_name='Увлечения', blank=True, null=True)
    dream = models.TextField(verbose_name='Мечта', blank=True, null=True)
    courses = models.ManyToManyField(
        'Course',
        blank=True,
        verbose_name='Доступные курсы',
        related_name='student_courses'
    )

    class Meta:
        verbose_name = 'Обучающийся'
        verbose_name_plural = 'Обучающиеся'


class Teacher(Profile):
    """ Модель преподавателей """
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
        verbose_name_plural = 'Преподаватели'


class Manager(Profile):
    """ Модель менеджера учебного процесса """

    class Meta:
        verbose_name = 'Менеджер учебного процесса'
        verbose_name_plural = 'Менеджеры учебного процесса'


class Course(models.Model):
    """ Модель курса """
    name = models.CharField(max_length=100, verbose_name='Название курса')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель курса')
    price = models.DecimalField(verbose_name='Цена', max_digits=3000000, decimal_places=2)
    is_finished = models.ManyToManyField(
        Student,
        blank=True,
        verbose_name='Обучающиеся завершившие курс',
        related_name='is_finished_course'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """ Модель урока """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    theme = models.CharField(max_length=100, verbose_name='Тема урока')
    video_slug = models.SlugField(verbose_name='Ссылка на видеозапись урока', blank=True, null=True)
    lesson_number = models.PositiveIntegerField(verbose_name='Номер урока в курсе', default=1)
    description = models.TextField(verbose_name='Описание урока', blank=True, null=True)
    is_finished = models.ManyToManyField(
        Student,
        blank=True,
        verbose_name='Обучающиеся завершившие урок',
        related_name='is_finished_lesson'
    )

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Timetable(models.Model):
    """ Модель рассписания занятий """
    date = models.DateTimeField(verbose_name='Дата и время урока')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    is_finished = models.BooleanField(default=False, verbose_name='Завершен')

    def __str__(self):
        return f'{self.lesson} - {self.date}'

    class Meta:
        verbose_name = 'Рассписание урока'
        verbose_name_plural = 'Рассписание занятий'
        ordering = ['-date']


class Certificate(models.Model):
    """ Модель сертификатов о прохождении/проведении обучения """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль пользователя')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Пройденный курс')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/certificates')
    date = models.DateField(auto_now_add=True, verbose_name='Дата вручения')

    def __str__(self):
        return f'{self.profile} - {self.course}'

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class AcademicPerformance(models.Model):
    """ Модель успеваемости """
    pass
