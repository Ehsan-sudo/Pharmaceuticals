from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('home')
    else:
        return render(request, 'users/register.html')