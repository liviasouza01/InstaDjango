from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from reaction.models import Like
from post.models import Post

@login_required
def likes(request, id):
    # Get the current user
    user = request.user
    
    # Get the post object by its ID
    post = Post.objects.get(id=id)
    
    # Get the current number of likes for the post
    current_likes = post.likes
    
    # Check if the user has already liked the post
    liked = Like.objects.filter(user=user, post=post).count()

    if not liked:
        # If the user has not liked the post, create a new Like object
        liked = Like.objects.create(user=user, post=post)
        current_likes += 1
    else:
        # If the user has already liked the post, delete the Like object
        Like.objects.filter(user=user, post=post).delete()
        current_likes -= 1

    # Update the number of likes for the post
    post.likes = current_likes
    post.save()

    # Redirect the user back to the post details page
    return HttpResponseRedirect(reverse('post:post_details', args=[id]))
