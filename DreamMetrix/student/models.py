from django.db import models

from user.models import User


# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODOD



class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    children = models.ManyToManyField(User)


    