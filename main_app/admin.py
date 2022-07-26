from django.contrib import admin
from .models import Book, Feedback, Store, Photo

# Register your models here.

admin.site.register(Book)
admin.site.register(Feedback)
admin.site.register(Store)
admin.site.register(Photo)