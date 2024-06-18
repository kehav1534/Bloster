from django import template
from ..models import UserProfile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
register = template.Library()

@register.simple_tag
def get_user_profile(user):
    profile_pic = get_object_or_404(UserProfile, user=user)
    if profile_pic.pic:
        return f'/media/{profile_pic.pic}'
    else: return '/media/blank-user.png'
