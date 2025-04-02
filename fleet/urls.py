from django.urls import path
from .views import (
    driver_dashboard,
    tout_dashboard,
    login_view,
    logout_view,
    redirect_dashboard,
    admin_dashboard,
    matatu_list,
    driver_list,
    tout_list,
    shift_list,
)

urlpatterns = [
    # Login and Logout
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    # Dashboards
    path("driver/dashboard/", driver_dashboard, name="driver_dashboard"),
    path("tout/dashboard/", tout_dashboard, name="tout_dashboard"),
    path(
        "owner/dashboard/", admin_dashboard, name="admin_dashboard"
    ),  # Changed from "dashboard/" to avoid conflict
    path("redirect_dashboard/", redirect_dashboard, name="redirect_dashboard"),
    # Admin Management
    path("matatu/list/", matatu_list, name="matatu_list"),
    path("driver/list/", driver_list, name="driver_list"),
    path("tout/list/", tout_list, name="tout_list"),
    path("shift/list/", shift_list, name="shift_list"),
]
