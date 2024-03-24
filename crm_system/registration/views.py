from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import RegisterForm
from products.models import Product
from advertising.models import AdvertisingCompany
from customers.models import ActiveLead
from leads.models import Leads


class HomeView(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["products_count"] = Product.objects.count()
        data["advertisements_count"] = AdvertisingCompany.objects.count()
        data["leads_count"] = Leads.objects.count()
        data["customers_count"] = ActiveLead.objects.count()
        return data


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("registration:home")


class Login(LoginView):
    template_name = "registration/login.html"
