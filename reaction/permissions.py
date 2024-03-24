from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from .models import Like

class PermissionsLike(permissions.BasePermission):
    def has_permission(self, request, view):
        like_id = view.kwargs.get('pk')  # Like id from views

        if request.method == 'DELETE':
            # Only auth users
            like = get_object_or_404(Like, pk=like_id)
            if request.user.is_authenticated and like.user.id == request.user.id:
                return True
            return False
        
        if request.method == 'POST':
            # Only auth users can create
            if request.user.is_authenticated:
                return True
            return False

        return True