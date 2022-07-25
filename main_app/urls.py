from django.urls import URLPattern, path
from . import views

# all site routes /URLS go below
urlpatterns = [
    # ('route', controller, nickname)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='books'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    # new route used to show a form and create a book
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),

    path('books/<int:book_id>/add_feedback/', views.add_feedback, name='add_feedback'),

    path('stores/', views.StoreList.as_view(), name='stores_index'),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
]

