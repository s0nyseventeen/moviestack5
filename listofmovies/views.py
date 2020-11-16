from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')

def list_of_movies(request):
    return render(request, 'listofmovies.html')
