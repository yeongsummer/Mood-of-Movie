from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import (
    MovielistSerializer, 
    MovieSerializer, 
    ReviewlistSerializer,
    ReviewSerializer, 
    CommentlistSerializer,
    CommentSerializer
    )
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Review, Comment, Genre, Actor, Director, Keyword
from django.contrib.auth import get_user_model
from tmdb import TMDBHelper
import requests


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    if request.method == 'GET':
        movies = movie_ranking()
        serializers = MovielistSerializer(movies, many=True)
        return Response(serializers.data)


def movie_ranking():
    tmdbhelper = TMDBHelper('fc736c578445be44e87a385015c5331d')
    url = tmdbhelper.get_request_url(method=f'/movie/popular', language='ko', region='KR')
    response = requests.get(url).json()
    movies = []
    for movie in response['results']:
        movie_obj, flag = Movie.objects.get_or_create(
            movie_id = movie['id'],
            title = movie['title'],
            overview = movie['overview'],
            release_date = movie['release_date'],
            popularity = movie['popularity'],
            poster_path = movie['poster_path'],
            vote_average = movie['vote_average'],
            vote_count = movie['vote_count'],
        )
        if flag :
            for genre_pk in movie['genre_ids']:
                genre = get_object_or_404(Genre, pk=genre_pk)
                movie_obj.genres.add(genre)

            movie_id = movie['id']
            url = tmdbhelper.get_request_url(method=f'/movie/{movie_id}/credits', language='ko', region='KR')
            response = requests.get(url).json()

            for cast in response['cast'] :
                if cast['cast_id'] < 10 :
                    actor = Actor.objects.get_or_create(id = int(cast['id']), name = cast['name'])[0]
                    movie_obj.actors.add(actor)

            for crew in response['crew'] :
                if crew['department'] == 'Directing' and crew['job'] == 'Director':
                    director = Director.objects.get_or_create(id = int(crew['id']), name = crew['name'])[0]
                    movie_obj.directors.add(director)

        movies.append(movie_obj)
    return movies

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_list_create(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializers = ReviewlistSerializer(reviews, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def comment_list_create(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializers = CommentlistSerializer(comments, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = CommentlistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_user.filter(pk=request.user.pk).exists():
        movie.like_user.remove(request.user)
        liked = False
    else:
        movie.like_user.add(request.user)
        liked = True
    context = {
        'liked': liked,
        'like_count': movie.like_user.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_user.filter(pk=request.user.pk).exists():
        review.like_user.remove(request.user)
        liked = False
    else:
        review.like_user.add(request.user)
        liked = True
    context = {
        'liked':liked,
        'like_count':review.like_user.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


def movie_recommend(request, movie_pk):
    pass


# @api_view(['POST'])
# def user_reviews(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     reviews = user.review_set.all()
#     data = []
#     reviews_pk = request.data
#     for review_pk in reviews_pk:
#         review = get_object_or_404(Review, pk=review_pk)
#         serializer = ReviewSerializer(review)
#         data.append(serializer.data)
#     return Response(data)


# @api_view(['POST'])
# def user_comments(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     comments = user.comment_set.all()
#     data = []
#     comments_pk = request.data
#     for comment_pk in comments_pk:
#         comment = get_object_or_404(Comment, pk=comment_pk)
#         serializer = CommentSerializer(comment)
#         data.append(serializer.data)
#     return Response(data)