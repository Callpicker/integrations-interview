from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Reader

admin.site.register(Book)
admin.site.register(Reader)