from django.contrib import admin
from .models import Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    fields = ["title", "slug"]
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    prepopulated_fields = {"slug": ["name"]}
