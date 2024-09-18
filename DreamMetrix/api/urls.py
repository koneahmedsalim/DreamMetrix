from django.http import JsonResponse
from django.urls import path

import classes
from user.views import login_view, student_create, teacher_create
from classes.views import classes_view



def test(request):
    return JsonResponse({"message": "test"}, safe=False)

urlpatterns = [
path("", test, name="home"),
    path('login/', login_view, name='login'),
    path('create-student/', student_create, name='create-student'),
    path('create-teacher/', teacher_create, name='create-teacher'),
    path('teacher-classes/', classes_view, name='teacher-classes'),
    path("update-class/", classes_view, name='update-class'),
    path("delete-class/", classes_view, name='delete-class'),
    path("create-class/", classes_view, name='create-class'),

]


