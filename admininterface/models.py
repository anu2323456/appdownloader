from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Appcollections(models.Model):
    name=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    subcategory=models.CharField(max_length=250)
    link=models.CharField(max_length=250)
    image=models.ImageField()
    points=models.IntegerField()

    def __str__(self):
        return self.name