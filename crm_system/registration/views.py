from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import RegisterForm
from products.models import Product
from advertising.models import AdvertisingCompany
from customers.models import ActiveLead
from leads.models import Leads


class HomeView(TemplateView, LoginRequiredMixin):
    """Домашняя страница"""
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["products_count"] = Product.objects.count()
        data["advertisements_count"] = AdvertisingCompany.objects.count()
        data["leads_count"] = Leads.objects.count()
        data["customers_count"] = ActiveLead.objects.count()
        return data


class RegisterUser(CreateView):
    """Регистрация пользователя"""
    form_class = RegisterForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("registration:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class Login(LoginView):
    """Аутентификация пользователя"""
    template_name = "registration/login.html"
