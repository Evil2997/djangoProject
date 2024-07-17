from django.shortcuts import render


def index(request):
    return render(request, 'app1/index.html')


def about(request):
    return render(request, 'app1/about.html')


def books(request):
    return render(request, 'app1/books.html')
