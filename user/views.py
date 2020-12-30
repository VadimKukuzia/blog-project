from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from user.forms import UserRegisterForm, UserLoginForm


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
        form = UserLoginForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f'Hello, {user.username}')
            return redirect('index')
        else:
            messages.info(request, 'Username or password don`t match')
            return render(request, 'user/login.html', {'form': form})
    else:
        form = UserLoginForm()

    return render(request, 'user/login.html', {'form': form})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been successfully logged out')
        return redirect('index')
    return redirect('index')
