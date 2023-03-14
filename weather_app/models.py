from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
class location(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.location_name