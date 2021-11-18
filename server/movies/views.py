from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
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
from .models import Movie, Review, Comment
from django.contrib.auth import get_user_model


@api_view(['GET', 'POST'])
def movie_list_create(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializers = MovielistSerializer(movies, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
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