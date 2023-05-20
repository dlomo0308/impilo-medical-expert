from .models import Disease


def get_disease_info(disease_name):
    """
    Retrieves the disease information for the specified disease name.
    """
    try:
        # Get the Disease object with the specified name from the database
        disease = Disease.objects.get(name=disease_name)
        symptom_names = [symptom.name for symptom in disease.symptoms.all()]
        causes_list = [cause.name for cause in disease.causes.all()]
        effects_list = [effect.name for effect in disease.effects.all()]
        # Return a dictionary containing the disease information
        return {'name': disease.name, 'description': disease.description, 'symptoms': symptom_names, 'causes': causes_list, 'treatments': disease.treatments, 'effects': effects_list}
    except Disease.DoesNotExist:
        pass
    # Return an empty dictionary if the disease information could not be retrieved
    return {}