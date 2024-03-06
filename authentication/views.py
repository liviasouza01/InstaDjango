from django.shortcuts import redirect, render
from . import models
from . import forms
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return redirect('login')

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            full_name = form.cleaned_data['full_name'].split()

            if len(full_name) <= 1:
                empt_str =''
                user.first_name = empt_str.join(full_name)

            else:
                fname = full_name[0]
                lname = full_name[1]
                user.first_name = fname
                user.last_name = lname
            user.save()
            messages.success(request, 'Successfully Signed in!')
            return redirect('login')
    else:
        form = forms.SignUpForm()
    return render(request, 'auth/signup.html', {'form':form})
