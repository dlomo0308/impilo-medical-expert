import pandas as pd
from django import forms
from django.conf import settings
import os

# GENDER_CHOICES = (
#     ('Male', 'Male'),
#     ('Female', 'Female'),
# )

csv_path = getattr(settings, 'CSV_MODEL_PATH', None)
csv_file = os.path.join(csv_path, 'Testing.csv')

class SymptomForm(forms.Form):
    # gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label='Gender', required=True)    
    symptoms = forms.MultipleChoiceField(choices=(), widget=forms.SelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        symptoms_df = pd.read_csv(csv_file, ).reset_index(drop=True)
        self.fields['symptoms'].choices = sorted([(symptom, symptom) for symptom in symptoms_df.columns[:-1]])
    
    def get_method(self):
        return 'POST'
    

    # def clean_symptomz(self):
    #     selected_symptoms = []
    #     gender = self.cleaned_data['gender']
    #     if gender =='Male' and 'abnormal_menstruation' in selected_symptoms:
    #         raise forms.ValidationError("Men cannot select the 'abnormal_menstruation' symptom")
    #     return selected_symptoms




    # def clean_symptoms(self):
    #     selected_symptoms = self.cleaned_data.get('symptoms', [])
    #     print('Selected symptoms:', selected_symptoms)
    #     print('Cleaned data:', self.cleaned_data)
    #     if not selected_symptoms:
    #         raise forms.ValidationError("Please select at least one symptom.")
    #     return selected_symptoms
    
    

    

    # def clean(self):
    #     cleaned_data = super().clean()
    #     selected_symptoms = cleaned_data.get('symptoms')
    #     if selected_symptoms is None:
    #         raise forms.ValidationError("Please select at least one symptom.")
    #     return cleaned_data