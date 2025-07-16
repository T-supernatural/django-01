from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookFormModel

# Create your views here.
def home_view(request):
    book = Book.objects.all
    context = {
        'book': book
    }
    return render(request, 'home.html', context)

# details of book
def details_home(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'details.html', {"book":book})

# update of book
def update_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        # If the user submitted the form (POST), Django builds a form with
        form = BookFormModel(request.POST, request.FILES, instance=book)
# request.POST (text data),
# request.FILES (for uploaded image),
# instance=book (we are updating this exact book).

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookFormModel(instance=book)
        context = {
            'book': book,
            'form': form
        }
        return render(request, 'update.html', context)