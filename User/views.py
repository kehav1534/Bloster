from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from . import models
from posts.models import postModel
from django.contrib import messages

def user_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("/") 
        else:
            return redirect("/about")
    else:
        form=AuthenticationForm()
        return render(request, 'user/loginuser.html', {'login_form':form})
    
def user_signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            save=form.save()
            login(request, save)
            createUserProfile = models.UserProfile()
            createUserProfile.user=save
            createUserProfile.save()
            if 'next' in request.POST:
                messages.success(request, 'You have successfully signed up')
                redirect(request.POST.get('get'))
            else:
                messages.success(request, 'You have successfully signed up')
                return redirect("/")
        else:messages.error(request, "Error");return render(request, 'user/SignUp.html', {'signup_form': form})
    else:
        form = UserCreationForm()
        return render(request, 'user/SignUp.html', {'signup_form': form})

@login_required(login_url='/user/login/')
def user_logout(request):
    if request.method=="POST" and request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:redirect('/')
    
@login_required(login_url='/user/login/')
def user_profile(request):
    profile_data = get_object_or_404(models.UserProfile, user=request.user)
    if request.method=='POST':
        profile = forms.UserProfileForm(request.POST, request.FILES, instance=profile_data)
        if profile.is_valid():
            profile.save()
            return redirect('/')
    else:
        profile = forms.UserProfileForm(instance=profile_data)
        return render(request, 'user/profile.html', {'profile_data': profile})
    
@login_required(login_url='/user/login/')
def dashboard(request):
    userPosts = postModel.objects.filter(author=request.user).order_by("-creation_date")
    return render(request, 'user/dashboard.html', {'userposts':userPosts})