# Generated by Django 3.1.3 on 2020-11-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listofmovies', '0002_auto_20201116_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(help_text='Choose a genre of the movie', to='listofmovies.Genre'),
        ),
    ]
