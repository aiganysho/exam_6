from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Guestbook, status_choices
from webapp.form import BookForm, BookDeleteForm

# Create your views here.

def list_book_view(request):
    books = Guestbook.objects.all().filter(status="active").order_by('-time_of_creation')
    return render(request, 'list_book.html', context={'books': books})

def book_view(request, pk):
    book = Guestbook.objects.get(id=pk)
    return render(request, 'book_view.html', context={'book': book})

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})
    elif request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            books = Guestbook.objects.create(
                author=form.cleaned_data.get("author"),
                email=form.cleaned_data.get("email"),
                text=form.cleaned_data.get("text")
            )
            return redirect('list-book')
        return render(request, 'add_book.html', context={'form': form})

def book_update_view(request):
    books = Guestbook.objects
    if request.method == 'GET':
        form = BookForm(
            initial={
                'author': books.author,
                'email': books.email,
                'text': books.text
            })
        return render(request, 'book_update.html', context={'form': form, 'books': books})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            books.author = form.cleaned_data.get("author")
            books.email = form.cleaned_data.get("email")
            books.text = form.cleaned_data.get("text")
            books.save()
            return redirect('list-book')
        return render(request, 'book_update.html', context={'form': form, 'books': books})

def book_delete_view(request):
    books = Guestbook.objects
    if request.method == "GET":
        return render(request, 'book_delete.html', context={'books': books})
    elif request.method == 'POST':
        books.delete()
        return redirect('list-book')