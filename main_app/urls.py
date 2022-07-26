from django.urls import URLPattern, path
from . import views

# all site routes /URLS go below. Specifies endpoints
urlpatterns = [
    # ('route', controller, nickname)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='books'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    # new route used to show a form and create a book
    path('books/create/', views.BookCreate.as_view(), name='books_create'),

    # int:pk I believe is for class based views. B/c we are using the Django rules for class based views.
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),

    path('books/<int:book_id>/add_feedback/', views.add_feedback, name='add_feedback'),

    # <int:book_id> this means that in our controller/view function we will have access to book_id as an argument (since we are the ones writing the function differently than class based views). 
    # 'books/<int:book_id>/add_photos/', this is the end point
    # views.add_photo, the view function responsible to handing the endpoint
    # name='add_photo', name property that we can use when we want to access this via a form.
    path('books/<int:book_id>/add_photos/', views.add_photo, name='add_photo'),


    path('books/<int:book_id>/assoc_store/<int:store_id>/', views.assoc_store, name='assoc_store'),

    path('stores/', views.StoreList.as_view(), name='stores_index'),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
]

