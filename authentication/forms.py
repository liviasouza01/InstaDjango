from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (AuthenticationForm, UsernameField, 
 UserCreationForm, PasswordResetForm, SetPasswordForm)


def ForbiddenUsers(value):
    forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root',
    'email', 'user', 'join', 'sql', 'static', 'python', 'delete']
    if value.lower() in forbidden_users:
        raise ValidationError('Invalid name for user, this is a reserverd word.')

def InvalidUser(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('This is an Invalid username, Username may contain only letters, numbers, and ./_ characters.')

def UniqueEmail(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this email already exists.')

def UniqueUser(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this username already exists.')


class SignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs=
    {'class':'form-control shadow-none', 'autofocus':True, 'placeholder':'Email Address'}))

    full_name = forms.CharField(widget=forms.TextInput(attrs=
    {'class':'form-control shadow-none', 'placeholder':'Full Name'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs=
    {'class':'form-control shadow-none', 'placeholder':'Password',
     'autocomplete':'current-password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=
    {'class':'form-control shadow-none', 'placeholder':'Confirm Password',
     'autocomplete':'current-password'}))

    class Meta():
        model = User
        fields = ['email','full_name', 'username', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs=
         {'class':'form-control shadow-none', 
         'autofocus':False, 'placeholder':'Username'})}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsers)
        self.fields['username'].validators.append(InvalidUser)
        self.fields['username'].validators.append(UniqueUser)
        self.fields['email'].validators.append(UniqueEmail)


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs=
     {'class':'form-control shadow-none', 'placeholder':'Username'}))

    password = forms.CharField(label=_("Password"), strip=False, 
     widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 
     'class':'form-control shadow-none', 'placeholder':'Password'}))


class PassResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs=
    {'autofocus':True,'class':'form-control shadow-none',
    'autocomplete':'email', 'placeholder':'Email'}))


class SetPassForm(SetPasswordForm):
    new_password1 = forms.CharField(strip=False, widget=forms.PasswordInput
     (attrs={'autocomplete':'new-password', 
     'placeholder':'New Password', 'class':'form-control shadow-none pass-confirm'}), 
     help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(strip=False, widget=forms.PasswordInput
     (attrs={'autocomplete':'new-password', 
     'placeholder':'Confirm New Password', 'class':'form-control shadow-none pass-confirm'}))
