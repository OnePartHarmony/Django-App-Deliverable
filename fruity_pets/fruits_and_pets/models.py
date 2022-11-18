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


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)   

    def __str__(self):
        return f"{self.first_name} {self.last_name}, the {self.profession}"


class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=40)
    age = models.IntegerField(default=1)
    is_adoptable = models.BooleanField(default=1)
    owner = models.ForeignKey(
            Owner,
            on_delete=models.CASCADE,
            related_name="owned_pets"
        )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        adoptable = "is not"
        if self.is_adoptable:
            adoptable = "is"
        return f"{self.name} is a {self.age}-year-old {self.type} that {adoptable} adoptable."


class Toy(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    condition = models.CharField(max_length=40)
    is_squeaky = models.BooleanField(default=1)
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="owned_toys"
    )

    def __str__(self):
        squeaky = "is not"
        if self.is_squeaky:
            squeaky = "is"
        return f"{self.name} is a {self.condition} {self.description} that {squeaky} squeaky."
