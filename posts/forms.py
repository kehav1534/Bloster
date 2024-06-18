from django import forms
from . import models
from django.forms import Textarea
class CreatePost(forms.ModelForm):
    class Meta:
        model = models.postModel
        fields= ['title', 'content', 'image', 'status']
        widgets = {
            'title' : forms.TextInput(attrs={"style":"width:40rem;border-radius:20px;padding:20px;font-size:1.5rem;","placeholder":"Title..."}),
            'content': Textarea(attrs={"style":"width:40rem;border-radius:20px;padding:20px;font-size:1rem;","placeholder":"Content..."}),
            
        }