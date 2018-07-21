from django.shortcuts import render
from rest_framework import generics
from .serializers import PeopleSerializer
from .models import People

class PeopleCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

