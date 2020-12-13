from django.db import models


class company(models.Model):
    name = models.CharField(max_length=50, null=True)
    addr = models.CharField(max_length=200, null=True)
    telephone_number = models.CharField(max_length=20, null=True)
    sector = models.CharField(max_length=50, null=True)
    business_description = models.CharField(max_length=200, null=True)
    logo = models.FileField(null=True)
    website = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)
