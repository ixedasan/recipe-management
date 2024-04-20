from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from user.models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm


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
            messages.error(request, f'User does not exist')
    return render(request, 'login.html')


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        user_image = request.FILES.get('user_image')
        bio = request.POST.get('bio')
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                image_profile=user_image,
                bio=bio,
            )
            login(request, user)
            return redirect('index')
        else:
            for error in form.errors.values():
                for msg in error:
                    messages.error(request, msg)
    context = {'form': form}
    return render(request, 'signup.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
