import os
import uuid

from decimal import Decimal
from mainapp.models import Course, Student
from rest_framework import status
from yookassa import Configuration, Refund, Payment

from management.models import Client, Order


class BuyingCourseManager:
    """ Реализация оплаты курса """
    YOKASSA_API_KEY = os.environ.get('API_YOOKASSA')
    YOKASSA_SHOP_ID = os.environ.get('YOOKASSA_SHOP_ID')

    def __init__(self, request):
        self.profile = request.user.profile
        self.course = None
        self.data = request.data

    def pay(self):
        """ Проверяет является ли пользователь студентом и существует ли данный курс """
        if self.profile.user_group != "student":
            # Покупают курсы только с аккаунтов студентов
            return {"message": "User is not a student"}, status.HTTP_403_FORBIDDEN
        try:
            self.course = Course.objects.get(pk=self.data.get('id'))
        except Course.DoesNotExist:
            return {"message": "Bad request"}, status.HTTP_400_BAD_REQUEST
        if self.course in self.profile.student.courses.all():
            return {"message": "Already reported"}, status.HTTP_208_ALREADY_REPORTED
        # if not self.check_age_group():
            # Покупать курсы можно только с правами соответствующими возрастной категории студента
            # return {"message": "Not suitable age category"}, status.HTTP_403_FORBIDDEN
        response = self.get_paid_status_from_yookassa()
        print(response)
        # add_order.delay(self.profile.id, course.id, response)
        # student.courses.add(course)
        return response, status.HTTP_201_CREATED

    def get_paid_status_from_yookassa(self):
        """ Реализация взаимодействия с платежной системой YOOKASSA
        :return: объект платежа от YOOKASSA
        """
        order = self.create_order()
        Configuration.account_id = self.YOKASSA_SHOP_ID
        Configuration.secret_key = self.YOKASSA_API_KEY
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
            "amount": {
                "value": Decimal(self.course.price).quantize(Decimal('.01')),
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": f"{os.environ.get('BASE_HOST')}/chess/{self.course.id}"
            },
            "capture": True,
            "description": f"Заказ №{order.id}"
        }, idempotence_key)
        order.payment_response_id = payment.id
        order.student = self.profile.student
        order.save()
        return payment.__dict__

    def create_order(self):
        """ Создание заказа в CRM
        :return: объект заказа
        """
        client = Client.objects.get_or_create(
            first_name=self.profile.user.first_name,
            last_name=self.profile.user.last_name,
            middle_name=self.profile.middle_name,
            phone=self.profile.phone,
            email=self.profile.user.email
        )
        order = Order.objects.get_or_create(client=client[0], course=self.course, price=self.course.price)
        return order[0]

    def check_age_group(self):
        """ Проверяет соответствие возрастной группы студента с возрастной группой приобретаемого курса
        """
        for age_group_access in self.profile.student.age_group_access.all():
            if self.course.category.age_group in age_group_access.age_group:
                return True
        return False
