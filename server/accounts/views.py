from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, UserImgSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from movies.serializers import MovielistSerializer, ReviewlistSerializer
from movies.models import Review

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def user_profile_update_delete(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.user != user:
        return Response({'profile':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        return Response({ 'id': user_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def password(request):
    print('실행')
    print(request.data)
    user = request.user

    old_password = request.data['old_password']
    if old_password is not None:
        password_match = user.check_password(old_password) #현재 비번이 맞는 지 체크
        if password_match:
            new_password1 = request.data['new_password1']
            if new_password1 is not None:
                user.set_password(new_password1)
                user.save()
                return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def follow(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)
    if request.method == 'GET':
        if user.followers.filter(pk=request.user.pk).exists():
            followed = True
        else:
            followed = False
    elif request.method == 'POST':
        if user != request.user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
                followed = True
            else:
                user.followers.add(request.user)
                followed = False
    
    context = {
        'followed': followed,
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    return Response({ 'id': request.user.id, 'nickname': request.user.nickname })


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_followers(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)
    followers = user.followers.all()
    serializer = UserSerializer(followers, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_followings(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)
    followings = user.followings.all()
    serializer = UserSerializer(followings, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_like_movies(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)
    like_movies = user.like_movies.all()

    serializer = MovielistSerializer(like_movies, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_review(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)
    reviews = Review.objects.filter(user=user)
    serializers = ReviewlistSerializer(reviews, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def upload_img(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)

    if request.method == 'GET':
        serializer = UserImgSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.user != user:
        return Response({'profile':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = UserImgSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)