from django.db import models

from user.models import User


# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes')
    students = models.ManyToManyField(User, related_name='student_class')
    timetable = models.JSONField(default=dict)


    def __str__(self):
        return self.name



class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='Assignment/assignment', blank=True)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    dateline = models.DateTimeField()

    def __str__(self):
        return self.title





class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='Assignment/submission', blank=True)
    content = models.TextField(blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField(blank=True, null=True)





class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='Quiz/quiz')
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    dateline = models.DateTimeField()

    def __str__(self):
        return self.title



class QuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    file = models.FileField(upload_to='Quiz/submission')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField()
