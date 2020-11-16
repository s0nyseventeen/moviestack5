from django.shortcuts import render
from .models import Movie, Director

def home(request):
    return render(request, 'homepage.html')

def list_of_movies(request):
    movies = Movie.objects.all()
    directors = Director.objects.all()
    # genres = Genre.objects.all()

    return render(
        request,
        'listofmovies.html',
        context = {
            'movies': movies,
            'directors': directors,
            # 'genres': genres,
        }
    )
