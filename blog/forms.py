from django import forms
from .models import Blog, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'slug', 'body', 'category')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'slug')
