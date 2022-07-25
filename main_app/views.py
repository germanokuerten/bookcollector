from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Store
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedbackForm

# Faux Cat Data - Database simulation
# class Book:
#     def __init__(self, name, author, description, price):
#         self.name = name
#         self.author = author
#         self.description = description
#         self.price = price

#     # Book objects that are being instantiated from the Book class.
# books = [
#     Book('Rich Dad Poor Dad', 'Robert T. Kiyosaki', ' What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!', 7),
#     Book('Think and Grow Rich', 'Napoleon Hill', '"Think and Grow Rich" is a motivational personal development and self-help book written by Napoleon Hill and inspired by a suggestion from Scottish-American businessman Andrew Carnegie."', 15),
#     Book('The Alchemist', 'Paulo Coelho', 'A Fable About Following Your Dream', 14),
# ]




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
    # books = Book.objects.all()
    # use code below if you want to order by id
    books = Book.objects.order_by('id')
    return render(request, 'books/index.html', {'books': books})

def books_detail(request, book_id):
    # Get the individual book
    book = Book.objects.get(id=book_id)

    # Instantiate our feeding form
    feedback_form = FeedbackForm()
    # Render template, pass it the book
    return render(request, 'books/detail.html', {'book': book, 'feedback_form': feedback_form })

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['name', 'author', 'description', 'price']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'




def add_feedback(request, book_id):
	# create the ModelForm using the data in request.POST
  form = FeedbackForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feedback = form.save(commit=False)
    new_feedback.book_id = book_id
    new_feedback.save()
  return redirect('detail', book_id=book_id)



class StoreList(ListView):
  model = Store

class StoreDetail(DetailView):
  model = Store

class StoreCreate(CreateView):
  model = Store
  fields = '__all__'

class StoreUpdate(UpdateView):
  model = Store
  fields = ['name']

class StoreDelete(DeleteView):
  model = Store
  success_url = '/stores/'