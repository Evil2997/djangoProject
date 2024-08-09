# djangoProject/celery.py

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject', broker='amqp://guest:guest@rabbitmq//')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    broker_url='pyamqp://guest@localhost//',  # RabbitMQ как брокер сообщений
    result_backend='django-db',  # Используем базу данных Django для хранения результатов
    # result_backend = 'rpc://',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

app.autodiscover_tasks()
