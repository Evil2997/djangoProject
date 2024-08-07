from django.shortcuts import render, get_object_or_404

from .models import Book


def index(request):
    return render(request, 'app1/index.html')


def about(request):
    return render(request, 'app1/about.html')


def book_list(request):
    # Проверяем, есть ли книги в базе данных
    if Book.objects.count() == 0:
        # Добавляем книги в базу данных, если их еще нет
        Book.objects.create(title="Война и мир", author="Лев Толстой", year=1869)
        Book.objects.create(title="Преступление и наказание", author="Фёдор Достоевский", year=1866)
        Book.objects.create(title="Евгений Онегин", author="Александр Пушкин", year=1833)
        Book.objects.create(title="Мёртвые души", author="Николай Гоголь", year=1842)

    books = Book.objects.all()  # Извлекаем все книги из базы данных
    return render(request, 'app1/books.html', {'books': books})  # Передаем книги в шаблон


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'app1/book_detail.html', {'book': book})

# app1/views.py
from django.http import JsonResponse
from .tasks import add
from celery.result import AsyncResult
from djangoProject.celery import app

def add_numbers(request):
    task = add.delay(4, 4)
    return JsonResponse({'task_id': task.id})

def task_status(request, task_id):
    task_result = AsyncResult(task_id, app=app)
    response = {
        'task_id': task_id,
        'state': task_result.state,
        'result': task_result.result
    }
    return JsonResponse(response)