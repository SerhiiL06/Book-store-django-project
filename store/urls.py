from django.urls import path
from . import views


app_name = "store"

urlpatterns = [
    path("", views.StoreIndexView.as_view(), name="index"),
    path("book/<slug:slug>/", views.BookDetailView.as_view(), name="detail"),
    path(
        "category/<slug:category_slug>/",
        views.StoreIndexView.as_view(),
        name="category",
    ),
]
