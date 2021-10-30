from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from mainapp.models import Course


class Client(models.Model):
    """ Модель клиента
    """
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Менеджер клиента', blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    passport = models.CharField(max_length=50, verbose_name='Серия и номер паспорта', blank=True, null=True)
    passport_issued_by = models.TextField(verbose_name='Кем выдан пасспорт', blank=True, null=True)
    address = models.TextField(verbose_name='Адрес прописки', blank=True, null=True)
    phone = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name='Город', blank=True, null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = '01. Клиенты'


class Contract(models.Model):
    """ Модель договор
    """
    number = models.PositiveIntegerField(verbose_name='Номер договора')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    file = models.FileField(upload_to='files/contracts', verbose_name='Файл', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Приобретенный курс')
    date = models.DateField(verbose_name='Дата')
    comment = models.TextField(verbose_name='Комментарий рекрутера')

    def __str__(self):
        return f'Договор {self.number} от {self.date}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = '02. Договоры'


class Order(models.Model):
    """ Модель заказа
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    payed = models.BooleanField(default=False, verbose_name='Оплачено')
    date_and_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = '03. Заказы'


class Request(models.Model):
    """ Модель заявки на покупку курсов
    """
    TYPE_CHOICES = ('incoming_call', 'outgoing_call', 'online', 'visit')
    TYPE_CHOICES_RUS = ('Входящий звонок', 'Исходящий звонок', 'Онлайн', 'Визит')
    TYPE_CHOICES = list(zip(TYPE_CHOICES, TYPE_CHOICES_RUS))

    STATUS_CHOICES = ('new', 'processed', 'deleted')
    STATUS_CHOICES_RUS = ('Новая', 'Обработанная', 'Удаленная')
    STATUS_CHOICES = list(zip(STATUS_CHOICES, STATUS_CHOICES_RUS))

    PURPOSE_CHOICES = ('price', 'meeting', 'info', 'details', 'repeat')
    PURPOSE_CHOICES_RUS = (
        'Узнать цену', 'Договориться о встрече', 'Получить общую информацию',
        'Уточнить детали перед заключением договора', 'Повторная консультация'
    )
    PURPOSE_CHOICES = list(zip(PURPOSE_CHOICES, PURPOSE_CHOICES_RUS))

    RESULT_CHOICES = ('contract', 'meeting', 'waiting_call', 'will_think', 'refusal', 'dissatisfied')
    RESULT_CHOICES_RUS = (
        'Заключен договор', 'Назначена встреча', 'Ждет звонка', 'Будет думать', 'Отказ', 'Недовольный клиент',
    )
    RESULT_CHOICES = list(zip(RESULT_CHOICES, RESULT_CHOICES_RUS))

    manager = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Менеджер', blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    type_request = models.CharField(max_length=50, verbose_name='Тип заявки', choices=TYPE_CHOICES)
    status = models.CharField(max_length=50, verbose_name='Статус заявки', choices=STATUS_CHOICES, default='new')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', blank=True, null=True)
    purpose = models.CharField(
        max_length=50,
        verbose_name='Цель заявки',
        choices=PURPOSE_CHOICES,
        blank=True,
        null=True
    )
    result = models.CharField(
        max_length=50,
        verbose_name='Результат заявки',
        choices=RESULT_CHOICES,
        blank=True,
        null=True
    )
    remind = models.DateField(verbose_name='Перезвонить / напомнить', blank=True, null=True)
    date = models.DateTimeField(verbose_name='Дата и время заявки', auto_now_add=True)
    comment = models.TextField(verbose_name='Комментарий менеджера')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = '04. Заявки'


class Vacancy(models.Model):
    """ Модель вакансии
    """
    name = models.CharField(max_length=50, verbose_name='Название вакансии')
    salary = models.IntegerField(verbose_name='Зарплата', blank=True, null=True)
    requirements = models.TextField(verbose_name='Требования к кандидату')
    conditions = models.TextField(verbose_name='Условия работы')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    date = models.DateField(verbose_name='Дата размещения вакансии', auto_now_add=True)
    active = models.BooleanField(verbose_name='Активная вакансия', default=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = '05. Вакансии'

    def __str__(self):
        return self.name


class Interview(models.Model):
    """ Модель собеседования
    """
    RESULT_CHOICES = ('new', 'contract', 'passed', 'not_pass', 'course')
    RESULT_CHOICES_RUS = ('Назначено', 'Заключен договор', 'Сдал', 'Не сдал', 'Рекомендованы курсы')
    RESULT_CHOICES = list(zip(RESULT_CHOICES, RESULT_CHOICES_RUS))

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Рекрутер', blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.SET_NULL, verbose_name='Вакансия', blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    age = models.IntegerField(verbose_name='Возраст')
    place_of_study = models.CharField(max_length=50, verbose_name='Место учебы')
    place_of_work = models.CharField(max_length=50, verbose_name='Место работы')
    phone = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    result = models.CharField(max_length=50, verbose_name='Результат собеседования', choices=RESULT_CHOICES)
    comment = models.TextField(verbose_name='Комментарий рекрутера', blank=True, null=True)
    date = models.DateField(verbose_name='Дата собеседования', blank=True, null=True)

    class Meta:
        verbose_name = 'Собеседование'
        verbose_name_plural = '06. Собеседования'


class CostCategory(models.Model):
    """ Модель категории затрат
    """
    name = models.CharField(max_length=50, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория затрат'
        verbose_name_plural = '07. Категории затрат'

    def __str__(self):
        return self.name


class Cost(models.Model):
    """ Модель регастрации затрат
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор записи', blank=True, null=True)
    category = models.ForeignKey(CostCategory, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name='Дата и время затраты', auto_now_add=True)
    amount = models.IntegerField(verbose_name='Сумма затрат')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    class Meta:
        verbose_name = 'Затрата'
        verbose_name_plural = '08. Затраты'
