import json
import os
import uuid

from decimal import Decimal
from mainapp.models import Course
from yookassa import Configuration, Refund, Payment


class BuyingCourseManager:
    """ Реализация оплаты курса """
    YOKASSA_API_KEY = os.environ.get('API_YOOKASSA')
    YOKASSA_SHOP_ID = os.environ.get('YOOKASSA_SHOP_ID')

    def __init__(self, request):
        self.user = request.user.profile
        self.data = request.data
        self._return_url = None
        self._price = None

    def pay(self):
        """ Проверяет является ли пользователь студентом и существует ли данный курс """
        profile = self.user
        if profile.user_group != "student":
            return 403  # Покупают курсы только с аккаунтов студентов
        student = profile.student
        try:
            course = Course.objects.get(pk=self.data.get('id'))
        except Course.DoesNotExist:
            return 400
        if course in student.courses.all():
            return 208
        self._return_url = f"http://127.0.0.1:8080/education/{course.id}"
        self._price = Decimal(course.price).quantize(Decimal('.01'))
        print(self._price)
        response = self.get_paid_status_from_yookassa()
        # student.courses.add(course)
        return response, 201

    def get_paid_status_from_yookassa(self):
        """ Реализация взаимодействия с платежной системой YOOKASSA
        :return: объект платежа от YOOKASSA
        """
        Configuration.account_id = self.YOKASSA_SHOP_ID
        Configuration.secret_key = self.YOKASSA_API_KEY
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
            "amount": {
                "value": self._price,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": self._return_url
            },
            "capture": True,
            "description": "Заказ №1"
        }, idempotence_key)
        return payment.__dict__
