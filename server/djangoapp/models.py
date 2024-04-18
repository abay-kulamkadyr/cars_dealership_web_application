from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Car's make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Car's model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=100)
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023),
                    MinValueValidator(2015)])

    def __str__(self):
        return self.name
