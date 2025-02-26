from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify
import uuid


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    img_url = models.URLField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        # Automatically set content_type and object_id
        if not self.slug:
            self.slug = original_slug = slugify(self.name)
        for i in range(1, 1000):
            if not Product.objects.filter(slug=self.slug).exists():
                break
            self.slug = f'{original_slug}-{i}'
        if not self.content_type:
            self.content_type = ContentType.objects.get_for_model(self)
        self.object_id = self.pk

        # Set default meta_title and meta_description if not provided
        if not self.meta_title:
            self.meta_title = f'{self.name} - Buy Now at BookNook'
        if not self.meta_description:
            self.meta_description = f'{self.description[:150]}...'

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)  # Explicit id field
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)
    parent_genre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subgenres')

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name


class Book(Product):
    book_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre, null=True, blank=True, on_delete=models.SET_NULL
    )
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    category_id = models.AutoField(primary_key=True)  # Explicit id field
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcategories')

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name


class Accessory(Product):

    class Meta:
        verbose_name_plural = 'Accessories'

    accessories_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=100)

    def __str__(self):
        return self.name
