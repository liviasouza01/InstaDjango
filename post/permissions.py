from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from .models import Post
from reaction.models import Comment
from rest_framework import permissions

class PermissionsPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        post_id = view.kwargs.get('pk')  

        if request.method == 'DELETE':
            # Only auth users
            post = get_object_or_404(Post, pk=post_id)
            if request.user.is_authenticated and post.user.id == request.user.id:
                return True
            return False
        
        if request.method == 'POST':
            # Only auth users can create
            if request.user.is_authenticated:
                return True
            return False
        
        if request.method == 'PUT':
            # Only auth users can edit
            post = get_object_or_404(Post, pk=post_id)
            if request.user.is_authenticated and post.user.id == request.user.id:
                return True
            return False

        return True  

class PermissionsComment(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        comment_id = view.kwargs.get('pk')  # Like id from views

        if request.method == 'DELETE':
            # Only auth users
            comment = get_object_or_404(Comment, pk=comment_id)
            if request.user.is_authenticated and comment.user.id == request.user.id:
                return True
            return False
        
        if request.method == 'POST':
            # Only auth users can create
            if request.user.is_authenticated:
                return True
            return False
        
        if request.method == 'PUT':
            # Only auth users can edit
            comment = get_object_or_404(Comment, pk=comment_id)
            if request.user.is_authenticated and comment.user.id == request.user.id:
                return True
            return False
        
        return True  
