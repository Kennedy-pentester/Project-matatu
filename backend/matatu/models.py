from django.db import models
from django.contrib.auth.models import User

class Matatu(models.Model):
    name = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    conductor = models.CharField(max_length=100)
    capacity = models.IntegerField(default=14)
    available_seats = models.IntegerField(default=14)

    def __str__(self):
        return self.name

class Booking(models.Model):
    matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
    passenger = models.CharField(max_length=100)
    seats = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.passenger} - {self.matatu.name}"
from django.db import models

# Create your models here.
