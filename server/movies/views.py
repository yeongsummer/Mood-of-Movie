from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_safe, require_POST
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


def movie_like(request, movie_pk):
    pass


def review_like(request, review_pk):
    pass


def follow(request, user_pk):
    pass