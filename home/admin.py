from django.contrib import admin
from .models import NewsletterSignup


# Register your models here.
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_signed_up')
    search_fields = ('name', 'email')
    list_filter = ('date_signed_up')


admin.site.register(NewsletterSignup)
