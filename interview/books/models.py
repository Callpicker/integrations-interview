from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100) 
    isbn = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Reader(models.Model):
    username = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.username