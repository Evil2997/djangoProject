# app1/tasks.py
from celery import shared_task

@shared_task
def add(x, y):
    return x + y
