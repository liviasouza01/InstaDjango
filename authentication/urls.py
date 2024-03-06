from django.contrib import auth
from django.urls import path
from . import views
from .forms import LoginForm, PassResetForm, SetPassForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    
    path('login/', auth_views.LoginView.as_view
     (template_name= 'auth/login.html', authentication_form=LoginForm), 
     name='login'),

    path('password_reset/', auth_views.PasswordResetView.as_view
     (template_name='auth/pass_reset.html', form_class=PassResetForm),
     name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view
     (template_name='auth/pass_reset_done.html'), 
     name='password_reset_done'),

    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
     (template_name='auth/pass_reset_confirm.html', form_class=SetPassForm),
     name='password_reset_confirm'),

    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view
     (template_name='auth/pass_reset_complete.html'), 
     name='password_reset_complete'),

]
