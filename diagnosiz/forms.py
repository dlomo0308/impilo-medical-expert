import pandas as pd
from django import forms
from django.conf import settings
import os

# GENDER_CHOICES = (
#     ('Male', 'Male'),
#     ('Female', 'Female'),
# )

csv_path = getattr(settings, 'CSV_MODEL_PATH', None)
csv_file = os.path.join(csv_path, 'NewData.csv')

class SymptomForm(forms.Form):
    # gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label='Gender', required=True)    
    symptoms = forms.MultipleChoiceField(choices=(), widget=forms.SelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        symptoms_df = pd.read_csv(csv_file, ).reset_index(drop=True)
        self.fields['symptoms'].choices = sorted([(symptom, symptom) for symptom in symptoms_df.columns[:-1]])
        # self.fields['symptoms'].choices = [(symptom, symptom) for symptom in symptoms_df.columns[1:]]
    
    def get_method(self):
        return 'POST'
    
