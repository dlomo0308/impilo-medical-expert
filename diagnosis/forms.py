from django import forms
from .models import Symptom

# class SymptomForm(forms.Form):
#     symptoms = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['symptoms'].choices = self.get_symptoms_choices()

#     def get_symptoms_choices(self):
#         symptoms = Symptom.objects.order_by('name').values_list('name', flat=True)
#         return [(symptom, symptom) for symptom in symptoms]

SYMPTOM_CHOICES = tuple((symptom.name, symptom.name) for symptom in Symptom.objects.all())

class SymptomForm(forms.Form):
    symptoms = forms.MultipleChoiceField(choices=SYMPTOM_CHOICES, widget=forms.CheckboxSelectMultiple, required=True)

    def __init__(self, *args, **kwargs):
        selected_symptoms = kwargs.pop('selected_symptoms', [])
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].initial = selected_symptoms