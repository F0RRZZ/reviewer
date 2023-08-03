# Generated by Django 3.2.16 on 2023-08-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20230713_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_link',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='imdb_link'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='budget'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(blank=True, help_text='Maximum of 50 symbols', max_length=50, null=True, verbose_name='country'),
        ),
    ]
