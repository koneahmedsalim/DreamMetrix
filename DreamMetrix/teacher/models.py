from django.db import models

from user.models import User


# Create your models here.


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    photo = models.ImageField(upload_to='Profile/teacher/photo', blank=True)
