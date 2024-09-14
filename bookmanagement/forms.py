from django import forms
from .models import User, Book

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'publisher', 'category', 'borrow_duration', 'borrowed_to']
