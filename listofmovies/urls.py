from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('listofmovies', views.list_of_movies, name='listofmovies'),
    path('listofmovies/<int:movie_id>/', views.movie_details, name='moviedetails'),
]
