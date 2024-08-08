# app2/views.py

from django.http import JsonResponse
from django.shortcuts import render
from .tasks import num1_speed0, num2_speed20, num3_speed60, num4_speed120
from celery import chain, chord, group
from celery.result import AsyncResult
from djangoProject.celery import app

def task_status(request, task_id):
    task_result = AsyncResult(task_id, app=app)
    response = {
        'task_id': task_id,
        'state': task_result.state,
        'result': task_result.result
    }
    return JsonResponse(response)

def start_all_tasks(request):
    if request.method == "POST":
        urgent_tasks = [
            num1_speed0.apply_async((1, 11), priority=1, queue='urgent_tasks'),
            num1_speed0.apply_async((9, 99), priority=9, queue='urgent_tasks'),
            num1_speed0.apply_async((3, 33), priority=3, queue='urgent_tasks'),
            num1_speed0.apply_async((9, 99), priority=9, queue='urgent_tasks'),
            num1_speed0.apply_async((3, 33), priority=3, queue='urgent_tasks'),
            num1_speed0.apply_async((1, 11), priority=1, queue='urgent_tasks'),
        ]

        background_tasks = [
            num1_speed0.apply_async((9, 99), priority=9, queue='background_tasks'),
            num1_speed0.apply_async((3, 33), priority=3, queue='background_tasks'),
            num1_speed0.apply_async((1, 11), priority=1, queue='background_tasks'),
            num1_speed0.apply_async((9, 99), priority=9, queue='background_tasks'),
            num1_speed0.apply_async((3, 33), priority=3, queue='background_tasks'),
            num1_speed0.apply_async((1, 11), priority=1, queue='background_tasks'),
        ]

        return JsonResponse({
            'status': 'All tasks started',
            'urgent_task_ids': [task.id for task in urgent_tasks],
            'background_task_ids': [task.id for task in background_tasks]
        })
    return render(request, 'app2/start_all_tasks.html')
