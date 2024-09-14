from django.test import TestCase
from django.urls import reverse
from .models import User, Book, Catalouge
from datetime import date, timedelta
from .forms import BookForm
# Create your tests here.

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="john", last_name="doe", email="john.doe@gmail.com")
    
    def test_user_registration(self):
        self.assertEqual(self.user.first_name, "john")
        self.assertEqual(self.user.last_name, "doe")
        self.assertEqual(self.user.email, "john.doe@gmail.com")

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(name="JJK", publisher="gege akutami", category="horror")

    def test_book_registration(self):
        self.assertEqual(self.book.name, "JJK")
        self.assertEqual(self.book.publisher, "gege akutami")
        self.assertEqual(self.book.category, "horror")

class CatalougeModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(name="JJK", publisher="gege akutami", category="horror")
        self.catalouge = Catalouge.objects.create(book=self.book)

    def test_add_book_to_catalouge(self):
        self.assertEqual(self.book, self.catalouge.book)


class bookViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="john", last_name="doe", email="john.doe@gmail.com")
        self.book = Book.objects.create(name="JJK", publisher="gege akutami", category="horror")
    
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'gege akutami')

    def test_borrow_book(self):
        self.book.isBorrowed = True
        self.book.borrowed_to = self.user
        self.book.borrow_duration = 3
        self.book.available = date.today() + timedelta(days=self.book.borrow_duration)
        self.book.save()
        response = self.client.post(reverse('borrow_book_by_id', args=[self.book.id]))
        self.book.refresh_from_db()
        self.assertTrue(self.book.isBorrowed)
        self.assertEqual(self.book.borrowed_to, self.user)

class BookFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="john", last_name="doe", email="john.doe@gmail.com")
    def test_valid_form(self):
        form_data = {'name': 'Dragon ball', 'publisher': 'akira toriyama', 'category': 'fantasy', 'borrow_duration': 7, 'borrowed_to': self.user}
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())
