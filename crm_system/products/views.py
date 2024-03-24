from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm


class ProductsList(UserPassesTestMixin, ListView):
    """Представление всех продуктов"""
    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()


class ProductDetail(UserPassesTestMixin, DetailView):
    """Детальная страница продукта"""
    model = Product
    template_name = "products/products-detail.html"
    context_object_name = "product"

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()


class ProductCreate(UserPassesTestMixin, CreateView):
    """Добавление продукта"""
    model = Product
    form_class = ProductForm
    template_name = "products/products-create.html"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()


class ProductUpdate(UserPassesTestMixin, UpdateView):
    """Редактирование продукта"""
    model = Product
    form_class = ProductForm
    template_name = "products/products-edit.html"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()


class ProductDelete(UserPassesTestMixin, DeleteView):
    """Удаление продукта"""
    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("products:products")

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()