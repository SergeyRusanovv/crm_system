from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import RegisterForm


class HomeView(TemplateView):
    template_name = "_base.html"


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("registration:home")


class Login(LoginView):
    template_name = "registration/login.html"
