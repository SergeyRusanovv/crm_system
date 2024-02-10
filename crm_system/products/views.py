from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm


class ProductsList(ListView):
    """Представление всех продуктов"""
    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"


class ProductDetail(DetailView):
    """Детальная страница продукта"""
    model = Product
    template_name = "products/products-detail.html"
    context_object_name = "product"


class ProductCreate(CreateView):
    """Добавление продукта"""
    model = Product
    form_class = ProductForm
    template_name = "products/products-create.html"

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProductUpdate(UpdateView):
    """Редактирование продукта"""
    model = Product
    template_name = "products/products-edit.html"
    fields = "__all__"

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProductDelete(DeleteView):
    """Удаление продукта"""
    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("products:products")
