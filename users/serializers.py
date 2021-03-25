from rest_framework import serializers

from posts.serializers import PostSerializer

from .models import User

class UserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            'pk',
            'name',
            'username',
            'email',
            'phone',
            'posts'
        ]