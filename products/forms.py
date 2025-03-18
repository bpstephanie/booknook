from django import forms
from .models import Book, Accessory, Genre, Category, Review, ReviewComment


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for g in genres]

        self.fields['genre'].choices = friendly_names
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
