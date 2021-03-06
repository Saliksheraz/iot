from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    CNIC = models.CharField(max_length=50, null=True)
    Picture = models.FileField(null=True)

    def __str__(self):
        return str(self.user)
