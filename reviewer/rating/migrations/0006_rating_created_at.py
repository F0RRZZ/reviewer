# Generated by Django 3.2.16 on 2023-07-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_auto_20230711_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
    ]
