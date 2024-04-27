from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    about = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} profili"


