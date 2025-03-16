from django import forms
from .models import UserProfile
from products.models import Book


class DeliveryDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'bio', 'date_joined',
                   'my_wishlists', 'my_saved_items',
                   'favourite_books')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-navy rounded-0 profile-form')
            self.fields[field].label = False


class PersonalInfoForm(forms.ModelForm):
    favourite_books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'class': 'select2', 'multiple': 'multiple'}
        ),
        required=False
    )

    class Meta:
        model = UserProfile
        exclude = ('user', 'date_joined',
                   'my_wishlists', 'my_saved_items',
                   'default_phone_number', 'default_country',
                   'default_postcode', 'default_town_or_city',
                   'default_street_address1', 'default_street_address2',
                   'default_county')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'bio': 'Biography',
            'favourite_books': 'Favourite Books',
        }

        self.fields['bio'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = (
            'border-navy rounded-0 profile-form')
        self.fields[field].label = False
