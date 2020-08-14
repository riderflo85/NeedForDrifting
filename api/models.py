from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAC(User):
    token = models.CharField(
        max_length=24
    )