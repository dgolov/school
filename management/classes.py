import os
import uuid

from decimal import Decimal
from django.core.mail import send_mail
from yookassa import Configuration, Refund, Payment


class PaymentManager:
    """ Реализация оплаты курса """
    YOKASSA_API_KEY = os.environ.get('API_YOOKASSA')
    YOKASSA_SHOP_ID = os.environ.get('YOOKASSA_SHOP_ID')

    def __init__(self, order):
        self.order = order
        self.payment = None

    def get_paid_uuid(self):
        """ Реализация взаимодействия с платежной системой YOOKASSA
        :return: объект платежа от YOOKASSA
        """
        Configuration.account_id = self.YOKASSA_SHOP_ID
        Configuration.secret_key = self.YOKASSA_API_KEY
        idempotence_key = str(uuid.uuid4())
        self.payment = Payment.create({
            "amount": {
                "value": Decimal(self.order.course.price).quantize(Decimal('.01')),
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": f"{os.environ.get('BASE_HOST')}/chess/{self.order.course.id}"
            },
            "capture": True,
            "description": f"Заказ №{self.order.id}"
        }, idempotence_key)
        self.order.payment_response_id = self.payment.id
        self.order.save()
        return self.payment.__dict__

    def send_payment_url(self):
        """ Отправка ссылки на оплату клиенту
        :return:
        """
        order_url = f'https://yoomoney.ru/payments/checkout/confirmation?orderId={self.payment.id}'
        send_mail(
            'Оплата курса Академии Будущего',
            f'Ссылка на оплату:\n{order_url}',
            os.environ.get('DEFAULT_FROM_EMAIL'),
            [self.order.client.email],
            fail_silently=False
        )
