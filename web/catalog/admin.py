from django.contrib import admin
from .models import Author, Genre, Book, Publisher, Orders_detail, Orders, City

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(City)
admin.site.register(Orders)
admin.site.register(Orders_detail)
