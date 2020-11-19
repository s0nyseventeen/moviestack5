from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('listofmovies', views.list_of_movies, name='listofmovies'),
    path('listofmovies/<int:movie_id>/', views.movie_details, name='moviedetails'),
    path('genres/', views.list_of_genres, name='genres'),
    path('genres/<int:genre_id>/', views.genre_details, name='genredetails')
]
