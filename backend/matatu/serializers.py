from rest_framework import serializers
from .models import Matatu, Booking

class MatatuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matatu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
