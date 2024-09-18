from rest_framework import serializers

from student.models import StudentProfile
from teacher.models import TeacherProfile
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
        write_only_fields = ('password', 'last_login', 'is_superuser', 'is_staff')

    def create(self, validated_data):
        pass
        # todo or not



class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ["photo"]
        write_only_fields = ('photo',)


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ["photo"]
        write_only_fields = ('photo',)


