from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),

]
