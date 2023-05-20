from django.urls import path
from .views import diagnosiz, results

app_name = 'diagnosiz'

urlpatterns = [
    path('diagnosiz', diagnosiz, name='diagnosiz'),
    path('results/', results, name='results'),
]