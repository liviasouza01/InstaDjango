from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from chatrooms.routing import websocket_urlpatterns

#Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Instagram Clone",
      default_version='v6',
      description="This is a project proposed by Loomi to check backend knowledge",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="liviaa.sa@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('user/', include('user.urls')),
    path('profile/', include('user_profile.urls')),
    path('follow/', include('follow.urls')),
    path('reactions/', include('reaction.urls')),
    path('notification/', include('notification.urls')),
    path('chat/', include('chatrooms.urls')),


    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset-password-done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset-password-confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset-password-complete.html'), name='password_reset_complete'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Instagram Adminstration"
admin.site.site_title = "Admin"
admin.site.index_title = "Instagram"