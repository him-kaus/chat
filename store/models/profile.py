from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import datetime


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(default='',max_length=100 )
    last_name = models.CharField(default='',max_length=100)
    email = models.EmailField(max_length=100, default='')
    date_birth = models.DateField(default=datetime.datetime.now())
    bio = models.TextField(default='')
    image = models.ImageField(upload_to='profile_image', blank=True)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)