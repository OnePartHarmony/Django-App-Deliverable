from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from fruits_and_pets.serializers import ToySerializer, ToyReadSerializer

from ..models import Toy

class ToysView(APIView):    
    """View class at toys/ for indexing and creating toys."""
    serializer_class = ToySerializer
    def get(self, request):
        toys = Toy.objects.all()
        serializer = ToyReadSerializer(toys, many=True)
        return Response({"toys": serializer.data})

    def post(self, request):
        serializer = ToySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToyDetailView(APIView):
    """View class at toys/:pk/ for showing, updating, and deleting toys."""
    def get(self, request, pk):
        toy = get_object_or_404(Toy, pk=pk)
        serializer = ToySerializer(toy)
        return Response({"toy": serializer.data})

    def patch(self, request, pk):
        toy = get_object_or_404(Toy, pk=pk)
        serializer = ToyReadSerializer(toy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        toy = get_object_or_404(Toy, pk=pk)
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)