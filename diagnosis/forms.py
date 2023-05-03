from django import forms
from .models import Symptom

class SymptomForm(forms.Form):
     symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input', 'style': 'display:none'})
    )