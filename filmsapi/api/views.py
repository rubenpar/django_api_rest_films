from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import PeopleSerializer, StudioSerializer, FilmSerializer
from .models import People, Studio, Film



class PeopleCreateView(generics.ListCreateAPIView):
    """
    Defines the GET and POST
    """

    serializer_class = PeopleSerializer

    def post(self,request, format=None):
        """
            Save the post data when creating a new person.
        """

        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        """
            Return all the people
        """
        people_list = People.objects.all()
        serializer = PeopleSerializer(people_list, many=True)
        return Response(serializer.data)


class StudioCreateView(generics.ListCreateAPIView):
    """
    This class defines the create behavior of the rest api.
    """

    serializer_class = StudioSerializer

    
    def post(self,request, format=None):
        """
            Save the post data when creating a new studio.
        """

        serializer = StudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        """
            Return all the studios
        """
        studio_list = Studio.objects.all()
        serializer = StudioSerializer(studio_list, many=True)
        return Response(serializer.data)




class FilmCreateView(generics.ListCreateAPIView):
    """
    This class defines the create behavior of the rest api.
    """
    
    serializer_class = FilmSerializer

    def post(self,request, format=None):
        """
            Save the post data when creating a new film.
        """

        print("="*50)
        print(request.data)
        # get studio if from name
        studio_id = Studio.objects.get(name=request.data["studio"]).id
        request.data["studio"]=studio_id

        # get people id from name
        director_id = People.objects.get(name=request.data["director"]).id
        request.data["director"]=director_id

        # get actors id from name
        actors_id=[]
        actors_name = request.data["actors"]
        for str_name in actors_name:
            actors_id.append(People.objects.get(name=str_name).id)
        request.data["actors"] = actors_id

        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        """
            Return all the films listed on the database
        """
        date = Film.objects.all()
        serializer = FilmSerializer(date, many=True)
        return Response(serializer.data)


class FilmYearCreateView(generics.ListCreateAPIView):
    """
    This class defines the GET method
    """

    http_method_names = ['get']
    serializer_class = FilmSerializer

    def get(self,request, year):
        """
            Return all the films released on {year}
        """
        date = Film.objects.filter(release_date__contains=year)
        serializer = FilmSerializer(date, many=True)
        return Response(serializer.data)

