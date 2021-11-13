import os

from celery import shared_task
from django.core.mail import send_mail

from school.celery import app
from yookassa import Payment, Configuration
from datetime import datetime

from management.models import Order


@app.task
def send_mail_task(theme, message, email_to, email_from='facademy52@gmail.com'):
    send_mail(theme, message, email_from, [email_to], fail_silently=False)


@shared_task
def get_payed_status():
    Configuration.account_id = os.environ.get('YOOKASSA_SHOP_ID')
    Configuration.secret_key = os.environ.get('API_YOOKASSA')
    not_payed_orders = Order.objects.filter(payed=False)
    for order in not_payed_orders:
        payment_id = order.payment_response_id
        payment = Payment.find_one(payment_id)
        if payment.status == 'succeeded':
            order.payed = True
            order.student.courses.add(order.course)
            order.save()
