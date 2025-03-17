from django.contrib import admin
from .models import Category, Thread, Post


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'category', 'created_at')
    search_fields = ('title', 'created_by__username')
    list_filter = ('category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'created_by', 'created_at')
    search_fields = ('thread__title', 'created_by__username')
    list_filter = ('created_at',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
