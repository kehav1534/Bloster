from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import time
class UserProfile(models.Model):
    pic = models.ImageField(verbose_name='Profile Picture', default='blank.png', blank=True)
    firstname = models.CharField(max_length=35, blank=True, verbose_name='First Name')
    lastname = models.CharField(max_length=35, blank=True, verbose_name='Last Name')
    bio = models.TextField(max_length=200, blank=True, verbose_name='Bio')
    uuid = models.SlugField(unique=True, editable=False, verbose_name='Unique User Id', blank=True)
    email = models.EmailField(verbose_name='Email ID', blank=True, max_length=254)
    user= models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    def __str__(self):
        return self.uuid
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = slugify(self.user.username)+f'-{time.time()}'.replace('.', '-')
        super().save(*args, **kwargs)