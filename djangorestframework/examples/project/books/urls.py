
from django.contrib import admin
from django.urls import path
from .views import book_list, BookList

urlpatterns = [
    path('fbv/', book_list),
    path('cbv/', BookList.as_view()),
]
