from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from follow.models import Follow, Stream
from post.models import Post

# Create your views here.

@login_required
def follow(request, username, option):
    # Retrieve the currently logged-in user
    user = request.user
    # Retrieve the user being followed based on the provided username
    following = get_object_or_404(User, username=username)

    try:
        # Attempt to get or create a Follow instance representing the relationship between the logged-in user and the user being followed
        f, created = Follow.objects.get_or_create(followers=user, following=following)
        # If the option is 0, indicating an unfollow action
        if int(option) == 0:
            # Delete the Follow instance representing the relationship
            f.delete()
            # Remove related items from the Stream model
            Stream.objects.filter(following=following, user=user).all().delete()
        else:
            # Retrieve all posts from the user being followed
            posts = Post.objects.all().filter(user=following)
            # Use a transaction to ensure atomicity
            with transaction.atomic():
                # Iterate over the posts
                for post in posts:
                    # Create a Stream instance for each post, effectively adding those posts to the user's stream
                    stream = Stream(post=post, user=user, following=following, date=post.created_at)
                    stream.save()
        # Redirect the user to the profile page of the user being followed
        return HttpResponseRedirect(reverse('profile:profile', args=[username]))
    except User.DoesNotExist:
        # If the specified user does not exist, redirect the user to the profile page of the specified username
        return HttpResponseRedirect(reverse('profile:profile', args=[username]))
