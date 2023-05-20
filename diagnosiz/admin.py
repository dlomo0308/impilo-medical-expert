from django.contrib import admin
from .models import Symptom, Disease, Effect, Cause

# Register your models here.
class DiseaseAdmin(admin.ModelAdmin):
    disease_info = ('name', 'description', 'symptoms', 'causes', 'treatments', 'effects')



admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Symptom)
admin.site.register(Effect)
admin.site.register(Cause)