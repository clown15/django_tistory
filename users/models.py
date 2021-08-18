from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=256, uniqe=True)
    username = models.CharField(max_length=32)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    def __str__(self):
        return "<%d %s>" % (self.pk,self.email)
