from django.http import HttpResponse
from django.shortcuts import render, redirect


def homePage(request):
    return render(request, 'layout.html')

def about(request):
    return HttpResponse('This is About Page.')

def contact(request):
    return HttpResponse('This is Contact Page...')

def error_404_view(request, exception):
    return render(request, '404.html')