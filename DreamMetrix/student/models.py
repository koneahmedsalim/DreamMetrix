from django.db import models
from user.models import User

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO: Add other fields as needed


class ParentProfile(models.Model):
    user = models.OneToOneField(User, related_name='student_parent_profile', on_delete=models.CASCADE)
    children = models.ManyToManyField(User, related_name='student_parent_children')