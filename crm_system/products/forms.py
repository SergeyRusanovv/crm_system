from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Введите название продукта",
                    "required": True,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Описание",
                    "required": True,
                    "rows": 5,
                    "cols": 25,
                }
            ),
        }
        fields = "name", "description", "price"
