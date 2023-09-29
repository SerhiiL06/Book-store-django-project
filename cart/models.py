from django.db import models
from django.core.validators import MaxValueValidator
from store.models import Book
from users.models import User


class CartQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_qty(self):
        return sum(basket.quantity for basket in self)


class Cart(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="cart_book"
    )
    quantity = models.SmallIntegerField(default=1, validators=[MaxValueValidator(100)])

    objects = CartQuerySet.as_manager()

    def sum(self):
        return self.quantity * self.book.price
