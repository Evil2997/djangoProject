# app2/views.py
import logging

from celery import group
from django.http import JsonResponse
from django.shortcuts import render

from .tasks import num1_speed0

logger = logging.getLogger(__name__)


def start_all_tasks(request):
    if request.method == "POST":
        urgent_tasks = group([
            num1_speed0.s(4, 4).set(priority=4),
            num1_speed0.s(3, 3).set(priority=3),
            num1_speed0.s(7, 7).set(priority=7),
            num1_speed0.s(3, 3).set(priority=3),
            num1_speed0.s(2, 2).set(priority=2),
            num1_speed0.s(2, 2).set(priority=2),
        ])

        background_tasks = group([
            num1_speed0.s(1, 1).set(priority=1),
            num1_speed0.s(5, 5).set(priority=5),
            num1_speed0.s(4, 4).set(priority=4),
            num1_speed0.s(2, 2).set(priority=2),
            num1_speed0.s(2, 2).set(priority=2),
            num1_speed0.s(2, 2).set(priority=2),
        ])

        urgent_result = urgent_tasks.apply_async()
        background_result = background_tasks.apply_async()

        return JsonResponse({
            'status': 'All tasks started',
            'urgent_task_ids': [task.id for task in urgent_result.results],
            'background_task_ids': [task.id for task in background_result.results],
        })

    return render(request, 'app2/start_all_tasks.html')
