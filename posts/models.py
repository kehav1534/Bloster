from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import hashlib, time

class postModel(models.Model):
    status_option = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, default=None, editable=False)
    title = models.CharField(verbose_name='Post Title', blank=False, max_length=150)
    content = models.TextField(verbose_name='Post Content', blank=False)
    image = models.ImageField(blank=True, default='blank.png')
    creation_date = models.DateTimeField(editable=False , blank=True)
    modify_date = models.DateTimeField(editable=False, blank=True)
    ulink = models.SlugField(verbose_name='Unique Link ID',editable=False, unique=True, blank=False)
    status = models.CharField(max_length=1,choices=status_option,default='d', blank=False)
    
    def __str__(self):
        return self.ulink
    
    def create_unique_strings(self, input_string: str) -> str:
        hash_object = hashlib.sha256()
        hash_object.update(input_string.encode('utf-8'))
        unique_string = hash_object.hexdigest()
        return unique_string+f'{time.time()}'.replace('.','')

    def save(self, *args, **kwargs):
        if not self.ulink:
            self.ulink = self.create_unique_strings(self.title)
            self.creation_date= timezone.now()
        self.modify_date = timezone.now()
        super().save(*args, **kwargs)
