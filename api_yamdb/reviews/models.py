from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug


class Genre(models.Model):
    BOOKS = 'books'
    MOVIES = 'movies'
    MUSIC = 'music'

    GENRES = [
        (BOOKS, 'Книги'),
        (MOVIES, 'Фильмы'),
        (MUSIC, 'Музыка')
    ]

    name = models.CharField(
        max_length=256,
        choices=GENRES,)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug


class Title(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='categories',
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='genres',
    )
    name = models.CharField(max_length=256)
    year = models.PositiveIntegerField()
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
