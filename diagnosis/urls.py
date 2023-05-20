from django.urls import path
from .views import diagnosis, results

app_name = 'diagnosis'

urlpattens = [
    path('diagnosis/', diagnosis, name='diagnosis'),
    path('results/<str:selected_symptoms>/', results, name='results'),
    
]