from django.urls import path, include
from . import views
urlpatterns = [
    path('view/', views.kidsbook_list, name='kidsbook_list_home'),
    path('view/<id>/', views.kidsbook_detail, name='kidsbook_detail'),
]
