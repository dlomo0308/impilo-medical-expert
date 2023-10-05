from django.contrib import admin
from .models import Symptom, Disease, Effect, Cause, DiagnosedDisease
# from django.http import HttpResponse
# from django.db.models import Count
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from django.urls import reverse
# from django.utils.html import format_html

# import matplotlib.pyplot as plt
# from django.shortcuts import render
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# from io import BytesIO
# import base64
# import datetime

# Register your models here.
class DiseaseAdmin(admin.ModelAdmin):
    disease_info = ('name', 'description', 'symptoms', 'causes', 'treatments', 'effects')
    ordering = ['name'] #ordering the diseases


admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Symptom)
admin.site.register(Effect)
admin.site.register(Cause)


class DiagnosedDiseaseAdmin(admin.ModelAdmin):
    list_display = ('userId', 'user', 'email', 'date_of_diagnosis', 'symptoms_selected', 'diagnosed_disease')
    list_filter = ('date_of_diagnosis', 'diagnosed_disease')
    search_fields = ('user__username', 'diagnosed_disease')

admin.site.register(DiagnosedDisease, DiagnosedDiseaseAdmin)

