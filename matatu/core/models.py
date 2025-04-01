from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("driver", "Driver"),
        ("admin", "Admin"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="owner")

    # Set related_name to avoid conflicts with the default User model
    groups = models.ManyToManyField(
        "auth.Group", related_name="core_user_set", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="core_user_permissions", blank=True
    )

    def __str__(self):
        return self.username


# Matatu Fleet Model
class Matatu(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    maintenance_schedule = models.DateField()
    last_serviced = models.DateField()

    def __str__(self):
        return self.name


# Driver Model
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matatu = models.ForeignKey(Matatu, on_delete=models.SET_NULL, null=True)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.matatu.name}"


# Touts Model
class Tout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matatu = models.ForeignKey(Matatu, on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.matatu.name}"


# Payment Model for Tracking Payments
class Payment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    payment_method = models.CharField(max_length=20)

    def __str__(self):
        return f"Payment of {self.amount} to {self.driver.user.username} on {self.date_paid}"


# Expense Model for Tracking Business Expenses
class Expense(models.Model):
    matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_incurred = models.DateField()

    def __str__(self):
        return (
            f"Expense of {self.amount} for {self.matatu.name} on {self.date_incurred}"
        )


# Maintenance Model to Track Matatu Maintenance
class Maintenance(models.Model):
    matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    mileage = models.IntegerField()
    date_serviced = models.DateField()

    def __str__(self):
        return f"Maintenance for {self.matatu.name} on {self.date_serviced}"


# Route Model for Matatu Route Planning
class Route(models.Model):
    matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    distance_km = models.IntegerField()

    def __str__(self):
        return (
            f"Route from {self.start_point} to {self.end_point} for {self.matatu.name}"
        )
