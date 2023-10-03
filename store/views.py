from typing import Any


from .models import Book, Category
from django.views.generic import ListView, DetailView, View

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class StoreIndexView(ListView):
    model = Book
    template_name = "store/store.html"

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        category_slug = self.kwargs.get("category_slug")
        print(category_slug)
        return (
            queryset.filter(category__slug=category_slug) if category_slug else queryset
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get("category_slug")
        context["fav_list"] = self.request.session.get("fav_list")
        if category_slug:
            context["categor"] = Category.objects.get(slug=category_slug)
        return context


class BookDetailView(DetailView):
    template_name = "store/product-info.html"
    model = Book


def add_to_fav(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    fav_list = request.session.get("fav_list")

    if not fav_list:
        request["fav_list"] = list()

    request.session["fav_list"].append(book_id)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def add_to_fav(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    fav_list = request.session.get("fav_list", [])

    if book_id not in fav_list:
        fav_list.append(book_id)
    else:
        fav_list.remove(book_id)

    request.session["fav_list"] = fav_list

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def delete_favorite_list(request):
    fav_list = request.session.get("fav_list")
    fav_list.clear()
    request.session["fav_list"] = fav_list

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


class FavorireListView(View):
    def get(self, request):
        fav_list = request.session.get("fav_list", [])
        fav_books = Book.objects.filter(id__in=fav_list)

        return render(request, "store/favorite-list.html", {"fav_list": fav_books})
