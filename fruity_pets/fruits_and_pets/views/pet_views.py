from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from fruits_and_pets.serializers import PetSerializer, PetReadSerializer

from ..models import Pet

class PetsView(APIView):    
    """View class at pets/ for indexing and creating pets."""
    serializer_class = PetSerializer
    def get(self, request):
        pets = Pet.objects.all()
        serializer = PetReadSerializer(pets, many=True)
        return Response({"pets": serializer.data})

    def post(self, request):
        serializer = PetSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetailView(APIView):
    """View class at pets/:pk/ for showing, updating, and deleting pets."""
    def get(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        serializer = PetReadSerializer(pet)
        return Response({"pet": serializer.data})

    def patch(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        serializer = PetSerializer(pet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        pet = get_object_or_404(Pet, pk=pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)