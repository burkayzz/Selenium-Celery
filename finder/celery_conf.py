from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
from kombu import Exchange, Queue

broker_url = 'amqp://guest:guest@localhost:5672/'
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'otonom.settings')

app = Celery('finder', broker=broker_url)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.task_queues = (
    
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('high_priority', Exchange('high_priority'), routing_key='high_priority'),
    Queue('low_priority', Exchange('low_priority'), routing_key='low_priority')
    
)


app.conf.task_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'


app.conf.beat_schedule = {
    'sell': {
        'task': 'finder.tasks.sell',
        'schedule': crontab(hour=9, minute=0),
                    # timedelta(minutes=5),
        'options':{'queue':'low_priority'}               
    },
    
    'trends_task': {
        'task': 'finder.tasks.trends_task',
        'schedule': crontab(hour=8, minute=0),
        'options':{'queue':'high_priority'} ,
    }
}

