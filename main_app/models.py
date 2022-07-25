from django.db import models
from django.urls import reverse
from datetime import date

#select options for feeding types in Feeding Model
SCORES = (
    ('G', 'Great'),
    ('O', 'Okay'),
    ('T', 'Terrible'),
)

# Django built a parent class called models that has a bunch of functionality built in.

class Store(models.Model):
    name = models.CharField(max_length=50)
    # color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store_detail', kwargs={'pk': self.id})

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

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Feedback(models.Model):
    # This title 'Feedback Date' will be seen by the user in the forms.
    date = models.DateField('Feedback Date')
    score = models.CharField('Score Here',
        max_length=1,
        # add the 'choices' field option
        choices=SCORES,
        # set the default value for meal to be 'B'
        default=SCORES[0][0]
  )

    # This is where the relationship is defined (one to many in this case)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_score_display()} on {self.date}' 

    # class Meta:
    #     ordering = ['-date']
