# app2/views.py
from celery import group
from django.http import JsonResponse
from django.shortcuts import render
import logging

from .tasks import num1_speed0

logger = logging.getLogger(__name__)

def schedule_tasks(task_list):
    tasks = []
    logger.info("Запуск создания задач...")

    for task_data in task_list:
        task = num1_speed0.si(*task_data['args']).set(priority=task_data['priority'], queue=task_data['queue'])
        tasks.append(task)

    task_group = group(tasks)
    logger.info("Задачи сформированы.")
    return task_group


def start_all_tasks(request):
    if request.method == "POST":
        task_list = [
            {'queue': 'urgent_tasks', 'priority': 1, 'args': (1, 11)},
            {'queue': 'background_tasks', 'priority': 5, 'args': (5, 55)},
            {'queue': 'urgent_tasks', 'priority': 10, 'args': (10, 10)},
            {'queue': 'background_tasks', 'priority': 1, 'args': (1, 11)},
            {'queue': 'urgent_tasks', 'priority': 2, 'args': (2, 22)},
            {'queue': 'background_tasks', 'priority': 3, 'args': (3, 4)},
            {'queue': 'urgent_tasks', 'priority': 6, 'args': (6, 66)},
            {'queue': 'background_tasks', 'priority': 3, 'args': (3, 33)},
            {'queue': 'urgent_tasks', 'priority': 4, 'args': (4, 44)},
            {'queue': 'background_tasks', 'priority': 2, 'args': (2, 22)},
            {'queue': 'urgent_tasks', 'priority': 4, 'args': (4, 44)},
            {'queue': 'background_tasks', 'priority': 1, 'args': (1, 11)},
        ]

        task_group = schedule_tasks(task_list)
        task_group.apply_async()

        return JsonResponse({'status': 'All tasks started'})

    return render(request, 'app2/start_all_tasks.html')
