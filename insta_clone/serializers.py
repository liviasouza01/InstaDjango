from rest_framework import serializers
from post.models import Post
from reaction.models import Like, Comment
from user_profile.models import Profile
from chatrooms.models import Message

#REST FRAMEWORK

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'likes',
            'photo',
            'caption',
            'location',
        )

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'likes',
        )

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'user',
            'post',
            'body',
        )

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'first_name',
            'last_name',
            'gender',
        )

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'username',
            'content',
        )