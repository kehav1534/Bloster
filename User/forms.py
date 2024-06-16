from django import forms
from . import models

class UserProfileForm(forms.ModelForm):
    class Meta:
        model= models.UserProfile
        fields = ['pic', 'firstname', 'lastname', 'bio', 'email']