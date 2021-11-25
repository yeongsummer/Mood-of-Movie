from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('email', 'password', 'nickname')

    # def validate(self, data):
    #     password = data.get('password')
    #     username = data.get('username')
    #     user = User(username=username, password=password)
        
    #     error = ''
    #     try:
    #         validate_password(password, user=user)
    #     except ValidationError as e:
    #         error = e

    #     if error:
    #         raise ValidationError(error)

    #     return data


class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_img', 'id')