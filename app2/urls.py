from django.urls import path

from . import views

urlpatterns = [
    path('task_status/<str:task_id>/', views.task_status, name='task_status'),
    path('start_all_tasks/', views.start_all_tasks, name='start_all_tasks'),
]
