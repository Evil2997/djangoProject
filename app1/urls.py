from django.urls import path

from .views import home, main_page, about_page, books_page

urlpatterns = [
    path('', home, name='home'),  # Маршрут для главной страницы
    path('main/', main_page, name='main'),
    path('about/', about_page, name='about'),
    path('books/', books_page, name='books'),
]
