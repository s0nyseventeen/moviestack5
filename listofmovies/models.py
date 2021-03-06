from django.db import models
from django.conf import settings


class Genre(models.Model):

	name = models.CharField(max_length=200, help_text='Enter a movie genre')
	image = models.ImageField(upload_to='listofmovies/', null=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Movie(models.Model):

	title = models.CharField(max_length=200)
	release = models.IntegerField(default=0)
	poster = models.ImageField(upload_to='listofmovies/')
	company = models.CharField(max_length=200, help_text='Enter a company of movie')
	description = models.TextField(help_text='Enter a short description', max_length=1000, null=True)
	language = models.CharField(max_length=200, help_text='Choose a language of the movie')
	genre = models.ManyToManyField(Genre, help_text='Choose a genre of the movie')
	director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
	big_photo = models.ImageField(upload_to='listofmovies/', null=True)

	rating_list = (
		('1', '*'),
		('2', '**'),
		('3', '***'),
		('4', '****'),
		('5', '*****'),
	)

	rating = models.CharField(max_length=100, choices=rating_list, help_text='rating of a movie')

	def __str__(self):
		return self.title

	def get_summary(self):
		return self.description[:100] + '...'

	def show_genre(self):
		return ', '.join([ genre.name for genre in self.genre.all()[:3]] )

	show_genre.short_description = 'Genre'


class Director(models.Model):

	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
