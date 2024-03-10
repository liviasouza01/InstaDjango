from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from user.forms import ChangePasswordForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        # If the request method is POST, attempt to authenticate the user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # If authentication is successful, log in the user
            auth.login(request, user)
            messages.success(request, 'You have been logged in to your account!')
            return redirect('post:home')
        else:
            messages.error(request, 'Oops! Username and Password do not match!')
            return redirect('user:login')
    else:
        context = {'title': 'Login'}
        return render(request, 'login.html', context)

@login_required
def logout(request):
    # Log out the current user and display a success message
    auth.logout(request)
    messages.success(request, 'You have been logged out of your account!')
    return redirect('user:login')

def register(request):
    if request.method == 'POST':
        # If the request method is POST, attempt to register the user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # If passwords match, check if the username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Oops! User with this Username already exists.')
                return redirect('user:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Oops! User with this Email already exists.')
                return redirect('user:register')
            else:
                # If username and email are unique, create a new user
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request, f'Congratulations! {first_name}, Your account has been created!/n Now, please login and edit your informations.')
                return redirect('profile:edit-profile')
        else:
            # If passwords don't match, display an error message
            messages.error(request, 'Oops! Password do not match.')
            return redirect('user:register')

    else:
        # If the request method is not POST, render the registration page
        context = {'title': 'Register'}
        return render(request, 'signup.html', context)

def password_reset(request):
    # Render the password reset page
    context = {'title': 'Reset Password'}
    return render(request, 'reset-password.html', context)

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        # If the request method is POST, attempt to change the password
        form = ChangePasswordForm(request.POST, user)
        if form.is_valid():
            # If form is valid, retrieve old and new passwords
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if not user.check_password(old_password):
                messages.error(request, 'Oops! Your old password was entered incorrectly.')
                return redirect('user:change-password')
            elif new_password != confirm_password:
                messages.error(request, 'Oops! Your passwords do not match.')
                return redirect('user:change-password')
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Congratulations! Your password was changed successfully.')
                return redirect('post:home')

    else:
        form = ChangePasswordForm(instance=user)
    context = {'title':'Change Password', 'form':form}
    return render(request, 'change-password.html', context)
