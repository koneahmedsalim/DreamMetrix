from django.db import models

from classes.models import Class
from user.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='msg_received')
    to_class = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True, related_name='all_msg')
    to_parent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='parent_msg')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.content[20]
