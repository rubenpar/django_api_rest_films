from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from .models import People, Studio, Film

from datetime import datetime

#################
## Test Models ##
#################

class PeopleTestCase(TestCase):
    """
    Defines the people model test case
    """

    def setUp(self):
        """
        Defines the test variables
        """
        self.name = "test_a"
        self.birth_date = "02/02/1975"
        self.actor = People(name=self.name, birth_date=self.birth_date)

    def test_model_can_create_a_person(self):
        """
        Test the People model can create a person.
        """
        old_count = People.objects.count()
        self.actor.save()
        new_count = People.objects.count()
        self.assertNotEqual(old_count, new_count)

class StudioTestCase(TestCase):
    """
    Defines the Studio model test case
    """

    def setUp(self):
        """
        Defines the test variables
        """
        self.name = "test_a"
        self.city = "test_city"
        self.studio = Studio(name=self.name, city=self.city)

    def test_model_can_create_a_studio(self):
        """
        Test the Studio model can create a studio.
        """
        old_count = Studio.objects.count()
        self.studio.save()
        new_count = Studio.objects.count()
        self.assertNotEqual(old_count, new_count)

class FilmTestCase(TestCase):
    """
    Defines the Film model test case
    """

    def setUp(self):
        """
        Defines the test variables
        """
        self.title = "test_a"
        self.studio = Studio.objects.create(name="test_b", city="test_b")
        self.release_date = "1st Feb 2015"
        self.director = People.objects.create(name="test_b", birth_date="00/00/2000")
        self.actors = [People.objects.create(name="test_", birth_date="00/00/2000")]
        self.film = Film.objects.create(title=self.title, 
                            studio=self.studio,
                            release_date=self.release_date,
                            director = self.director,
                            )

    def test_model_can_create_a_film(self):
        """
        Test the Film model can create a film.
        """
        self.assertEqual(self.film.title, "test_a")

#################
## Test Api ##
#################
class APITestCase(TestCase):
    """
    Test post case.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.client = APIClient()
        self.actor_data = {"name": "test_c", "birth_date": "02/02/1975"}
        self.studio_data = {"name": "test_c", "city": "Madrid"}
        self.film_data = {"title": "test_film",
                    "studio": "test_c",
                    "release_date": "3rd May 2018",
                     "director": "test_c",
                    "actors": ["test_c"]
                   }

    def test_api_can_create_a_person(self):
        """
        Test the api has person creation capability.
        """

        self.response = self.client.post(
            reverse("create_person"),
            self.actor_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_api_can_create_a_studio(self):
        """
        Test the api has studio creation capability.
        """

        self.response = self.client.post(
            reverse("create_studio"),
            self.studio_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # def test_api_can_create_a_film(self):
    #     """
    #     Test the api has film creation capability.
    #     """

    #     print(Studio.objects.all())
    #     self.response = self.client.post(
    #         reverse("create_film"),
    #         self.film_data,
    #         format="json")
    #     self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # def test_api_can_get_people(self):
    #     """
    #     Test the api can get the people list.
    #     """

    #     people = People.objects.get()
    #     response = self.client.get(
    #         reverse("details",
    #         kwargs={"pk": people.id}),
    #         format="json"
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertContains(response, people)

    
