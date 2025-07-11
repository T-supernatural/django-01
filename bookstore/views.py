from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

# Create your views here.
def home_view(request):
    book = Book.objects.all
    context = {
        'book': book
    }
    return render(request, 'home.html', context)