from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from .models import People

from datetime import datetime

class PeopleTestCase(TestCase):
    """
    Defines the people model test case
    """

    def setUp(self):
        """
        Defines the test variables
        """
        self.name = "Christopher Nolan"
        self.birth_date = "02/02/1975"
        self.actor = People(name=self.name, birth_date=self.birth_date)

    def test_model_can_create_a_bucketlist(self):
        """Test the People model can create a person."""
        old_count = People.objects.count()
        self.actor.save()
        new_count = People.objects.count()
        self.assertNotEqual(old_count, new_count)



class PeopleViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.actor_data = {'name': 'Christopher Nolan', 'birth_date': '02/02/1975'}
        self.response = self.client.post(
            reverse('create'),
            self.actor_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
