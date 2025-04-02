from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    ROLE_CHOICES = [
        ("driver", "Driver"),
        ("tout", "Tout"),
    ]

    # Add the role field to the login form
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
