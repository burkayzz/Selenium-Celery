from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

broker_url = 'amqp://guest:guest@localhost:5672/'
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'otonom.settings')

app = Celery('finder', broker=broker_url)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sell': {
        'task': 'finder.tasks.sell',
        'schedule': crontab(hour=9, minute=0)
                    # timedelta(minutes=5),               
    },
    
    'trends_task': {
        'task': 'finder.tasks.trends_task',
        'schedule': crontab(hour=8, minute=0)
    }
}

