from django import forms
from .models import Thread, Category, Post


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
