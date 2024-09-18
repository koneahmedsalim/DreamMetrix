from django.http import JsonResponse
from django.urls import path

import classes
from user.views import login_view, student_create, teacher_create, student_profile_view, teacher_profile_view
from classes.views import classes_view



def test(request):
    return JsonResponse({"message": "test"}, safe=False)

urlpatterns = [
    path("", test, name="home"),
    path('login/', login_view, name='login'),

    # user related endpoint
    path('create-student/', student_create, name='create-student'),
    path('create-teacher/', teacher_create, name='create-teacher'),

    ### class related endpoints
    path('teacher-classes/', classes_view, name='teacher-classes'),
    path("update-class/", classes_view, name='update-class'),
    path("delete-class/", classes_view, name='delete-class'),
    path("create-class/", classes_view, name='create-class'),

    ## profile related endpoint
    path("student-profile-update/", student_profile_view, name='student-profile-update'),
    path("teacher-profile-update/", teacher_profile_view, name='teacher-profile-update'),

    # Assignment related endpoints

]


