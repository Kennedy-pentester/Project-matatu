from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Driver, Tout, Payment


def user_login(request):
    """Handles user login."""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, "login.html")


@login_required
def user_logout(request):
    """Logs out the user and redirects to the homepage."""
    logout(request)
    return redirect("index")


@login_required
def dashboard(request):
    """Redirect users to their respective dashboards based on their role."""
    user = request.user  # Get the logged-in user

    if hasattr(user, "driver"):  # ✅ Check if user has a driver profile
        driver = user.driver
        payments = Payment.objects.filter(driver=driver)
        return render(
            request,
            "driver_dashboard.html",
            {"driver": driver, "payments": payments},
        )

    if hasattr(user, "tout"):  # ✅ Check if user has a tout profile
        tout = user.tout
        return render(request, "tout_dashboard.html", {"tout": tout})
    # If the user is neither a driver nor a tout, redirect them
    return redirect("index")


def index(request):
    """Render the homepage."""
    return render(request, "index.html")
