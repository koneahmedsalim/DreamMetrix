from rest_framework import serializers

from classes.models import Class, Assignment, AssignmentSubmission, Quiz, QuizSubmission


class ClassSerializer(serializers.Serializer):
    class Meta:
        model = Class
        fields = '__all__'



class AssignmentSerializer(serializers.Serializer):
    class Meta:
        model = Assignment
        fields = "__all__"



class AssignmentSubmissionSerializer(serializers.Serializer):
    class Meta:
        model = AssignmentSubmission(serializers.Serializer)
        fields = ["assignment", "file", "content", "student"]


class QuizSerializer(serializers.Serializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class QuizSubmissionSerializer(serializers.Serializer):
    class Meta:
        model = QuizSubmission(serializers.Serializer)
        fields = ["quiz", "file", "content", "student"]

