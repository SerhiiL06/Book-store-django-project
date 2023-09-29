from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("email-message/", views.EmailVerificatinMessageView.as_view(), name="message"),
    path(
        "emailverif/<str:email>/<uuid:code>/",
        views.EmailVerificatedView.as_view(),
        name="verification",
    ),
    path(
        "message-success/<str:email>/",
        views.EmailSuccessView.as_view(),
        name="success-message",
    ),
    path("failed-message/", views.EmailFailedView.as_view(), name="failed-message"),
]
