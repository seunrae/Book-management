from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"id: {self.id} {self.first_name} {self.last_name}"

class Book(models.Model):
    BOOK_PUBLISHERS = (
        ("Wiley", "Wiley"),
        ("Apress", "Apress"),
        ("Manning", "Manning")
    )
    BOOK_CATEGORIES = (
        ("fiction", "fiction"),
        ("technology", "technology"),
        ("science", "science")
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    isBorrowed = models.BooleanField(default=False)
    borrowed_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="books")
    borrow_duration = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(7)])
    available = models.DateField(null=True, blank= True)

    def __str__(self):
        return f"id:{self.id} name:{self.name}, published by: {self.publisher}, category: {self.category}"
    
class Catalouge(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True, related_name="books")

    def __str__(self):
        return f""