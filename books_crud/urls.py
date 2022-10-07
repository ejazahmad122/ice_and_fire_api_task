from django.urls import path
from .views import ice_and_fire_api

urlpatterns = [
    path('external-books/<str:name_of_book>/',
         ice_and_fire_api, name='iceandfireapi'),
]
