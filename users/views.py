from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from .models import User, EmailVerification
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    template_name = "users/register.html"
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("users:message")


class UserLoginView(LoginView):
    template_name = "users/my-login.html"
    model = User
    form_class = LoginForm
    success_url = reverse_lazy("store:index")


class EmailVerificatinMessageView(TemplateView):
    template_name = "users/email-verification-sent.html"


class EmailVerificatedView(TemplateView):
    template_name = "users/email-verification.html"

    def get(self, request, *args, **kwargs):
        code = kwargs.get("code")
        email = kwargs.get("email")
        user = User.objects.get(email=email)
        email_object = EmailVerification.objects.get(user=user)
        return render(
            request,
            "users/email-verification.html",
            {"email_object": email_object, "email_user": user},
        )


class EmailSuccessView(TemplateView):
    template_name = "users/email-verification-success.html"

    def get(self, request, *args, **kwargs):
        email = kwargs.get("email")
        user = User.objects.get(email=email)
        user.is_verificated = True
        user.save()
        return render(request, "users/email-verification-success.html")


class EmailFailedView(TemplateView):
    template_name = "users/email-verification-failed.html"
