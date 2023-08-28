from django.conf import settings
from django.contrib.auth import get_user_model
from smart_selects.db_fields import ChainedForeignKey
from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f" {self.name!r}"


class VehicleModel(models.Model):
    name = models.CharField(max_length=50,)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicles")

    def __str__(self):
        return f" {self.name!r}"


class ModelYear(models.Model):
    year = models.IntegerField()
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, related_name="models")

    def __str__(self):
        return f" {self.year!r}"


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50, unique=True,)
    description = models.CharField(max_length=200,)

    def __str__(self):
        return f" {self.name!r}"


class Advert(models.Model):

    class Status(models.IntegerChoices):
        DEACTIVATED = 0
        ACTIVE = 1

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, related_name="advert_vehicles")
    model = models.ForeignKey(VehicleModel, on_delete=models.PROTECT, related_name="advert_models")
    model_year = models.ForeignKey(ModelYear, on_delete=models.PROTECT, related_name="advert_year")
    photo = models.ImageField(upload_to="images", blank=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)
    engine_volume = models.DecimalField(max_digits=2, decimal_places=1)
    engine_type = models.CharField(max_length=20, choices=[('gasoline', "gasoline"),
                                                           ('diesel', "diesel"),
                                                           ('electric', "electric")
                                                           ])
    transmission = models.CharField(max_length=20, choices=[('manual', "manual"),
                                                            ('automatic', "automatic"),
                                                            ('variator', "variator")
                                                            ])
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="users")
    condition = models.CharField(max_length=30, blank=True)
    status = models.IntegerField(choices=Status.choices, default=1,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.name!r}"


bmw = Advert.objects.get(name="BMW X5")
print("______")
print(bmw.photo)

