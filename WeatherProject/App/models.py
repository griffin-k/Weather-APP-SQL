from django.db import models
from django.utils import timezone

class UserLogin(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    dateTime = models.DateTimeField(default=timezone.now)

class History(models.Model):
    city = models.CharField(max_length=50)
    dateTime = models.DateTimeField(default=timezone.now)

class JoinThis(models.Model):
    name = models.CharField(max_length=255)
    userEmail = models.EmailField(max_length=255)
    cityName = models.CharField(max_length=50)
    dateTime = models.DateTimeField(default=timezone.now)
    
    
