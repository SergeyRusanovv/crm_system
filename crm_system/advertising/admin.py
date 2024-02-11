from django.contrib import admin
from .models import AdvertisingCompany


@admin.register(AdvertisingCompany)
class AdvertisingCompanyAdmin(admin.ModelAdmin):
    list_display = "name", "product", "channel", "budget"
    list_display_links = "name", "channel", "budget"
