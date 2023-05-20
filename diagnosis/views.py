from django.shortcuts import render, redirect
from django.contrib import sessions
from django.urls import reverse
from django.contrib import messages
from .models import Symptom
from .forms import SymptomForm
from django.contrib.auth.decorators import login_required, user_passes_test
import pickle
import joblib
import pandas as pd
from django.http import HttpResponse



# SYMPTOMS_CSV_PATH = '../notebook/Data/Testing.csv'
# MODEL_PICKLE_PATH = '../notebook/ml_model.ipynb'

# def encode_symptoms(selected_symptoms):
#     symptoms_df = pd.read_csv(SYMPTOMS_CSV_PATH)
#     selected_symptoms_encoded = pd.DataFrame(0, index=[0], columns=symptoms_df.columns) #it should exclude the diseases column
#     for symptom in selected_symptoms:
#         selected_symptoms_encoded[symptom] = 1
#     return selected_symptoms_encoded

# def load_model():
#     model = joblib.load(MODEL_PICKLE_PATH)
#     return model

# #WHAT EXACTLY IS HAPPENING HERE
# def predict_disease(selected_symptoms_encoded, model): 
#     probabilities = model.predict_proba(selected_symptoms_encoded)
#     predicted_disease_index = probabilities.argmax()
#     predicted_disease = model.classes_[predicted_disease_index]
#     return predicted_disease

# @login_required
# def diagnosis(request):
#     symptoms = Symptom.objects.order_by('name')
#     form = SymptomForm()
#     if request.method == 'POST':
#         form = SymptomForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data.getlist('symptoms')
#             selected_symptoms_encoded = encode_symptoms(selected_symptoms)
#             model = load_model()
#             predicted_disease = predict_disease(selected_symptoms_encoded, model)
#             request.session['selected_symptoms'] = selected_symptoms
#             request.session['predicted_disease'] = predicted_disease
#             return 
#         form.fields['symptoms'].choices=[(symptom,symptom) for symptom in symptoms]
#     else:
#         selected_symptoms = request.session.get('selected_symptoms', None)
#         print("Invalid form data: ", request.POST)
#         form = SymptomForm()
#         form.fields['symptoms'].choices=[(symptom,symptom) for symptom in symptoms]
#     context = {'form':form}
#     return render(request, 'pages/diagnosis.html', context)

# @login_required
# def results(request):
#     selected_symptoms = request.session.get('selected_symptoms', None)
#     if not selected_symptoms:
#         # messages.error(request, 'Symptoms are not being passed')
#         return redirect('diagnosis')

#     predicted_disease = request.session.get('predicted_disease', '')

#     context = {'selected_symptoms': selected_symptoms, 'predicted_disease': predicted_disease}
#     return render(request, 'pages/results.html', context)












# model = pickle.load(open('C:/Users/sjr/OneDrive/Desktop/COMP SCIENCE/sjrCodes/py/DJANGO/impilo/diagnosis/impilo_ml_model.sav', 'rb'))


@login_required
def diagnosis(request):
    symptoms = Symptom.objects.order_by('name')
    form = SymptomForm()
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            selected_symptoms = form.cleaned_data.getlist('symptoms')
            request.session['selected_symptoms'] = selected_symptoms
            url = reverse('results') + '?symptoms=' + ','.join(selected_symptoms)
            return redirect(url)
        form.fields['symptoms'].choices=[(symptom,symptom) for symptom in symptoms]
    else:
        selected_symptoms = request.session.get('selected_symptoms', None)
        form = SymptomForm(selected_symptoms=selected_symptoms)
        form.fields['symptoms'].choices=[(symptom,symptom) for symptom in symptoms]
    context = {'form':form}
    return render(request, 'pages/diagnosis.html', context)

def results(request):
    selected_symptoms = request.GET.get('symptoms', None)
    if selected_symptoms:
        selected_symptoms = selected_symptoms.split(',')
        form = SymptomForm(initial={'symptoms': selected_symptoms})
        context = {'selected_symptoms': selected_symptoms, 'form': form}
        return render(request, 'pages/results.html', context)
    else:
        messages.warning(request, 'Selected symptoms were not passed')
        return redirect('diagnosis')

# def results(request):
#     selected_symptoms = request.session.get('selected_symptoms')
#     if selected_symptoms:
#         form = SymptomForm(initial={'symptoms': selected_symptoms}, selected_symptoms=selected_symptoms)
#         context = {'selected_symptoms': selected_symptoms, 'form': form}
#         return render(request, 'pages/results.html', context)
#     else:
#         return redirect('diagnosis')
   

# def diagnosis(request):
#     symptoms = Symptom.objects.order_by('name')
#     selected_symptoms = request.session.get('selected_symptoms')
#     form = SymptomForm(selected_symptoms=selected_symptoms)
#     if request.method == 'POST':
#         form = SymptomForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data.getlist('symptoms')
#             request.session['selected_symptoms'] = selected_symptoms
#             return redirect('results')
#         form.fields['symptoms'].choices=[(symptom,symptom) for symptom in symptoms]
#     context = {'form':form}
#     return render(request, 'pages/diagnosis.html', context)
