from django.shortcuts import render, redirect
from .models import Follow, Post, Hashtag, Stream, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

@login_required
def post_view(request):
    user = request.user
    if (request.method == 'POST'):
        # get picture and caption
        picture = request.FILES['picture']
        caption = request.POST['caption']
        # create post
        post = Post(user=user, picture=picture, caption=caption)
        post.save()
        # save hashtags dont split just get the next word after the hashtag
        hashtags = caption.split('#')[1:]
        for hashtag in hashtags:
            if hashtag:
                hashtag = Hashtag.objects.get_or_create(title=hashtag)
                post.tags.add(hashtag[0])
        post.save()
        messages.success(request, 'Your post has been uploaded')
        # redirect to new post
        return redirect('postdetails', id=post.id)
    posts = Stream.objects.filter(user=user)

    group_ids = []

    for post in posts:
        group_ids.append(post.post.id)

    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    return render(request, 'post/post_view.html', {'post_items':post_items})


def get_single_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/single_post.html', {'post':post})

def comment(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    if (request.method == 'POST'):
        comment_text = request.POST['comment']
        comment = Comment(user=user, comment=comment_text)
        comment.save()
        post.comments.add(comment)
        post.save()
        messages.success(request, 'Your comment has been added')
        return redirect('postdetails', id=id)
    return render(request, 'post/single_post.html', {'post':post})
