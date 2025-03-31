from django.urls import path
from .views import login_view, get_matatus, get_bookings, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('matatus/', get_matatus, name='matatus'),
    path('bookings/', get_bookings, name='bookings'),
    path('logout/', logout_view, name='logout'),
]
