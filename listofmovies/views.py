from django.shortcuts import render, get_object_or_404
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

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})
