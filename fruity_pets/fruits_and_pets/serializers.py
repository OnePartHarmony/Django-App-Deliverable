from rest_framework import serializers

from .models import Fruit, Pet, Toy, Owner


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Fruit

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Pet

class PetReadSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        fields = "__all__"
        model = Pet

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Toy

class ToyReadSerializer(serializers.ModelSerializer):
    pet = serializers.StringRelatedField()
    class Meta:
        fields = "__all__"
        model = Toy

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Owner