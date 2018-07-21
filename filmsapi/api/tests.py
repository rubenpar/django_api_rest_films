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
        """
        Test the People model can create a person.
        """
        old_count = People.objects.count()
        self.actor.save()
        new_count = People.objects.count()
        self.assertNotEqual(old_count, new_count)



class PeopleViewTestCase(TestCase):
    """
    Test suite for the api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.client = APIClient()
        self.actor_data = {'name': 'Christopher Nolan', 'birth_date': '02/02/1975'}
        self.response = self.client.post(
            reverse('create'),
            self.actor_data,
            format="json")

    def test_api_can_create_a_person(self):
        """
        Test the api has person creation capability.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_people(self):
        """
        Test the api can get the people list.
        """

        people = People.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': people.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, people)

    def test_api_can_update_people(self):
        """
        Test the api can update a given person.
        """
        change_person = {'name': 'Something new'}
        people = People.objects.get()
        res = self.client.put(
            reverse('details', 
            kwargs={'pk': people.id}),
            change_person, 
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_people(self):
        """
        Test the api can delete a person.
        """
        people = People.objects.get()
        response = self.client.delete(
            reverse('details', 
            kwargs={'pk': people.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

