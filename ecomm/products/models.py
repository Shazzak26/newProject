from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    neme = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name