from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "cart"

urlpatterns = [
    path("", login_required(views.CartSummaryView.as_view()), name="cart-summary"),
    path("cart-add/<int:book_id>/", views.add_to_cart, name="add-cart"),
    path("cart-delete/<int:book_id>/", views.delete_from_cart, name="delete-cart"),
    path("cart/update/<int:book_id>/", views.CartSummaryView.as_view(), name="update"),
]
