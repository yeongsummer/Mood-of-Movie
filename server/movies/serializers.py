from rest_framework import serializers
from .models import Movie, Review, Comment


class MovielistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('poster_path','title',)


class MovieSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(write_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id','title',)


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'


class CommentlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'

