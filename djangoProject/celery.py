# djangoProject/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Создание двух очередей с пользовательскими именами
app.conf.task_queues = (
    Queue('urgent_tasks', routing_key='urgent.#', queue_arguments={'x-max-priority': 10}),
    Queue('background_tasks', routing_key='background.#', queue_arguments={'x-max-priority': 10}),
)

# Настройка маршрутизации задач в соответствующие очереди
app.conf.task_routes = {
    'app2.tasks.num1_speed0': {'queue': 'background_tasks'},
    'app2.tasks.num2_speed20': {'queue': 'background_tasks'},
    'app2.tasks.num3_speed60': {'queue': 'background_tasks'},
    'app2.tasks.num4_speed120': {'queue': 'urgent_tasks'},
}

app.autodiscover_tasks()
