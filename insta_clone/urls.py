from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Route to the Django admin page
    path('admin/', admin.site.urls),

    # Includes URLs from the apps
    path('', include('post.urls')),
    path('user/', include('user.urls')),
    path('profile/', include('user_profile.urls')),
    path('follow/', include('follow.urls')),
    path('reactions/', include('reaction.urls')),
    path('notification/', include('notification.urls')),
    path('chat/', include('chatrooms.urls')),

    # Routes for password reset using Django auth views
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset-password-done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset-password-confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset-password-complete.html'), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Custom configuration for the Django admin panel
admin.site.site_header = "Instagram Administration"
admin.site.site_title = "Admin"
admin.site.index_title = "Instagram"

