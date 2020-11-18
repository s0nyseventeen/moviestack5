from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('genres/', views.genre_list, name='genrelist'),
    path('genres/<int:genre_id>/', views.genre_detail, name='genre_detail'),
]
