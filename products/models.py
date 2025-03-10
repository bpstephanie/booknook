from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)
import uuid


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        help_text="Price should be between £0.00 and £999.99"
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    img_url = models.URLField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
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
            self.meta_title = f'{self.friendly_name} - Buy Now at BookNook'
        if not self.meta_description:
            self.meta_description = (
                f'{self.description[:147]}...'
                if len(self.description) > 150
                else (
                    self.description
                )
            )

        super(Product, self).save(*args, **kwargs)

    def is_book(self):
        return isinstance(self, Book)

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name

    class Meta:
        ordering = ['name']


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)  # Explicit id field
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)
    parent_genre = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='subgenres'
    )

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name

    class Meta:
        ordering = ['name']


class Book(Product):
    book_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    author = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre, null=True, blank=True, on_delete=models.SET_NULL
    )
    isbn = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\d{10}(\d{3})?$',
                message="ISBN must be either 10 or 13 digits long"
            )
        ]
    )

    def __str__(self):
        return f"{self.friendly_name or self.name} by {self.author}"

    class Meta:
        ordering = ['name']


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)  # Explicit id field
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)
    parent_category = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='subcategories'
    )

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Accessory(Product):
    accessories_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Accessories'
        ordering = ['name']


class Review(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name="reviews"
    )
    body = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating should be between 1 and 5"
    )
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.title} by {self.author.username} - "
            f"Rating: {self.rating}"
        )

    class Meta:
        ordering = ['-created_on']


class ReviewComment(models.Model):
    review = models.ForeignKey(
        'Review', on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username}"

    class Meta:
        ordering = ['created_on']
