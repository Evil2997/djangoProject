# app2/views.py
from celery import group, chain, chord
from celery.result import AsyncResult
from django.http import JsonResponse
from django.shortcuts import render

from djangoProject.celery import app
from .tasks import *



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
        # Группа задач с высоким приоритетом
        urgent_tasks = group(
            num4_speed120.s(9, 99).set(priority=9, queue='urgent_tasks')
        )

        # Группа задач с низким приоритетом
        background_tasks = group(
            num1_speed0.s(1, 11).set(priority=1, queue='background_tasks'),
            num3_speed60.s(3, 33).set(priority=3, queue='background_tasks'),
            num2_speed20.s(5, 55).set(priority=5, queue='background_tasks')
        )

        # Создаем цепочку: сначала выполнится urgent_tasks, затем background_tasks
        task_chain = chain(
            chord(urgent_tasks, body=background_tasks)
        )

        result = task_chain.apply_async()
        return JsonResponse({'status': 'All tasks started', 'chain_id': result.id})
    return render(request, 'app2/start_all_tasks.html')
