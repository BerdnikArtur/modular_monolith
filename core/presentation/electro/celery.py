from __future__ import absolute_import, unicode_literals
import os

from config import MAILCHIMP_AUDIENCE_ID

from celery import Celery
from celery.schedules import crontab

app = Celery('electro')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_connection_retry_on_startup = True 

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-monthly-email-task': {
        'task': 'notification_management.tasks.send_email_monthly_task',
        'schedule': crontab(day_of_month=1, hour=0, minute=0),
        'args': ('Monthly Update', 'electro@gmail.com', MAILCHIMP_AUDIENCE_ID, "<h1>Hello!</h1><p>This is a test email sent via Mailchimp.</p>"),
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')