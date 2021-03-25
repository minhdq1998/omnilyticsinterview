from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'body',
            'owner',
        ]

        extra_kwargs = {
            'owner': { 'write_only': True },
        }

        