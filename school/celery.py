import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')

app = Celery('school')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'report-pay-status': {
        'task': 'mainapp.tasks.get_payed_status',
        'schedule': 180.0,
    },
}
