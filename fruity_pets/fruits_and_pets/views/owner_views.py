from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from fruits_and_pets.serializers import OwnerSerializer

from ..models import Owner

class OwnersView(APIView):    
    """View class at owners/ for indexing and creating owners."""
    serializer_class = OwnerSerializer
    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response({"owners": serializer.data})

    def post(self, request):
        serializer = OwnerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OwnerDetailView(APIView):
    """View class at owners/:pk/ for showing, updating, and deleting owners."""
    def get(self, request, pk):
        owner = get_object_or_404(Owner, pk=pk)
        serializer = OwnerSerializer(owner)
        return Response({"owner": serializer.data})

    def patch(self, request, pk):
        owner = get_object_or_404(Owner, pk=pk)
        serializer = OwnerSerializer(owner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        owner = get_object_or_404(Owner, pk=pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)