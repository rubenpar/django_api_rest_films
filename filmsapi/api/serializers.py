from rest_framework import serializers
from .models import People, Studio

class PeopleSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Model instance into JSON format.
    """


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = People
        fields = ('name', 'birth_date')
        
class StudioSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Model instance into JSON format.
    """


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Studio
        fields = ('name', 'city')
        