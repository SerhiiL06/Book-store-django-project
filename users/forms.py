from uuid import uuid4
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User, EmailVerification


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(max_length=30, label="First Name", required=True)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True)
    gender = forms.ChoiceField(choices=User.GENDES, label="Gender", required=False)

    class Meta:
        model = User
        fields = [
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "gender",
        ]

    def save(self, commit=True):
        user = super().save(commit=True)
        period = timezone.now() + timedelta(hours=72)
        email_object = EmailVerification.objects.create(
            user=user, valid_period=period, code=uuid4()
        )
        email_object.sending_mail()
        return user


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["email", "password"]
