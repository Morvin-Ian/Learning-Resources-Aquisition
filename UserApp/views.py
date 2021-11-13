
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from ResourceApp.models import Borrowed_Resource




@login_required
def index(request):
    return render(request, 'UserApp/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f'Account creation for {username} succesful')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'UserApp/register.html',{"form":form})


