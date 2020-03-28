from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class Task(models.Model):
    content = models.CharField(max_length=64, null=False, blank=False)
    userTag = models.IntegerField(null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
