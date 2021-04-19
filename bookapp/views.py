from django.shortcuts import render
# Create your views here.
from .models import Book
def index(request):
    books = Book.objects
    return render(request, 'index.html', {'book1': books})

def about(request):
    return render(request, 'about.html')


