from django.db import models


class Fruit(models.Model):
    type = models.CharField(max_length=25)
    color = models.CharField(max_length=40)
    is_ripe = models.BooleanField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        ripeness = "is not"
        if self.is_ripe:
            ripeness = "is"
        return f"A {self.color} {self.type} that {ripeness} ready to eat."


class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=40)
    age = models.IntegerField(default=1)
    is_adoptable = models.BooleanField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        adoptable = "is not"
        if self.is_adoptable:
            adoptable = "is"
        return f"{self.name} is a {self.age}-year-old {self.type} that {adoptable} adoptable."
