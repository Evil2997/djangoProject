# app2/tasks.py

import time

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task()
def num1_speed0(self, x, y):
    logger.info(f'Starting task {self.request.id} with priority {self.request.delivery_info.get("priority")}')
    result = (x + y) * (x - y)
    time.sleep(5)
    logger.info(f'Task {self.request.id} completed with result {result}')
    return result


@shared_task()
def num2_speed20(x, y):
    time.sleep(20)  # Симуляция долгой задачи
    return x + y


@shared_task()
def num3_speed60(x, y):
    time.sleep(60)  # Симуляция ещё более долгой задачи
    return x * y


@shared_task()
def num4_speed120(x, y):
    time.sleep(120)  # Очень долгая задача
    return x ** y
