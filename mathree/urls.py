from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # redirect from root URL to login page
    path("", lambda request: redirect("/accounts/login/")),
    path("myadmin/", admin.site.urls),  # django admin
    path("admin/", include("fleet.urls")),
    path("fleet/", include("fleet.urls")),  # Your app routes
    path("accounts/", include("django.contrib.auth.urls")),  # Add this for login/logout
]
# This file defines the URL patterns for the Django project. It includes the admin site and the fleet app's URLs.
# The fleet app's URLs are included under the "fleet/" path, and the Django authentication URLs are included under "accounts/".
