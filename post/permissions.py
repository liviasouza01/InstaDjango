from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from .models import Post

class PermissionsPost(permissions.BasePermission):
    def has_permission(self, request, view):
        post_id = view.kwargs.get('pk')  # Post id from views

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