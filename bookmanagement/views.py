from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem, User, Book
from .forms import UserForm, BookForm
from datetime import date, timedelta
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, "home.html");

def create_user(request):
    form = UserForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect("user_list")
    return render(request, "user_form.html", {"form": form})

def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users":users})


def book_list(request):
    books = Book.objects.all()
    if books.exists():
        return render(request, "book_list.html", {"books": books})
    else:
        return HttpResponse("No books available")

def get_book(request, id):
    book = Book.objects.get(id=id)
    if book:
        return render(request, "book.html", {"book":book})
    else:
        return HttpResponse("Book does not exist ")

def filter_book_by_publisher(request, publisher):
    books = Book.objects.filter(publisher=publisher)
    if books.exists():
        return render(request, "book_list.html", {"books" : books})
    else:
        return HttpResponse("No books available")
    
def filter_book_by_category(request, category):
    books = Book.objects.filter(category=category)
    if books.exists():
        return render(request, "book_list.html", {"books" : books})
    else:
        return HttpResponse("No books available")
    
def borrow_book_by_id(request, book_id):
    book = Book.objects.get(id=book_id)
    # user = User.objects.get(id=user_id)
    books = Book.objects.all()
    form = BookForm(request.POST or None, instance=book)
    if not book.isBorrowed:
        if request.method == "POST" and form.is_valid():
            book.isBorrowed = True
            user = form.cleaned_data.get('borrowed_to')
            book.borrowed_to = user
            borrow_duration = form.cleaned_data.get('borrow_duration')
            book.available = date.today() + timedelta(days=borrow_duration)
            form.save()
            return render(request, "book_list.html", {"books":books})
        return render(request, "book_form.html", {"form": form})
    return HttpResponse("Book borrowed")
