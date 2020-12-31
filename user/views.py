from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from user.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f'Hello, {user.username}')
            return redirect('index')
        else:
            messages.info(request, 'Username or password don`t match')
            return render(request, 'user/login.html', {'form': form})
    else:
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form})


def log_out(request):
    logout(request)
    messages.info(request, 'You have been successfully logged out')
    return redirect('index')


@login_required(login_url='log-in')
def profile(request):
    return render(request, 'user/profile.html')
