from django.db import models
from django.urls import reverse_lazy
from products.models import Product


class AdvertisingCompany(models.Model):
    """Рекламная компания"""
    class Meta:
        verbose_name = "Рекламная компания"
        verbose_name_plural = "Рекламные компании"

    name = models.CharField(max_length=50, verbose_name="Название")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт", related_name="advertisings")
    channel = models.CharField(max_length=50, verbose_name="Канал продвижения")
    budget = models.DecimalField(max_length=10, max_digits=10, decimal_places=3, verbose_name="Бюджет на рекламу")

    def get_absolute_url(self):
        return reverse_lazy("advertising:ads-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"
