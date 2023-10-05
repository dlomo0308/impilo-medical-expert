from django.urls import path
from .views import diagnosiz, results, diagnosis_history

app_name = 'diagnosiz'

urlpatterns = [
    path('diagnosiz', diagnosiz, name='diagnosiz'),
    path('diagnosis_history/', diagnosis_history, name='diagnosis_history'),
    path('results/', results, name='results'),
]