from django.shortcuts import render, redirect
from .models import Matatu, Driver, Tout, Shift, Fare, Activity
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, FareForm
from django.contrib.auth.models import Group
from datetime import datetime
from django.db.models import Sum


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                print(f"DEBUG: User {user.username} authenticated successfully.")

                # Check user groups
                owner_group = user.groups.filter(name="Owner").exists()
                print(f"DEBUG: Is {user.username} in 'Owner' group? {owner_group}")

                if user.is_superuser:
                    return redirect("/myadmin/")

                elif owner_group:
                    print("DEBUG: Redirecting to admin_dashboard")
                    return redirect("admin_dashboard")

                elif Driver.objects.filter(user=user).exists():
                    return redirect("driver_dashboard")

                elif Tout.objects.filter(user=user).exists():
                    return redirect("tout_dashboard")

                else:
                    messages.error(
                        request, "You are not authorized to access this system."
                    )
                    return redirect("login")
            else:
                messages.error(request, "Invalid username or password.")

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to the login page after logout


@login_required
def driver_dashboard(request):
    driver = Driver.objects.get(user=request.user)
    shifts = Shift.objects.filter(driver=driver)
    context = {
        "driver": driver,
        "shifts": shifts,
    }
    return render(request, "fleet/driver_dashboard.html", context)


@login_required
def tout_dashboard(request):
    try:
        tout = Tout.objects.get(user=request.user)
        shifts = Shift.objects.filter(tout=tout)

        # Calculate today's fare collection for the Tout
        today_fares = Fare.objects.filter(
            shift__tout=tout, timestamp__date=datetime.today().date()
        )
        total_fare = (
            today_fares.aggregate(Sum("amount_collected"))["amount_collected__sum"] or 0
        )

        print(f"DEBUG: Logged-in Tout: {tout.user.username}")
        print(f"DEBUG: Assigned Shifts: {shifts}")
        print(f"DEBUG: Today's Total Fare: {total_fare}")

        context = {
            "tout": tout,
            "shifts": shifts,
            "total_fare": total_fare,
        }
        return render(request, "fleet/tout_dashboard.html", context)

    except Tout.DoesNotExist:
        print("DEBUG: Tout record not found for this user.")
        messages.error(request, "You are not registered as a Tout.")
        return redirect("login")


@login_required
def redirect_dashboard(request):
    user = request.user
    if user.is_superuser:
        return redirect("/myadmin/")
    elif user.groups.filter(name="Owner").exists():
        return redirect("admin_dashboard")
    elif Driver.objects.filter(user=user).exists():
        return redirect("driver_dashboard")
    elif Tout.objects.filter(user=user).exists():
        return redirect("tout_dashboard")
    else:
        messages.error(request, "You are not authorized to access this system")
        return redirect("login")


# Admin Dashboard (for the owner)
@login_required
@user_passes_test(lambda user: user.groups.filter(name="Owner").exists())
def admin_dashboard(request):
    total_matatus = Matatu.objects.count()
    total_drivers = Driver.objects.count()
    total_touts = Tout.objects.count()
    total_shifts = Shift.objects.count()

    #    fecth recent activities
    recent_activities = Activity.objects.order_by("-created_at")[:5]

    context = {
        "total_matatus": total_matatus,
        "total_drivers": total_drivers,
        "total_touts": total_touts,
        "total_shifts": total_shifts,
        "recent_activities": recent_activities,
    }

    return render(request, "fleet/admin_dashboard.html", context)


# Additional views for managing matatus, drivers, touts, and shifts
@login_required
def matatu_list(request):
    matatus = Matatu.objects.all()
    context = {"matatus": matatus}
    return render(request, "fleet/matatu_list.html", context)


@login_required
def driver_list(request):
    drivers = Driver.objects.all()
    context = {"drivers": drivers}
    return render(request, "fleet/driver_list.html", context)


@login_required
def tout_list(request):
    touts = Tout.objects.all()
    context = {"touts": touts}
    return render(request, "fleet/tout_list.html", context)


@login_required
def shift_list(request):
    shifts = Shift.objects.all()
    context = {"shifts": shifts}
    return render(request, "fleet/shift_list.html", context)


# fare collection view for Touts
@login_required
def log_fare(request):
    tout = Tout.objects.get(user=request.user)

    if request.method == "POST":
        form = FareForm(request.POST)
        form.fields["shift"].queryset = Shift.objects.filter(tout=tout)

        if form.is_valid():
            fare = form.save(commit=False)
            fare.tout = tout
            fare.save()

            # Log activity
            log_activity(
                request.user,
                f"{request.user.username} logged a fare of KES {fare.amount_collected}.",
            )

            messages.success(request, "Fare logged successfully.")
            return redirect("tout_dashboard")
    else:
        form = FareForm()
        form.fields["shift"].queryset = Shift.objects.filter(tout=tout)

    return render(request, "fleet/log_fare.html", {"form": form})


# activity log
def log_activity(user, message):
    Activity.objects.create(user=user, message=message)
