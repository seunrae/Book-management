from django.contrib import admin
from .models import TodoItem, User, Book, Catalouge
# Register your models here.
admin.site.register(TodoItem)
# admin.site.register(User)
# admin.site.register(Book)
# admin.site.register(Catalouge)

class BookInLine(admin.TabularInline):
    model = Book
    fields = ('id', 'name','publisher', 'category', 'isBorrowed',)
    extra = 0

@admin.register(Catalouge)
class CatalougeAdmin(admin.ModelAdmin):
    model = Book
    if Book.isBorrowed:
        list_display = ('book',)
    

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name',)
    inlines = [BookInLine]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'publisher', 'category', 'isBorrowed', 'borrowed_to', 'available')
    search_fields = ('name', 'publisher', 'category', 'borrowed_to__first_name',)
    list_filter = ('publisher', 'isBorrowed')
        
    # autocomplete_fields = ['borrowed_to']