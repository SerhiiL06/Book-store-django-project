from django.db import models
from django.urls import reverse
from .managers import CustomUserManager
from base import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.core.mail import send_mail

from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    GENDES = (
        ("M", "Man"),
        ("W", "Woman"),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    is_verificated = models.BooleanField(default=False)
    image = models.ImageField(upload_to="user_image/", blank=True, null=True)
    gender = models.CharField(choices=GENDES, max_length=1, blank=True, null=True)

    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def is_auntheticated(self):
        return True

    def __str__(self):
        return self.email


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    valid_period = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def sending_mail(self, **kwargs):
        link = reverse(
            "users:verification", kwargs={"email": self.user.email, "code": self.code}
        )
        record = f"{settings.DOMAIN_NAME}{link}"
        subject = f"Email Verificatedd for {self.user.first_name}"
        message = f"If you want to verificated your mail please click {record}"
        send_mail(
            subject=subject,
            message=message,
            from_email="book-store@gmail.com",
            recipient_list=[self.user.email],
            fail_silently=True,
        )

    def is_valid(self):
        return timezone.now().date() < self.valid_period.date()
