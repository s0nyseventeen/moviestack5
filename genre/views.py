from django.shortcuts import render, get_object_or_404
from listofmovies.models import Genre, Movie




def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', context = {'genres': genres})

def genre_detail(request, genre_id):
    genres = get_object_or_404(Genre, pk=genre_id)
    genre_detail = Genre.objects.all()
    return render(request, 'genre_detail.html', context={'genres': genres, 'genre_detail': genre_detail})

# def movie_details(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     movie_genre = Movie.objects.all()
#
#     return render(
#         request,
#         'movie_detail.html',
#         {'movie': movie, 'movie_genre': movie_genre}
#     )
