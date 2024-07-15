from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def main_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def books_page(request):
    return render(request, 'books.html')
