from django.db import models

# Django built a parent class called models that has a bunch of functionality built in.

# Book Model
# Name, author, description, price

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        # return self.name
        return f"{self.name} - {self.author}"