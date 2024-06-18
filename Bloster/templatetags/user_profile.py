from django import template
from ...User import models
from django.shortcuts import get_object_or_404
register = template.Library()

@register.tag
def get_user_profile(user):
    profile_pic = get_object_or_404(models.UserProfile, user=user)

    if profile_pic:
        return '/media'+profile_pic.pic
    else: return '/media/blank.png'
