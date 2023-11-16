from rest_framework import serializers
from .models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content']
        read_only_fields = ['user']
