from django.shortcuts import render

# Render the home page template, after login

def home(request):
    return render(request, 'home/home.html')