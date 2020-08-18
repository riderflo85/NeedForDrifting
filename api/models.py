from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAC(AbstractUser):
    token = models.CharField(
        max_length=24,
        null=True,
        unique=True,
    )