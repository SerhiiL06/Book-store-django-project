from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Cart
from store.models import Book


class CartSummaryView(View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        return render(request, "cart/cart-summary.html", {"cart": cart})

    def post(self, request, book_id):
        cart = Cart.objects.get(book=book_id, user=request.user)
        cart.quantity = int(request.POST.get("quantity"))
        cart.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])


def cart_summary(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, "cart/cart-summary.html", {"cart": cart})


def add_to_cart(request, book_id, **kwargs):
    book = Book.objects.get(id=book_id)
    quantity = int(request.POST.get("quantity", 0))
    user = request.user
    cart_object = Cart.objects.filter(book=book, user=user)
    if cart_object.exists():
        cart = Cart.objects.get(book=book, user=user)
        cart.quantity += quantity
        cart.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        Cart.objects.create(book=book, user=user)
        return HttpResponseRedirect(request.META["HTTP_REFERER"])


def delete_from_cart(request, book_id):
    cart_object = Cart.objects.get(book=book_id, user=request.user)
    cart_object.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
