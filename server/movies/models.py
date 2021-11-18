from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    director = models.CharField(max_length=50)
    release_date = models.DateField()
    poster_path = models.TextField()
    tag = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.content


