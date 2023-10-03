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
    path("add_to_fav_list/<int:book_id>/", views.add_to_fav, name="add"),
    path("favorite_list/", views.FavorireListView.as_view(), name="favorite"),
    path("favorite_list/delete/", views.delete_favorite_list, name="delete-all"),
]
