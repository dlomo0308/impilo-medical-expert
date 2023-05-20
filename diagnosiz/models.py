from django.db import models

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



