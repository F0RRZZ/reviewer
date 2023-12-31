# Generated by Django 3.2.16 on 2023-07-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_alter_person_height'),
        ('movies', '0006_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='actors', to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='artist',
            field=models.ManyToManyField(blank=True, related_name='artist', to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='composer',
            field=models.ManyToManyField(blank=True, related_name='composer', to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, related_name='director', to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='montage',
            field=models.ManyToManyField(blank=True, related_name='montage', to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='operator',
            field=models.ManyToManyField(blank=True, related_name='operator', to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='producer',
            field=models.ManyToManyField(blank=True, related_name='producer', to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenwriter',
            field=models.ManyToManyField(blank=True, related_name='screenwriter', to='persons.Person'),
        ),
    ]
