from django.shortcuts import render, redirect
from .models import Follow, Post, Hashtag, Stream
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

@login_required
def post_view(request):
    user = request.user
    posts = Stream.objects.filter(user=user)

    group_ids = []

    for post in posts:
        group_ids.append(post.post.id)

    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    return render(request, 'post/post_view.html', {'post_items':post_items})
