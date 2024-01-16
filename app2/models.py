from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User,related_name='userprofile',on_delete=models.CASCADE)



class  student(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()

    def __str__(self):
        return self.name 