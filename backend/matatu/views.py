from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import Matatu, Booking
from .serializers import MatatuSerializer, BookingSerializer

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    
    if user:
        login(request, user)
        return Response({"message": "Login successful!"}, status=200)
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['GET'])
def get_matatus(request):
    matatus = Matatu.objects.all()
    serializer = MatatuSerializer(matatus, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully"}, status=200)
from django.shortcuts import render

# Create your views here.
