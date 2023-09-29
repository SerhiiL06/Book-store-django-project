from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MaxValueValidator


class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(default="", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    name = models.CharField(max_length=150, unique=True)
    discription = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(default="", unique=True)
    rating = models.PositiveSmallIntegerField(
        default=0,
        validators=[MaxValueValidator(5, "Please choose the rating beetween 1 and 5.")],
    )
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    update_in = models.DateTimeField(auto_now=True, editable=False)
    image = models.ImageField(upload_to="book_image/", blank=True)
    code = models.IntegerField(validators=[MaxValueValidator(9999)], default=0000)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self) -> str:
        return f"{self.name} | Category ({self.category.title})"

    def get_absolute_url(self, *args):
        return reverse("store:detail", args=[self.slug])

    class Meta:
        ordering = ["-date_created"]
