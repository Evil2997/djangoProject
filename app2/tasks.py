# app2/tasks.py

import time

from celery import shared_task


@shared_task()
def num1_speed0(x, y):
    return (x + y) * (x - y)


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
