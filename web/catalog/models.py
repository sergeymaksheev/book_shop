from collections import UserString
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.db import models

import uuid # Required for unique book instances

from users.models import CustomUser
# Create your models here.

class Book(models.Model):
    """This class representing a book(but not a specific copy of book)"""
    title = models.CharField('Title', max_length=150)
    author = models.ManyToManyField('Author')
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=17)
    genre = models.ManyToManyField('Genre', help_text="Select a genre for this book")
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    number_of_pages = models.IntegerField(help_text="Number_of_pages")
    price = models.IntegerField(help_text="Write your price here")
    quantity = models.IntegerField(help_text="Number of books in the store")
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    """This is class representing an authors"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

class Genre(models.Model):
    """This class representing a book genre (e.g. Science Fiction, Non Fiction)"""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Publisher(models.Model):
    """This class representing a book genre (e.g. Science Fiction, Non Fiction)"""
    name = models.CharField(max_length=200, help_text="Enter a publisher's name")
    phone = models.CharField(max_length=30, help_text="Publisher's phone")
    email = models.EmailField(help_text="Publisher's email")
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class City(models.Model):
    """This class representing """
    name = models.CharField(max_length=200, help_text="Enter a city")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Orders_detail(models.Model):
    """This class representing your order detail"""
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null=True)
    amount = models.IntegerField(help_text='Amount of books in order')
    price = models.IntegerField(help_text="Write your price here")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Orders(models.Model):
    """This class representing orders"""


