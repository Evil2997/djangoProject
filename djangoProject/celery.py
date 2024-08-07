# djangoProject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения для конфигурации Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

# Создаем экземпляр Celery
app = Celery('djangoProject')

# Используем настройки из settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем задачи в приложениях Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
