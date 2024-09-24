from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

# Инициализация Celery с использованием RabbitMQ как брокера
app = Celery('djangoProject')

# Загрузка настроек из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Обновление конфигурации Celery
app.conf.update(
    broker_url='amqp://guest:guest@rabbitmq//',  # RabbitMQ как брокер сообщений
    result_backend='django-db',  # Используем базу данных Django для хранения результатов
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

# Автоматическое обнаружение задач из установленных приложений
app.autodiscover_tasks()
