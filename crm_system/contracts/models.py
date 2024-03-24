from django.db import models
from django.urls import reverse_lazy
from products.models import Product


class Contract(models.Model):
    """Контракты"""
    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"

    name = models.CharField(max_length=50, verbose_name="Название контракта")
    product = models.ForeignKey(
        to=Product, related_name="contracts",
        on_delete=models.CASCADE,
        verbose_name="Предоставляемая услуга"
    )
    document = models.FileField(upload_to="contracts/documents", verbose_name="Документ")
    date_signed = models.DateField(verbose_name="Дата заключения")
    validity_period = models.DateField(verbose_name="Период окончания")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse_lazy("contracts:contract-detail", kwargs={"pk": self.pk})
