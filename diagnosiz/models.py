from django.db import models
from django.conf import settings
import json
from datetime import datetime

class Symptom(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Cause(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Effect(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    symptoms = models.ManyToManyField(Symptom)
    causes = models.ManyToManyField(Cause)
    treatments = models.TextField(blank=True)
    effects = models.ManyToManyField(Effect)

    def __str__(self):
        return self.name
    

# TO SAVE A DIAGNOSED DISEASE
class DiagnosedDisease(models.Model):
    userId = models.IntegerField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    date_of_diagnosis = models.DateField()
    symptoms_selected = models.CharField(max_length=255, default='None')
    diagnosed_disease = models.CharField(max_length=255)

    def __str__(self):
        return f"({self.userId}) {self.user.username} ({self.email}) {self.date_of_diagnosis}: {self.symptoms_selected} => {self.diagnosed_disease}"
    
    class Meta:
        unique_together = [] #to remove uniqueness

    @classmethod
    def create(cls, userId=None, email=None, date_of_diagnosis=None, symptoms_selected=None, diagnosed_disease=None):
        diagnosed_disease_obj = cls(userId=userId, user_id=userId, email=email, date_of_diagnosis=date_of_diagnosis, symptoms_selected=symptoms_selected, diagnosed_disease=diagnosed_disease)
        return diagnosed_disease_obj


