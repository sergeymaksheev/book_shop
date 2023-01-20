from django.db import models

# Create your models here.

class Book(models.Model):
    """This class representing a book(but not a specific copy of book)"""
    title = models.CharField('Title', max_length=150)
    author = models.ManyToManyField('Author')
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13)
    genre = models.ManyToManyField('Genre', help_text="Select a genre for this book")

class Author(models.Model):
    """This is class representing an authors"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

class Genre(models.Model):
    """This class representing a book genre (e.g. Science Fiction, Non Fiction)"""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")