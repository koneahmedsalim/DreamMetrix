from django.db import models

from user.models import User


# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Profile/student/photo/', blank=True)



class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    children = models.ManyToManyField(User, related_name='parents', blank=True)


