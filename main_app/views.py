from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This is equivalent to our controller /routes (in express js)

def home(request):
    return HttpResponse('<h1>Hello Mundão 📚📚📚</h1>')

