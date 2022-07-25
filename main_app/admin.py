from django.contrib import admin
from .models import Book, Feedback

# Register your models here.

admin.site.register(Book)
admin.site.register(Feedback)