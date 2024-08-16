# book_review/urls.py
from django.urls import path
from . import views

app_name = 'book_review'

urlpatterns = [
    path('', views.index, name='index'),
  
]
