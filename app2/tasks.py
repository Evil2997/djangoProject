# app2/tasks.py

import logging
import time

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def num1_speed0(x, y):
    logger.info(f"Запуск задачи с аргументами: x={x}, y={y}")
    result = (x + y) * (x - y)
    time.sleep(5)
    logger.info(f"Задача завершена с результатом: {result}")
    return result
