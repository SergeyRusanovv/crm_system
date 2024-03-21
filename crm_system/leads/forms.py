from django import forms
from .models import Leads


class LeadsForm(forms.ModelForm):

    class Meta:
        model = Leads
        fields = "first_name", "last_name", "phone", "advertising"
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Введите Фамилию и Имя",
                    "required": True,
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Введите Отчество (при наличии)",
                    "required": True,
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "+79000000000",
                    "required": True,
                }
            )
        }
