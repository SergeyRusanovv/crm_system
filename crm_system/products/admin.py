from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "name", "description", "price"
    list_display_links = "name", "description", "price"
