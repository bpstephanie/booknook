from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.apps import apps

from wishlist.models import Wishlist
from bag.models import SavedItem
from products.models import Book


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    my_wishlists = models.ManyToManyField(
        Wishlist, related_name='user_profiles', blank=True)
    my_saved_items = models.ManyToManyField(
        SavedItem, related_name='user_profiles', blank=True)
    favourite_books = models.ManyToManyField(
        Book, related_name='favourited_by', blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)

    def has_purchased(self, product):
        OrderLineItem = apps.get_model('checkout', 'OrderLineItem')
        return OrderLineItem.objects.filter(
            order__user_profile=self, product=product
        ).exists()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class PDF(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
