from django.db import models
from django.urls import reverse_lazy
from leads.models import Leads
from contracts.models import Contract


class ActiveLead(models.Model):
    """Активные клиенты"""
    class Meta:
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"

    lead = models.ForeignKey(to=Leads, on_delete=models.CASCADE, verbose_name="Клиент", related_name="active_lead")
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, verbose_name="Контракт", related_name="active_lead")

    def get_absolute_url(self):
        return reverse_lazy("customers:customer-detail", kwargs={"pk": self.pk})
