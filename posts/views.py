from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from User.models import UserProfile

def to_homepage(request):
    return redirect('/')

@login_required(login_url="/user/login/")
def createpost(request):
    if request.method=='POST':
        userpost = forms.CreatePost(request.POST, request.FILES)
        if userpost.is_valid():
            userpost = userpost.save(commit=False)
            userpost.author = request.user
            userpost.save()
            return redirect('/user/dashboard/')
    else:
        userpost = forms.CreatePost()
        return render(request, 'posts/WorkOnPost.html', {'postform':userpost, 'title':'Create Post', 'act':'/posts/create/'})
    
    
def showpost(request, ulink):
    post = get_object_or_404(models.postModel, ulink=ulink)
    if post.status=='d' and post.author!=request.user:
        raise Http404
    else:
        author = get_object_or_404(UserProfile, user=post.author)
        return render(request, 'posts/ViewPost.html', {'data':post, 'author':author})
        

@login_required(login_url="/user/login/")
def editpost(request):
    if request.method=='GET':
        if p:=request.GET.get('p'):
            try:
                post=models.postModel.objects.get(author=request.user, ulink=p)
                postform = forms.CreatePost(instance=post)
                return render(request, 'posts/WorkOnPost.html', {'postform':postform, 'title':'Edit Post', 'act':'/posts/edit/'})
            except models.postModel.DoesNotExist:
                return redirect('/posts/'+p)
                
                ##here need to redirect it to post in view mode.
                
        else:raise Http404
    elif request.method=='POST':
        p=request.POST.get('p')
        post = get_object_or_404(models.postModel,author=request.user, ulink=p)
        postform = forms.CreatePost(data=request.POST, files=request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('/user/dashboard/')

