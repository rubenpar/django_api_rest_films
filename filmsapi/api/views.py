from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

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
        Save the post data when creating a new person.
        """
        serializer.save()


class StudioCreateView(generics.ListCreateAPIView):
    """
    This class defines the create behavior of the rest api.
    """
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

    def perform_create(self, serializer):
        """
        Save the post data when creating a new studio.
        """
        serializer.save()


class FilmCreateView(generics.ListCreateAPIView):
    """
    This class defines the create behavior of the rest api.
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def perform_create(self, serializer):
        """
        Save the post data when creating a new film.
        """
        serializer.save()

    def retrieve(self,request, year):
        date = Film.objects.filter(release_date__contains=year)
        serializer = FilmSerializer(date, many=True)
        return Response(serializer.data)

