from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import HomeView, RegisterUser, Login


app_name = "registration"


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("registration/", RegisterUser.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", Login.as_view(), name="login")
]
