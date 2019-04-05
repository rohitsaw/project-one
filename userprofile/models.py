from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.conf import settings


class Myuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    dob = models.DateField(max_length=8, blank=True, auto_now_add=True)
    bio = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to="userprofile/profile_image/", blank=True)
    qualification = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.user} {self.email}"
