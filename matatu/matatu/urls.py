# from django.contrib import admin
# from django.urls import path
# from matatu import views
# from .views import user_login, user_logout, dashboard
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", views.index, name="index"),
#     path("dashboard/", views.dashboard, name="dashboard"),
#     path("login/", user_login, name="login"),
#     path("logout/", user_logout, name="logout"),
# ]


from django.contrib import admin
from django.urls import path
from .views import user_login, user_logout, dashboard, index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
]
