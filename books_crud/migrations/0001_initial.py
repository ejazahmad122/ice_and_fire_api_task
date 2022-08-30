# Generated by Django 4.1 on 2022-08-15 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookShelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=14)),
                ('country', models.CharField(max_length=200)),
                ('number_of_pages', models.IntegerField()),
                ('publisher', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_crud.author')),
            ],
        ),
    ]