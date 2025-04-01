from django.contrib import admin
from django.urls import path
from matatu import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("bookings/", views.bookings, name="bookings"),
]
