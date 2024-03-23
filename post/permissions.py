from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from .models import Post

class PermissionsPost(permissions.BasePermission):
    def has_permission(self, request, view):
        post_id = view.kwargs.get('pk')  # Obter o ID do post dos argumentos da visualização

        if request.method == 'DELETE':
            # Apenas usuários autenticados e de propriedade necessárias
            post = get_object_or_404(Post, pk=post_id)
            if request.user.is_authenticated and post.user.id == request.user.id:
                return True
            return False
        
        if request.method == 'POST':
            # Apenas usuários autenticados podem criar
            if request.user.is_authenticated:
                return True
            return False
        
        if request.method == 'PUT':
            # Apenas usuários autenticados e de propriedade necessárias
            post = get_object_or_404(Post, pk=post_id)

            print(request.user.is_authenticated)
            print(post.user.id)
            print(request.user.id)

            if request.user.is_authenticated and post.user.id == request.user.id:
                return True
            return False

        return True