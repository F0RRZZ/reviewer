# Generated by Django 3.2.16 on 2023-08-09 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_movie_kinopoisk_link'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0006_rating_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_reviews', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
