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


csv_path = getattr(settings, 'CSV_MODEL_PATH', None)
csv_file = os.path.join(csv_path, 'Testing.csv')
mode_file = os.path.join(csv_path, 'impilo_ml_model.sav')

model = joblib.load(mode_file)
symptoms_df = pd.read_csv(csv_file)

symptoms = symptoms_df.columns[:-1]

def predict_disease(selected_symptoms):
    # Convert the selected symptoms to binary format
    binary_features = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
    # reshape the binary features to match the input shape used during training
    binary_features = [binary_features]
    
    # make a prediction
    predicted_disease = model.predict(binary_features)[0]
    return predicted_disease

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

                # redirect to results page with selected symptoms and predicted disease as URL parameters
                params = {'selected_symptoms': selected_symptoms_json, 'predicted_disease': predicted_disease}
                url = reverse('results') + '?' + urlencode(params)
                return redirect(url)
        else:
            messages.error(request, "Invalid Form Data.")
            print('Invalid form data:', request.POST)
    else:
        messages.error(request, 'Method is not POST')
        print("Method is: "+ request.method)
        form = SymptomForm()
        context = {'form': form}
        return render(request, 'pages/diagnosiz.html', context=context)


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
    return render(request, 'pages/results.html')
    






