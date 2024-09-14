from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_user, name="create_user"),
    path("users/", views.user_list, name="user_list"),
    path("books/", views.book_list, name="book_list"),
    path("book/<int:id>", views.get_book, name="get_book"),
    path("books/publisher/<str:publisher>", views.filter_book_by_publisher, name="filter_book_by_publisher"),
    path("books/category/<str:category>", views.filter_book_by_category, name="filter_book_by_category"),
    path("borrow_book/<int:book_id>", views.borrow_book_by_id, name="borrow_book_by_id"),
    path("/error", views.book_list,name="error")
]