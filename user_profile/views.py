from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from post.models import Post
from follow.models import Follow
from user_profile.models import Profile
from user_profile.forms import EditProfileForm

from insta_clone.serializers import ProfileSerializers
from rest_framework import viewsets


# Create your views here.

@login_required
def profile(request, username):
    # Get the user object based on the provided username
    user = get_object_or_404(User, username=username)
    # Get the profile associated with the user
    profile = Profile.objects.get(user=user)
    # Get all posts of the user, ordered by creation date
    posts = Post.objects.filter(user=user).order_by('-created_at')
    # Count the number of posts
    post_count = Post.objects.filter(user=user).count()
    # Count the number of users the current user is following
    following_count = Follow.objects.filter(followers=user).count()
    followers_count = Follow.objects.filter(following=user).count()
    follow_status = Follow.objects.filter(followers=request.user, following=user).exists()

    # Prepare context data to be passed to the template
    context = {
        'title': 'Profile',
        'profile': profile,
        'posts': posts,
        'post_count': post_count,
        'following_count': following_count,
        'followers_count': followers_count,
        'follow_status': follow_status
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user__id=user.id)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # If form data is valid, update the profile information
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.nickname = form.cleaned_data.get('nickname')
            profile.phone = form.cleaned_data.get('phone')
            profile.location = form.cleaned_data.get('location')
            profile.website = form.cleaned_data.get('website')
            profile.bio = form.cleaned_data.get('bio')
            profile.gender = form.cleaned_data.get('gender')
            profile.save()
            return HttpResponseRedirect(reverse('profile:profile', args=[user.username]))
    else:
        form = EditProfileForm()

    context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'edit-profile.html', context)

#REST
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers