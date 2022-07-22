from django.urls import URLPattern, path
from . import views

# all site routes /URLS go below
urlpatterns = [
    # ('route', controller, nickname)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='books'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
]

