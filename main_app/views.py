from django.shortcuts import render
from django.http import HttpResponse

# Faux Cat Data - Database simulation
class Book:
    def __init__(self, name, author, description, price):
        self.name = name
        self.author = author
        self.description = description
        self.price = price

    # Book objects that are being instantiated from the Book class.
books = [
    Book('Rich Dad Poor Dad', 'Robert T. Kiyosaki', ' What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!', 7),
    Book('Think and Grow Rich', 'Napoleon Hill', '"Think and Grow Rich" is a motivational personal development and self-help book written by Napoleon Hill and inspired by a suggestion from Scottish-American businessman Andrew Carnegie."', 15),
    Book('The Alchemist', 'Paulo Coelho', 'A Fable About Following Your Dream', 14),
]




# Create your views here.

# This is equivalent to our controller /routes (in express js)

def home(request):
    return HttpResponse('<h1>Hello Mundão 📚📚📚</h1>')

def about(request):
    # If you want t osend back raw txt or an html string use HttpResponse
    # return HttpResponse('About Page')

    # If you want to send back a template file instead use "render"
    # Django will look into the folder called templates and return the specific file.
    return render(request, 'about.html')

def books_index(request):
    return render(request, 'books/index.html', {'books': books})