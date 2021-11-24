from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
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


# @api_view(['POST'])
# def password(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)

#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, '비밀번호가 변경되었습니다.')
#             return HttpResponse(status=200)
#         else:
#             messages.error(request, '비밀번호 변경 실패')
#     else:
#         form = PasswordChangeForm(request.user)
    
#     context = {
#         'form': form
#     }
#     return Response(context)


@api_view(['POST'])
def follow(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return HttpResponse(status=200)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    return Response({ 'id': request.user.id, 'nickname': request.user.nickname })


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_follow(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)

    followers = user.followers
    followings = user.followings
    like_movies = user.like_movies
    print(followings, followers)
    return Response({ 'followers': followers, 'followings': followings, 'likeMovieList': like_movies })