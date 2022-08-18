from pyexpat import model
from django.db import models

class Author(models.Model):
    author = models.CharField(max_length=200)

class BookShelf(models.Model):
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=14)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  #passing as a foreign key in Author table
    country = models.CharField(max_length=200)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=200)
    release_date = models.DateField()
