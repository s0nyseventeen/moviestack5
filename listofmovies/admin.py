from django.contrib import admin
from .models import Movie, Genre, Director

admin.site.register(Genre)





@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'director', 'show_genre', 'release')
    list_filter = ('release', 'genre')
    
