from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from fruits_and_pets.serializers import FruitSerializer, PetSerializer

from .models import Fruit, Pet


class FruitsView(APIView):
    """View class at fruits/ for indexing and creating fruits."""
    def get(self, request):
        fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return Response({"fruits": serializer.data})



class FruitDetailView(APIView):
    """View class at fruits/:pk/ for showing, updating, and deleting fruits."""
    pass


class PetsView(APIView):    
    """View class at pets/ for indexing and creating pets."""
    def get(self, request):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response({"pets": serializer.data})

class PetDetailView(APIView):
    """View class at pets/:pk/ for showing, updating, and deleting pets."""
    pass