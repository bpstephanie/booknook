from django.contrib import admin
from .models import Wishlist, WishlistItem


# Register your models here.
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
            'user_username',
            'name',
            'item_count',
        )

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = "Username"

    def item_count(self, obj):
        return obj.wishlist_items.count()
    item_count.short_description = "Number of Items"


admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(WishlistItem)
