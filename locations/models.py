from django.db import models


class company(models.Model):
    name = models.CharField(max_length=50, null=True)
    postal_address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(default='Pakistan', max_length=50, null=True)
    lat = models.CharField(max_length=50, null=True)
    long = models.CharField(max_length=50, null=True)
    google_pin = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)
