from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, 
        related_name='posts', 
        on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.TextField()

    def __str__(self):
        return self.title
