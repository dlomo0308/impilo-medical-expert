from django.shortcuts import render
from .models import Symptom
from .forms import SymptomForm

def diagnosis(request):
    form = SymptomForm()
    selected_symptoms = []
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
             selected_symptoms = form.cleaned_data['symptoms']
             print(selected_symptoms)
        else:
            form = SymptomForm()
        print(selected_symptoms)
    context = {'form': form, 'selected_symptoms': selected_symptoms}
    return render(request, 'pages/diagnosis.html', context)
