from django.shortcuts import render
from django.http import HttpResponse

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

