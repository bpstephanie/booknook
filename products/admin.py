from django.contrib import admin
from .models import Genre, Category, Book, Accessory


# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'parent_genre',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'parent_category',
    )

    ordering = ('name', 'parent_category')


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'isbn',
        'price',
        'rating',
        'image',
    )

    ordering = ('name', 'author', 'genre', )


class AccessoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'sku',
        'price',
        'rating',
        'image',
    )

    ordering = ('name', 'category', 'sku',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Accessory, AccessoryAdmin)
