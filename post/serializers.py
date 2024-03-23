from rest_framework import serializers
from post.models import Post
from reaction.models import Like, Comment

#REST FRAMEWORK

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'user',
            'id',
        )

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'user',
            'id',
        )

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'user',
            'id',
        )