from django.contrib import admin
from .models import Author, Genre, Book, Publisher, City, TheRestOfTheBook

# Register your models here.

admin.site.register(Book)
admin.site.register(TheRestOfTheBook)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(City)
