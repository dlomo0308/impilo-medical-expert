import pandas as pd 
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .forms import SymptomForm
from .models import Disease
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect, reverse
from django.http import QueryDict
import json
import joblib
import numpy as np
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
import os
from urllib.parse import urlencode
from .utils import get_disease_info
from .forms import csv_path, csv_file

from django.conf import settings
from .models import DiagnosedDisease
from datetime import datetime, timedelta, date
from django.utils import timezone



mode_file = os.path.join(csv_path, 'new_impilo.sav')

model = joblib.load(mode_file)
symptoms_df = pd.read_csv(csv_file)

symptoms = symptoms_df.columns[1:]

def predict_disease(selected_symptoms):
    # Convert the selected symptoms to binary format
    binary_features = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
    # reshape the binary features to match the input shape used during training
    binary_features = [binary_features]
    
    # make a prediction
    predicted_disease = model.predict(binary_features)[0]
    
    # check if the predicted disease is in your dataset
    if predicted_disease not in symptoms_df['diseases'].values:
        return 'The selected symptoms do not match any diseases in our dataset.'
    return predicted_disease


# def to_dict(self):
#         # Convert the last_diagnosis_timestamp field to a string representation
#         last_diagnosis_timestamp_str = self.last_diagnosis_timestamp.isoformat() if self.last_diagnosis_timestamp else None

@csrf_exempt
@login_required
def diagnosiz(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            selected_symptoms_json = request.POST.get("selected_symptoms")
            if selected_symptoms_json:
                selected_symptoms = json.loads(selected_symptoms_json)

                # perform prediction
                predicted_disease = predict_disease(selected_symptoms)

                # Check if the user has performed a diagnosis in the past 24 hours
                last_diagnosis_time = request.session.get('last_diagnosis_time')
                if last_diagnosis_time:
                    time_since_last_diagnosis = datetime.now(timezone.utc) - datetime.fromisoformat(last_diagnosis_time) #86400
                    if time_since_last_diagnosis.days == 0 and time_since_last_diagnosis.seconds < 86400: 
                        messages.error(request, "You can perform a diagnosis only once in 24 hours.")                
                        return redirect('diagnosiz')

                
                params = {'selected_symptoms': selected_symptoms_json, 'predicted_disease': predicted_disease}
                url = reverse('results') + '?' + urlencode(params)

                if predicted_disease: 
                    diagnosed_disease_obj = DiagnosedDisease.create(
                        userId=request.user.id, 
                        email=request.user.email, 
                        date_of_diagnosis= str(timezone.now().date()),
                        symptoms_selected= ', '.join(selected_symptoms),
                        diagnosed_disease=predicted_disease
                        )
                    diagnosed_disease_obj.save()
                # Store the current time in the session
                request.session['last_diagnosis_time'] = str(timezone.now())

                return redirect(url)
            else:
                return HttpResponse("There is an error")
        else:
            messages.error(request, "Invalid Form Data.")
            print('Invalid form data:', request.POST)
    else:
        # messages.error(request, 'Method is not POST')
        # print("Method is: "+ request.method)
        form = SymptomForm()
        context = {'form': form,
                   'title': 'Diagnosis'
                   }
        return render(request, 'pages/diagnosiz.html', context=context )
    
# results view function to show predicted results
def results(request):
    if request.method =='GET':
         # Get the selected symptoms and predicted disease from the query parameters
        selected_symptoms = request.GET.getlist('selected_symptoms')
        predicted_disease = request.GET.get('predicted_disease')
        
        # Get the disease information for the predicted disease
        disease_info = get_disease_info(predicted_disease)
        # Render the results.html template with the selected symptoms and disease information
        context = {'selected_symptoms': selected_symptoms, 'disease_info': disease_info, 'predicted_disease':predicted_disease}
        return render(request, 'pages/results.html', context)
    else:
        # If the request method is not GET, create a new DiagnosisForm instance
        messages.error(request, "Method is not GET")
    # Render the index.html template with the DiagnosisForm instance
    return render(request, 'pages/diagnosiz.html')


#diagnosis history view
@login_required
def diagnosis_history(request):
    user = request.user
    diagnoses = DiagnosedDisease.objects.filter(user=user).order_by('date_of_diagnosis')
    context = {'diagnoses':diagnoses}
    return render(request, 'pages/diagnosis_history.html', context)


# Store the timestamp of the user's last diagnosis in the session data
                # request.session['last_diagnosis_timestamp'] = timezone.now()

                



