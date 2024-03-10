from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from follow.models import Follow, Stream
from post.models import Post

@login_required
def follow(request, username, option):
    user = request.user
    # Get the user who is being followed/unfollowed
    following = get_object_or_404(User, username=username)

    try:
        # Check if there is already a follow relationship between the users
        f, created = Follow.objects.get_or_create(followers=user, following=following)

        # If option is 0, unfollow the user
        if int(option) == 0:
            # Delete the follow relationship
            f.delete()
            Stream.objects.filter(following=following, user=user).delete()
        else:
            # Get all posts from the user being followed with related user info
            posts = Post.objects.prefetch_related('user').filter(user=following)
            with transaction.atomic():
                # Create Stream objects for each post
                streams = [Stream(post=post, user=user, following=following, date=post.created_at) for post in posts]
                # Bulk create Stream objects
                Stream.objects.bulk_create(streams)

        return HttpResponseRedirect(reverse('profile:profile', args=[username]))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile:profile', args=[username]))
