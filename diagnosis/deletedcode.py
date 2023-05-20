# ---------from the views.py file-----------#

# symptom_indices = {symptom: index for index, symptom in enumerate(symptoms)}
# Define a function to process the selected symptoms and make a prediction
# def diagnose(selected_symptoms):
#     # Load your trained decision tree model
#     model = joblib.load('C:/Users/sjr/OneDrive/Desktop/COMP SCIENCE/sjrCodes/py/DJANGO/impilo/diagnosis/impilo_ml_model.sav')
#     form = SymptomForm()
#     symptoms = form.symptoms
#     # Convert the selected symptoms into a binary vector
#     binary_vector = np.zeros(len(symptoms))
#     for symptom in selected_symptoms:
#         binary_vector[symptoms.index(symptom)] = 1
#     # Make a prediction using the trained model
#     prediction = model.predict([binary_vector])[0]
#     return prediction

# @login_required
# def diagnosis(request):
#     form = SymptomForm()
#     context = {'form': form}
#     if request.method == 'POST':
#         form = SymptomForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data.GET('symptoms')
#             diagnosis = diagnose(selected_symptoms)
#             # print(selected_symptoms)
#             context = {'form': form, 'selected_symptoms': selected_symptoms, 'diagnose': diagnosis}
#             return render(request, 'pages/diagnosis.html', context)
#     else:
#         form = SymptomForm()
#         context = {'form': form}
#     return render(request, 'pages/diagnosis.html', context)


#SymptomForm class 
# class SymptomForm(forms.Form):
#     symptoms = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), 
#         required=True, 
#         label='',)

#     def __init__(self, *args, **kwargs):
#         choices = kwargs.pop('choices', [])
#         super(SymptomForm, self).__init__(*args, **kwargs)
#         self.fields['symptoms'].choices = [(symptom, symptom) for symptom in choices]





# ---------from the forms.py file-----------#

# class SymptomForm(forms.Form):
#      symptoms = forms.ModelMultipleChoiceField(
#         queryset=Symptom.objects.all().order_by('name'),
#         widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input', 'style': 'display:none'})
#     )
#      def __init__(self, *args, **kwargs):
#         symptoms = kwargs.pop('symptoms', []) 
#         print(f"symptoms in SymptomForm: {symptoms}")
#         super().__init__(*args, **kwargs)
#         self.fields['symptoms'].choices = [(symptom, symptom) for symptom in symptoms]

# class SymptomForm(forms.Form):
#     symptoms = forms.MultipleChoiceField(
#         choices=[(symptom, symptom) for symptom in symptoms], 
#         widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), 
#         required=True, 
#         label='')

