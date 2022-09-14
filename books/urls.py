from email.mime import base
from django.contrib import admin
from django.urls import path, include
from books_crud import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('api/v1/books', views.IceAndFireApi, basename='iceandfire')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include(router.urls)),
    path('api/', include('books_crud.urls')),
    
    path('user/', include('account.urls'))
]
