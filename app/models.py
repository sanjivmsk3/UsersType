from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile', null=True,blank=True)
    place = models.CharField(max_length=200, null=True,blank=True)
    city = models.CharField(max_length=200, null=True,blank=True)
    state = models.CharField(max_length=200, null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    allow = models.BooleanField(default=False)


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


class TimeSchedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time) + "-" + str(self.end_time)


class BookAppointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    CHOICE =(("Bariatrics","Bariatrics"), ("Cardiology","Cardiology"), ("Dermatology","Dermatology"), ("General surgery","General surgery"))
    speciality = models.CharField(max_length=30,choices=CHOICE)
    time = models.ForeignKey(TimeSchedule, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)