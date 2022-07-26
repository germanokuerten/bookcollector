from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Store, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedbackForm
# Aws stuff
# uuid gives us a globally unique string
import uuid 
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'book-collector-gk'

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
    # return HttpResponse('<h1>Hello Mundão 📚📚📚</h1>')
    return render(request, 'home.html')

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
    stores_book_not_available = Store.objects.exclude(id__in = book.stores.all().values_list('id'))

    # print(stores_book_not_available)
    # ps. in order to get the print, you must refresh the page, and it will show up at the terminal when server is running.

    # Instantiate our feeding form
    feedback_form = FeedbackForm()
    # Render template, pass it the book
    return render(request, 'books/detail.html', {'book': book, 'feedback_form': feedback_form, 'stores': stores_book_not_available })


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'description', 'price']
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

def add_photo(request, book_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, book_id=book_id)
            photo.save()
        except:
            print('An error occurred - S3')
    return redirect('detail', book_id=book_id)

def assoc_store(request, book_id, store_id):
    Book.objects.get(id=book_id).stores.add(store_id)
    return redirect('detail', book_id=book_id)


class StoreList(ListView):
  model = Store

class StoreDetail(DetailView):
  model = Store

class StoreCreate(CreateView):
  model = Store
  fields = '__all__'
  success_url = '/stores/'

class StoreUpdate(UpdateView):
  model = Store
  fields = ['name']

class StoreDelete(DeleteView):
  model = Store
  success_url = '/stores/'