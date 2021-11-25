from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import (
    MovielistSerializer, 
    MovieSerializer,
    ReviewDetailSerializer, 
    ReviewlistSerializer,
    ReviewSerializer, 
    CommentlistSerializer,
    CommentSerializer,
    )
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Review, Comment, Genre, Actor, Director, Keyword
from tmdb import TMDBHelper
import requests
from .recommend import recommend


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movie_titles = []
    if request.method == 'GET':
        movies = Movie.objects.all().values('title')
        for movie in movies:
            movie_titles.append(movie['title'])
        context = {
            'movie_titles': movie_titles
        }
        return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def popular_movie_list(request):
    if request.method == 'GET':
        movies = movie_ranking()
        serializers = MovielistSerializer(movies, many=True)
        return Response(serializers.data)


@permission_classes([AllowAny])
def movie_ranking():
    tmdbhelper = TMDBHelper('fc736c578445be44e87a385015c5331d')
    url = tmdbhelper.get_request_url(method=f'/movie/popular', language='ko', region='KR')
    response = requests.get(url).json()
    movies = []
    for movie in response['results']:
        if not Movie.objects.filter(movie_id=movie['id']).exists():
            movie_obj = Movie.objects.create(
                movie_id = movie['id'],
                title = movie['title'],
                overview = movie['overview'],
                release_date = movie['release_date'],
                popularity = movie['popularity'],
                poster_path = movie['poster_path'],
                vote_average = movie['vote_average'],
                vote_count = movie['vote_count'],
                )
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
        else:
            movie_obj = Movie.objects.filter(movie_id=movie['id'])[0]
        movies.append(movie_obj)
    return movies


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def review_list_all(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializers = ReviewlistSerializer(reviews, many=True)
        return Response(serializers.data)


@api_view(['GET', 'POST'])
def review_list_create(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie_id=movie_pk)
        serializers = ReviewlistSerializer(reviews, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    elif not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_search(request, search):
    reviews = Review.objects.filter(movie_id__title__icontains=search)
    print(reviews)
    serializers = ReviewlistSerializer(reviews, many=True)
    return Response(serializers.data)


@api_view(['GET', 'POST'])
def comment_list_create(request, review_pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_pk)
        serializers = CommentlistSerializer(comments, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        review = get_object_or_404(Review, pk=review_pk)
        print('review',review)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def comment_detail_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        if movie.like_users.filter(pk=request.user.pk).exists():
            liked = True
        else:
            liked = False
    elif request.method == 'POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            liked = False
        else:
            movie.like_users.add(request.user)
            liked = True
    context = {
        'liked': liked,
        'like_count': movie.like_users.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        if review.like_users.filter(pk=request.user.pk).exists():
            liked = True
        else:
            liked = False
    elif request.method == 'POST':
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            liked = False
        else:
            review.like_users.add(request.user)
            liked = True
    context = {
        'liked':liked,
        'like_count':review.like_users.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_recommend(request, movie_title):
    print(movie_title)
    movie_list = recommend(movie_title)
    if movie_list:
        movies = []
        for movie_title in movie_list:
            movies.append(Movie.objects.filter(title=movie_title)[0])
        serializers = MovielistSerializer(movies, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getMovieVideoKey(request, movie_pk):
    tmdbhelper = TMDBHelper('fc736c578445be44e87a385015c5331d')
    movie = Movie.objects.filter(pk=movie_pk)[0]
    url = tmdbhelper.get_request_url(method=f'/movie/{movie.movie_id}/videos')
    response = requests.get(url).json()
    video_key = response['results'][-1]['key']
    movie = Movie.objects.filter(pk=movie_pk)[0]
    directors = movie.directors.all()
    genres = movie.genres.all()
    director_list = []
    genre_list = []
    for director in directors:
        director_list.append(director.name)
    for genre in genres:
        genre_list.append(genre.name)
    context = {
        'video_key': video_key,
        'director_list': director_list,
        'genre_list': genre_list,
    }
    return Response(context, status=status.HTTP_200_OK)