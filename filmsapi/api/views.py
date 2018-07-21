from django.shortcuts import render
from rest_framework import generics
from .serializers import PeopleSerializer, StudioSerializer, FilmSerializer
from .models import People, Studio, Film

class PeopleCreateView(generics.ListCreateAPIView):
    """
    This class defines the create behavior of the rest api.
    """

    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def perform_create(self, serializer):
        """
        Save the post data when creating a new bucketlist.
        """
        serializer.save()

class PeopleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class handles the http GET, PUT and DELETE requests.
    """

    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class StudioCreateView(generics.ListCreateAPIView):
    """
    This class defines the create behavior of the rest api.
    """
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

    def perform_create(self, serializer):
        """
        Save the post data when creating a new bucketlist.
        """
        serializer.save()

class StudioDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class handles the http GET, PUT and DELETE requests.
    """

    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class FilmCreateView(generics.ListCreateAPIView):
    """
    This class defines the create behavior of the rest api.
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def perform_create(self, serializer):
        """
        Save the post data when creating a new bucketlist.
        """
        serializer.save()

class FilmDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class handles the http GET, PUT and DELETE requests.
    """

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
