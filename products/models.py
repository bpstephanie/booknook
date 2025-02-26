from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    img_url = models.URLField(max_length=1000, null=True, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)  # Explicit id field
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name


class Book(Product):
    book_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre, null=True, blank=True, on_delete=models.SET_NULL
    )
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)  # Explicit id field
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name


class Accessory(Product):
    accessories_id = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=100)

    def __str__(self):
        return self.name
