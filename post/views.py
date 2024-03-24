from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from post.models import Post
from follow.models import Stream
from reaction.models import Like, Comment
from reaction.forms import CommentForm
from post.forms import CreatePostForm

#CROPPING
from PIL import Image
import tempfile
import os
import io


#REST FRAMEWORK
from rest_framework import viewsets
#API
from insta_clone.serializers import *
#===================

# Create your views here.

@login_required
def feeds(request):
    user = request.user
    # Get all posts in the user's feed
    posts = Stream.objects.filter(user=user)
    post_list = []

    # Extract post IDs from the stream
    for post in posts:
        post_list.append(post.post_id)

    # Get all posts based on extracted post IDs, ordered by creation date
    all_posts = Post.objects.filter(id__in=post_list).all().order_by('-created_at')

    # Prepare context data to be passed to the template
    context = {'title': 'Feeds', 'all_posts': all_posts}
    # Render the feed.html template with the context data
    return render(request, 'feed.html', context)

@login_required
def create_post(request):
    user = request.user.id

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            # If form data is valid, extract photo, caption, and location
            photo = form.cleaned_data.get('photo')
            caption = form.cleaned_data.get('caption')
            location = form.cleaned_data.get('location')

            # Resize
            img = Image.open(photo)
            rotate = img.rotate(-90, expand=True) #don't know why, but I needed it
            width = 300
            height = 400
            img_resized = rotate.resize((width, height))
            

            # Save img resized
            img_io = io.BytesIO()
            img_resized.save(img_io, format='JPEG')

            post = Post(user_id=user, caption=caption, location=location)
            post.photo.save(photo.name, img_io)

            # Redirect
            return redirect('post:home')
    else:
        # If method is not POST
        form = CreatePostForm()

    # Prepare data to template
    context = {'title': 'Create New Post', 'form': form, 'user': request.user}
    return render(request, 'create-post.html', context)

@login_required
def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post).order_by('commented_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # If form data is valid, save the comment associated with the post
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('post:post_details', args=[id]))
    else:
        form = CommentForm()

    context = {'title': 'Post Details', 'post': post, 'form': form, 'comments': comments}
    return render(request, 'post-detail.html', context)

@login_required
def search(request):
    try:
        # Try to retrieve the 'query' parameter from the GET request
        query = request.GET['query']
    except:
        # If 'query' parameter is not found, set it to None
        query = None
    if query:
        # If 'query' parameter is not None, perform a search
        # Search users based on username, first name, or last name containing the query string
        users = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
        # __iexact for exact match
    else:
        # If 'query' parameter is None, retrieve all users
        users = User.objects.all()
    context = {'title': 'Search Results', 'users': users}
    return render(request, 'search.html', context)

#REST FRAMEWORK
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

