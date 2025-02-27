from django.urls import reverse

from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre (e.g Fiction, Comic)"
    )

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message="Genre already exists (case insensitive match)"
            )
        ]


class Book(models.Model):
    """Model representing the information of the book (not an instance)"""
    tilte = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of this book"
    )
    isbn = models.CharField(
        'ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn')

    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        return self.tilte
    
    def get_absolute_url():
        return reverse('book-detail', args=[str(self.id)])