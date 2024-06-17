from django.http import HttpResponse
from django.shortcuts import render, redirect
from posts import models

def homePage(request):
    published_posts = models.postModel.objects.filter(status='p').order_by("-creation_date")
    
    return render(request, 'homepage.html', {'posts':published_posts})

def about(request):
    return HttpResponse('This is About Page.')

def contact(request):
    return HttpResponse('This is Contact Page...')

def error_404_view(request, exception):
    return render(request, '404.html')