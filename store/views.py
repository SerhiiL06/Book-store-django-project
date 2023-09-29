from typing import Any

from django.db.models.query import QuerySet
from .models import Book, Category
from django.views.generic import ListView, TemplateView, DetailView


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
        if category_slug:
            context["categor"] = Category.objects.get(slug=category_slug)
        return context


class BookDetailView(DetailView):
    template_name = "store/product-info.html"
    model = Book
