from audioop import add
from django.urls import path
from .views import show_all_books, add_book, delete_book, update_book, show_specific_book, ice_and_fire_api

urlpatterns = [
    path('v1/books/', show_all_books, name='showallbooks'),
    path('v1/books/add/', add_book, name='add'),
    path('v1/books/<int:id>/delete', delete_book, name='delete'),
    path('v1/books/<int:id>/update', update_book, name='update'),
    path('v1/books/<int:id>/', show_specific_book, name='showspecific'),
    path('external-books/<str:name_of_book>/', ice_and_fire_api, name='iceandfireapi'),
]