from django.db import models

# Create your models here

class User(models.Model):
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)

    def __str__(self):
        return self.name
