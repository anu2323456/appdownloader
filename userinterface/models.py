from django.db import models

# Create your models here.
class appuser(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    profile=models.TextField()


    def __str__(self):
        return self.name
    

class Tasks(models.Model):
    user=models.ForeignKey(appuser,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    apppoint=models.IntegerField()
    image=models.ImageField()

    def __str__(self):
        return self.name


