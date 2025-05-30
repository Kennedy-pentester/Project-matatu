from django.db import models
from django.contrib.auth.models import User


# Matatu model
class Matatu(models.Model):
    plate_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    route = models.CharField(max_length=100)

    def __str__(self):
        return self.plate_number


# Driver model
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20, unique=True)
    assigned_matatu = models.OneToOneField(
        Matatu, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.assigned_matatu.plate_number if self.assigned_matatu else 'No Matatu'}"


# Tout model
class Tout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_matatu = models.ForeignKey(
        Matatu, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.assigned_matatu}"


# Shift model
class Shift(models.Model):
    SHIFT_TYPES = [
        ("morning", "Morning"),
        ("afternoon", "Afternoon"),
        ("night", "Night"),
    ]

    matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    tout = models.ForeignKey(Tout, on_delete=models.CASCADE)
    shift_type = models.CharField(max_length=10, choices=SHIFT_TYPES, default="morning")
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.matatu} - {self.shift_type}"


# fare collection model
class Fare(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shift} - KES {self.amount_collected}"


# activity log model
class Activity(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Who triggered the activity

    def __str__(self):
        return f"{self.message} at {self.created_at}"
