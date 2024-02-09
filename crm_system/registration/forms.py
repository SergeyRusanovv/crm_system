from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "email",
        )
        labels = {
            "email" : "E-mail",
            "first_name": "Имя",
            "last_name": "Фамилия"
        }
        widgets = {
            "email": forms.TextInput(),
            "first_name": forms.TextInput(),
            "last_name": forms.TextInput()
        }
