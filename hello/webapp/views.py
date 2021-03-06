from django.shortcuts import render

from webapp.models import Guestbook, status_choices
from webapp.form import BookForm

# Create your views here.

def list_book_view(request):
    books = Guestbook.objects.all().filter(status="active").order_by('-time_of_creation')
    return render(request, 'list_book.html', context={'books': books})

def book_view(request, pk):
    book = Guestbook.objects.get(id=pk)
    return render(request, 'book_view.html', context={'book': book})

# def add_book(request):
#     if request.method == 'GET':
#         form = BookForm()
#         return render(request, 'create_product.html', {'category': categories, 'form': form})
#     elif request.method == "POST":
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product = Product.objects.create(
#                 name=form.cleaned_data.get("name"),
#                 description=form.cleaned_data.get("description"),
#                 category=form.cleaned_data.get("category"),
#                 remainder=form.cleaned_data.get("remainder"),
#                 price=form.cleaned_data.get("price")
#             )
#             return redirect('view-product', pk=product.id)
#         return render(request, 'create_product.html', context={'form': form})