from django.db import models

from user.models import User


# Create your models here.

from django.db import models
from user.models import User

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)   
    biography = models.TextField(blank=True, null=True)
    subjects_taught = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='teacher_profiles/', blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   

class ParentProfile(models.Model):
    user = models.OneToOneField(User, related_name='teacher_parent_profile', on_delete=models.CASCADE)
    children = models.ManyToManyField(User, related_name='teacher_parent_children')
    def __str__(self):
        # Afficher le nom complet du professeur pour une meilleure lisibilité
        return f"{self.first_name} {self.last_name}"