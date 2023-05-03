from django.urls import path
from .views import diagnosis

urlpattens = [
    path('diagnosis/', diagnosis, name='diagnosis'),
]