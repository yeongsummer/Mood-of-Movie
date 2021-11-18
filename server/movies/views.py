from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views.decorators.http import require_safe, require_POST
from django.http import JsonResponse
from collections import defaultdict

from .models import Movie


def movie_index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


def movie_create(request, movie_pk):
    pass


def movie_update(request, movie_pk):
    pass


def movie_delete(request, movie_pk):
    pass


def movie_like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            is_like = False
        else:
            movie.like_users.add(user)
            is_like = True
        context = {
            'is_like': is_like,
            'like_count': movie.like_users.count()
        }
        return JsonResponse(context)
        
        # return redirect('community:index')
    return redirect('accounts:login')


@require_safe
def review_detail(request):
    pass


def review_create(request):
    pass


def review_update(request):
    pass


def review_delete(request):
    pass


def review_like(request):
    pass


def comment_create(request):
    pass


def comment_delete(request):
    pass


def follow(request):
    pass