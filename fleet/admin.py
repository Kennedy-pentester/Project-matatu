from django.contrib import admin
from .models import Matatu, Driver, Tout, Shift
from django.contrib.auth.models import User


class DriverAdmin(admin.ModelAdmin):
    list_display = ("user", "license_number", "assigned_vehicle")


class ToutAdmin(admin.ModelAdmin):
    list_display = ("user", "assigned_vehicle")


admin.site.register(Matatu)
admin.site.register(Driver)
admin.site.register(Tout)
admin.site.register(Shift)
