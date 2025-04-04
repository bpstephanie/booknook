from django import forms
from .models import NewsletterSignup


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['name', 'email']
