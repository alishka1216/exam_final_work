from django import forms
from django.core.validators import MinValueValidator, ValidationError
from webapp.models import Category, Review, Product


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['description_review']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category' ]


class UserForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author']


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')