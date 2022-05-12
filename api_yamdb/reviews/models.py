from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug


class Title(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='titles'
    )
    genre = models.ManyToManyField(
        Genre, on_delete=models.SET_NULL, related_name='titles'
    )
    name = models.CharField(max_length=256)
    year = models.PositiveIntegerField()
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
