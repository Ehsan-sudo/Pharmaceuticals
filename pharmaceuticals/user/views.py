from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout


def register(request):
    if request.POST:
        # if form is valid:
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        confirm = request.POST.get('confirm')
        if password == confirm:
            print(username, password)
            user = User(username=username, password=password)
            user.save()
            return login_user(request, user)
    else:
        return render(request, 'users/register.html')

def login_user(request, user):
    auth_login(request, user)
    messages.success(request, f'Welcome {user.username}!')
    return redirect('home')

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        print(username, password)
        user = User.objects.filter(username=username, password=password).first()
        print(user)
        if user:
            return login_user(request, user)
        else:
            messages.error(request, f'Username or password incorrect!')
    return render(request, 'users/login.html')
        

