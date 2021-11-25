from rest_framework import serializers
from .models import Movie, Review, Comment
from django.contrib.auth import get_user_model


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'nickname','email')
        

class MovielistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(write_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewlistSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    
    class Meta:
        model = Review
        fields = ('id','title','rank','content','created_at','user','movie_id')


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    movie = MovieSerializer()
    
    class Meta:
        model = Review
        fields = ('id','user','rank','movie','title','content','created_at','updated_at')


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id','rank','title','content')


class CommentlistSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    
    class Meta:
        model = Comment
        fields = ('id','content','user','created_at')


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id','content','user')


