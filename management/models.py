from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from mainapp.models import Course


class Client(models.Model):
    """ Модель клиента
    """
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    passport = models.CharField(max_length=50, verbose_name='Серия и номер паспорта', blank=True, null=True)
    passport_issued_by = models.TextField(verbose_name='Кем выдан пасспорт', blank=True, null=True)
    address = models.TextField(verbose_name='Адрес прописки', blank=True, null=True)
    phone = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Contract(models.Model):
    """ Модель договора
    """
    number = models.PositiveIntegerField(verbose_name='Номер договора')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    file = models.FileField(upload_to='files/contracts', verbose_name='Файл', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Приобретенный курс')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f'Договор {self.number} от {self.date}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Order(models.Model):
    """ Модель заказа
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    payed = models.BooleanField(default=False, verbose_name='Оплачено')
    date_and_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
