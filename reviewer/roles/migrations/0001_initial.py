# Generated by Django 3.2.16 on 2023-07-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Maximum of 50 symbols', max_length=50, verbose_name='name')),
                ('formatted_name', models.CharField(max_length=50, verbose_name='formatted_name')),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
            },
        ),
    ]
