# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from .choices import TYPE_CHOICES

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    about_me = models.TextField(default='',blank=True)
    type = models.CharField(choices=TYPE_CHOICES,max_length=12)

    def get_url(self):
        try:
            return self.url
        except IOError:
            return None

    def __str__(self):
        return self.user.username



class UploadReport(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=60,blank=False)
    description = models.TextField(blank=True)
    Doctor = models.BooleanField(default=False)
    Nurse = models.BooleanField(default=False)
    Receptionist = models.BooleanField(default=False)
    report_file = models.FileField()

    def __str__(self):
        return self.title
