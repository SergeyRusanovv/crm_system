from django.contrib import admin
from .models import ActiveLead


@admin.register(ActiveLead)
class ActiveLead(admin.ModelAdmin):
    list_display = "lead", "contract"
    list_display_links = "lead", "contract"
