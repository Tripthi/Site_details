from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Site(models.Model):

    site_name=models.CharField(max_length=250)

    rd_name=models.CharField(max_length=250)

    rd_version=models.CharField(max_length=250)

    def __str__(self):

        return self.site_name

    # def __str__(self):
    #     return self.rd_name
    #
    # def __str__(self):
    #     return self.rd_version

