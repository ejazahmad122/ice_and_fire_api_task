from django.urls import path
from .views import ice_and_fire_api, IceAndFireApi, IceAndFireApiDetail

urlpatterns = [
    
    path('v1/books/', IceAndFireApi.as_view()),
    path('v1/books/<int:pk>/', IceAndFireApiDetail.as_view()),
    path('external-books/<str:name_of_book>/', ice_and_fire_api, name='iceandfireapi'),
]