from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Fare  # 👈 Add this import


class LoginForm(AuthenticationForm):
    ROLE_CHOICES = [
        ("driver", "Driver"),
        ("tout", "Tout"),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )


# ✅ Fare logging form for Touts
class FareForm(forms.ModelForm):
    class Meta:
        model = Fare
        fields = ["shift", "amount_collected"]
        widgets = {
            "shift": forms.Select(attrs={"class": "form-control"}),
            "amount_collected": forms.NumberInput(attrs={"class": "form-control"}),
        }
