from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from fruits_and_pets.serializers import FruitSerializer

from ..models import Fruit

# Fruit views
class FruitsView(APIView):
    """View class at fruits/ for indexing and creating fruits."""
    serializer_class = FruitSerializer
    def get(self, request):
        fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return Response({"fruits": serializer.data})

    def post(self, request):
        serializer = FruitSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FruitDetailView(APIView):
    """View class at fruits/:pk/ for showing, updating, and deleting fruits."""
    def get(self, request, pk):
        fruit = get_object_or_404(Fruit, pk=pk)
        serializer = FruitSerializer(fruit)
        return Response({"fruit": serializer.data})

    def patch(self, request, pk):
        fruit = get_object_or_404(Fruit, pk=pk)
        serializer = FruitSerializer(fruit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        fruit = get_object_or_404(Fruit, pk=pk)
        fruit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)