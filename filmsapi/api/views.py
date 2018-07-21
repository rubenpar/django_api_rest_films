from django.shortcuts import render
from rest_framework import generics
from .serializers import PeopleSerializer
from .models import People

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
