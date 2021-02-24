from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse
from firstapp.integrations.jrapi import JrApi

# Create your tests here.
api = JrApi()
client = Client()

class IntegrationApi(TestCase):
    def test_get_all_orgs(self):
        response = client.get(reverse('listPage'))
        self.assertEqual(response.status_code, 200)


        
 