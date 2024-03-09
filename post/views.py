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

@login_required
def feeds(request):
    # Get the current user
    user = request.user
    
    # Retrieve all posts from the user's stream and order them by creation date
    posts = Stream.objects.filter(user=user)
    post_list = [post.post_id for post in posts]
    all_posts = Post.objects.filter(id__in=post_list).order_by('-created_at')

    # Prepare context data to be passed to the template
    context = {'title': 'Feeds', 'all_posts': all_posts}
    
    # Render the feeds template with the context data
    return render(request, 'feed.html', context)

@login_required
def create_post(request):
    # Get the ID of the current user
    user_id = request.user.id
    
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            # If the form is valid, save the new post
            photo = form.cleaned_data.get('photo')
            caption = form.cleaned_data.get('caption')
            location = form.cleaned_data.get('location')

            post, created_at = Post.objects.get_or_create(photo=photo, caption=caption, user_id=user_id)
            post.save()
            return redirect('post:home')
    else:
        # If the request method is GET, render the form
        form = CreatePostForm()

    # Prepare context data to be passed to the template
    context = {'title': 'Create New Post', 'form': form, 'user': request.user}
    
    # Render the create-post template with the context data
    return render(request, 'create-post.html', context)

@login_required
def post_details(request, id):
    # Get the post object by its ID
    post = get_object_or_404(Post, id=id)
    
    # Retrieve comments related to the post and order them by commented_at
    comments = Comment.objects.filter(post=post).order_by('commented_at')

    if request.method == 'POST':
        # If the request method is POST, process the comment form data
        form = CommentForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the comment
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('post:post_details', args=[id]))
    else:
        # If the request method is GET, render the comment form
        form = CommentForm()

    # Prepare context data to be passed to the template
    context = {'title': 'Post Details', 'post': post, 'form': form, 'comments': comments}
    
    # Render the post-detail template with the context data
    return render(request, 'post-detail.html', context)

@login_required
def search(request):
    # Retrieve the query from the request
    query = request.GET.get('query', None)
    
    if query:
        # If a query exists, filter users based on the query
        users = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
        # Use __iexact for exact match
        
    else:
        # If no query exists, retrieve all users
        users = User.objects.all()
    
    # Prepare context data to be passed to the template
    context = {'title': 'Search Results', 'users': users}
    
    # Render the search template with the context data
    return render(request, 'search.html', context)
