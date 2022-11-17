from rest_framework import serializers

from .models import Fruit, Pet


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Fruit

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Pet