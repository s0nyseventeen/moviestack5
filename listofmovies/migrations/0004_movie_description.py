# Generated by Django 3.1.3 on 2020-11-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listofmovies', '0003_auto_20201116_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(help_text='Enter a short description', max_length=1000, null=True),
        ),
    ]
