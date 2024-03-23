from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = "name", "product", "document", "date_signed", "validity_period"
    list_display_links = "name", "document", "date_signed", "validity_period"
