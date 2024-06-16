from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.postModel
        fields= ['title', 'content', 'image', 'status']