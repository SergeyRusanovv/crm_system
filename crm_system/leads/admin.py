from django.contrib import admin
from .models import Leads


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = "pk", "first_name", "last_name", "phone", "advertising"
    list_display_links = "pk", "first_name", "last_name", "phone"
