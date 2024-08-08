from django.urls import path

from . import views

urlpatterns = [
    path('task_status/<str:task_id>/', views.task_status, name='task_status'),
    path('num1_speed0/', views.num1_speed0, name='num1_speed0'),
    path('num2_speed20/', views.num2_speed20, name='num2_speed20'),
    path('num3_speed60/', views.num3_speed60, name='num3_speed60'),
    path('num4_speed120/', views.num4_speed120, name='num4_speed120'),
    path('start_all_tasks/', views.start_all_tasks, name='start_all_tasks'),
]
