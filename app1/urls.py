from django.urls import path
from . import views
from .views import add_numbers, task_status

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('add_numbers/', add_numbers, name='add_numbers'),
    path('task_status/<str:task_id>/', task_status, name='task_status'),

]
