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
    # Get the current logged-in user
    user = request.user
    # Get the user who is being followed/unfollowed
    following = get_object_or_404(User, username=username)

    try:
        # Check if there is already a follow relationship between the users
        f, created = Follow.objects.get_or_create(followers=user, following=following)
        if int(option) == 0:  # If option is 0, unfollow the user
            # Delete the follow relationship
            f.delete()
            # Delete all posts from the user being followed in the current user's stream
            Stream.objects.filter(following=following, user=user).all().delete()
        else:  # If option is not 0, follow the user
            # Get all posts from the user being followed
            posts = Post.objects.all().filter(user=following)
            with transaction.atomic():
                # Add each post to the current user's stream
                for post in posts:
                    stream = Stream(post=post, user=user, following=following, date=post.created_at)
                    stream.save()
        # Redirect to the profile page of the user being followed/unfollowed
        return HttpResponseRedirect(reverse('profile:profile', args=[username]))
    except User.DoesNotExist:
        # Redirect to the profile page of the user being followed/unfollowed if the user doesn't exist
        return HttpResponseRedirect(reverse('profile:profile', args=[username]))
