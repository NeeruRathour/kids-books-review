from django.urls import path, include
from . import views

urlpatterns = [  
    path('view/', views.kidsbook_list, name='kidsbook_list_home'),
    path('view/<id>/', views.kidsbook_detail, name='kidsbook_detail'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('kidsbooks/<int:book_id>/rate/', views.rate_book, name='rate_book'),
    path('my-reviews/', views.my_reviews, name='my_reviews'),
    path('about-us/', views.about_us, name='about_us'),
]
