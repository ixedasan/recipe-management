from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from user.models import Profile


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Wrong password')
        except:
            messages.error(request, f'User {username} does not exist')
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_image = request.FILES.get('user_image')
        bio = request.POST.get('bio')
        if User.objects.filter(username=username).exists():
            messages.error(request, f'User {username} already exists')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
            )
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                Profile.objects.create(
                    user=new_user,
                    image_profile=user_image,
                    bio=bio,
                )
                return redirect('index')

    return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    return redirect('index')
