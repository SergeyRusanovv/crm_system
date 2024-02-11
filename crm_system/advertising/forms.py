from django import forms
from .models import AdvertisingCompany


class AdsForm(forms.ModelForm):
    class Meta:
        model = AdvertisingCompany
        fields = "name", "product", "channel", "budget"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Введите название рекламы",
                    "required": True,
                }
            ),
            "channel": forms.TextInput(
                attrs={
                    "placeholder": "Описание",
                    "required": True,
                }
            ),
        }
