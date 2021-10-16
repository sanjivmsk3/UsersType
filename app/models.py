from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile', null=True,blank=True)
    place = models.CharField(max_length=200, null=True,blank=True)
    city = models.CharField(max_length=200, null=True,blank=True)
    state = models.CharField(max_length=200, null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)


class Categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    summary = models.TextField()
    content = models.TextField()
    CHOICE =(("DRAFT","ADD-TO-DRAFT"), ("PUBLIC","ADD-TO-PUBLIC"))
    draft = models.CharField(max_length=30,choices=CHOICE)