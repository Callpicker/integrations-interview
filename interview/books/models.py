from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100) 
    isbn = models.CharField(max_length=100)

class Reader(models.Model):
    username = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)