from django import forms
from .models import Book, Accessory, Genre, Category, Review, ReviewComment


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'name', 'friendly_name', 'author', 'description', 'price',
            'rating', 'image', 'img_url', 'isbn'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'] = forms.ModelChoiceField(
            queryset=Genre.objects.all(),
            empty_label="Select Genre",
            widget=forms.Select(attrs={'class': 'border-navy rounded-0'})
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-navy rounded-0'


class AccessoryForm(forms.ModelForm):

    class Meta:
        model = Accessory
        fields = [
            'name', 'friendly_name', 'description', 'price',
            'rating', 'image', 'img_url', 'sku'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'] = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            empty_label="Select Category",
            widget=forms.Select(attrs={'class': 'border-navy rounded-0'})
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-navy rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the review title',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your review here',
                'rows': 5,
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Rate from 1 to 5',
            }),
        }
        labels = {
            'title': 'Review Title',
            'body': 'Your Review',
            'rating': 'Rating (1-5)',
        }


class ReviewCommentForm(forms.ModelForm):
    class Meta:
        model = ReviewComment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Add your comment here',
                'rows': 3,
            }),
        }
        labels = {
            'body': 'Comment',
        }
