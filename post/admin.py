from django.contrib import admin
from .models import Post, Follow, Stream, Hashtag

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'id','posted', 'likes', 'picture']

@admin.register(Follow)
class FollowModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'follower', 'following']

@admin.register(Stream)
class StreamModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'following', 'post', 'date']

@admin.register(Hashtag)
class HashtagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
