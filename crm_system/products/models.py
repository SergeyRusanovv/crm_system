from django.db import models
from django.urls import reverse_lazy


class Product(models.Model):
    """Продукты"""
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.CharField(max_length=252, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, max_length=10, verbose_name="Цена", decimal_places=3)

    def get_absolute_url(self):
        return reverse_lazy("products:product-detail", kwargs={"pk": self.pk})
