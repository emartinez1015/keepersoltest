from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token
# Models
from django.contrib.auth.models import User
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    """
    Bookmark serializer
    """
    class Meta:
        model = Bookmark
        fields = ('id', 'title', 'url', 'created_at', 'is_public', 'owner' )

class UserLoginSerializer(serializers.Serializer):
    """
    User Login Serializer
    Handle the login request data
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    def validate(self, data):
        """
        Check credentials
        """
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data
    
    def create(self, validated_data):
        """
        Generate or retrieve new token
        """
        user = self.context['user']
        token, created = Token.objects.get_or_create(user=user)
        return user, token.key

class UserModelSerializer(serializers.ModelSerializer):
    """
    User model serializer
    """
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email', )