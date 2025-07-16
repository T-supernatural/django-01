from django import forms
from .models import Book

class BookFormModel(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "price", "cover"]