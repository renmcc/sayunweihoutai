from django.db import models

# Create your models here.

class service(models.Model):
    hostname = models.CharField(max_length=50,blank=True)
    inner_ip = models.GenericIPAddressField(unique=True, null=False)

    def __str__(self):
        return self.inner_ip
