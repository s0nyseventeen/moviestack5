from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Genre

def home(request):
    genres = Genre.objects.all()
    return render(request, 'listofmovies/homepage.html', {'genres': genres})

def list_of_movies(request):
    movies = Movie.objects.all()
    directors = Director.objects.all()
    genres = Genre.objects.all()

    return render(
        request,
        'listofmovies/listofmovies.html',
        context = {'movies': movies, 'directors': directors, 'genres': genres}
    )

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie_genre = Movie.objects.all()
    genres = Genre.objects.all()

    return render(
        request,
        'listofmovies/movie_detail.html',
        {'movie': movie, 'movie_genre': movie_genre, 'genres': genres}
    )

def list_of_genres(request):
    genres = Genre.objects.all()

    return render(
        request,
        'listofmovies/genres.html',
        context = {'genres': genres}
    )

def genre_details(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)

    return render(
        request,
        'listofmovies/genre_detail.html',
        {'genre': genre}
    )
