import pandas as pd
from django.test import TestCase, Client
from django.urls import reverse
from json import dumps

class DiagnosizTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.diagnosiz_url = reverse('diagnosiz')
        self.symptoms_df = pd.read_csv('C:/Users/sjr/OneDrive/Desktop/COMP SCIENCE/sjrCodes/py/DJANGO/impilo/notebook/Data/Testing.csv').reset_index(drop=True)

    def test_diagnosiz_view(self):
        # get a list of symptoms from the CSV file
        symptoms = sorted(self.symptoms_df.columns[:-1])

        # send a GET request to the URL to get the csrftoken cookie
        response = self.client.get(self.diagnosiz_url)

        # extract the csrftoken cookie from the response
        csrftoken = response.cookies['csrftoken'].value

        # send a POST request with the test data and the csrftoken cookie
        response = self.client.post(self.diagnosiz_url, {
            'selected_symptoms': dumps(symptoms),
            'csrfmiddlewaretoken': csrftoken
        })

        # check that the response is a JSON response with a predicted disease
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertIn('predicted_disease', response.json())