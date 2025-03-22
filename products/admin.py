from django.contrib import admin
from .models import Product, Genre, Category, Book, Accessory, Review


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'friendly_name',
            'price',
            'rating',
            'created_at',
            'updated_at'
        )
    prepopulated_fields = {'slug': ('name',)}


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
    prepopulated_fields = {'slug': ('name',)}

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
    prepopulated_fields = {'slug': ('name',)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'product',
        'approved',
    )

    ordering = ('product', 'approved',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Review, ReviewAdmin)
