from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse_lazy
from advertising.models import AdvertisingCompany


class Leads(models.Model):
    """Потенциальный клиент"""
    regex_phone = RegexValidator(
        regex=r"^((8|\+7|)(\d{10}))$", message="Формат номера телефона должен быть: +79999999999 или 89999999999"
    )

    class Meta:
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"

    first_name = models.CharField(max_length=20, verbose_name="Фамилия и имя")
    last_name = models.CharField(max_length=50, verbose_name="Отчество (при наличии)", blank=True, null=True)
    phone = models.CharField(max_length=12, validators=[regex_phone], verbose_name="Номер телефона", unique=True)
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    advertising = models.ForeignKey(AdvertisingCompany, on_delete=models.CASCADE, related_name="leads", verbose_name="Рекламная компания")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("leads:lead-detail", kwargs={"pk": self.pk})
