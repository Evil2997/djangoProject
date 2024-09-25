from django.urls import path

from .views import upload_chunk

urlpatterns = [
    path('upload_chunk/', upload_chunk, name='upload_chunk'),
]
