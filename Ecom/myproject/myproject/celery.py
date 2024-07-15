from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# app.conf.broker_url = 'redis://localhost:6379//'
# app.conf.result_backend = 'redis://localhost:6379//'

app.conf.beat_schedule = {
    'send-daily-status-email': {
        'task': 'myapp.tasks.send_daily_status_email',
        'schedule': crontab(minute = '*/1'),
    },
}

# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request!r}")