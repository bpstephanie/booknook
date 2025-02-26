from django.contrib import admin
from .models import Genre, Category, Book, Accessory

# Register your models here.
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Accessory)