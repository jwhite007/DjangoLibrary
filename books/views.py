from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from books.models import Books


def index(request):
    entries = Books.objects.all().order_by('author_lastname', 'title')[:]
    return render_to_response('books/index.html', {'Books': entries})


def CheckoutBook(request, pk):
    try:
        book = get_object_or_404(Books, pk=pk)
    except:
        return index(request)

    book.in_stock = False
    book.save()
    return render(request, 'books/checkout_book.html', {'book': book})


def CheckinBook(request, pk):
    try:
        book = get_object_or_404(Books, pk=pk)
    except:
        return index(request)

    book.in_stock = True
    book.save()
    return render(request, 'books/checkin_book.html', {'book': book})
