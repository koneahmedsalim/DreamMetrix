
from django.contrib.auth import authenticate
from rest_framework import generics, mixins, status, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, HTMLFormRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from student.models import StudentProfile
from teacher.models import TeacherProfile
from user.models import User
from user.serializers import UserSerializer, TeacherProfileSerializer, StudentProfileSerializer


class StudentCreate(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    serializer_class = UserSerializer

    queryset = User.objects.all()
    renderer_classes = [JSONRenderer, HTMLFormRenderer]

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('user.add_student'):
            raise PermissionDenied("You dont have permission to add student.")
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save()
        profile = StudentProfile.objects.get(user=user)
        profile.save()


    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, pk)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TeacherCreate(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    renderer_classes = [JSONRenderer, HTMLFormRenderer]

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('user.add_student'):
            raise PermissionDenied("You dont have permission to add student.")
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save()
        profile = TeacherProfile.objects.get(user=user)
        profile.save()


    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, pk)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentProfileUpdate(mixins.UpdateModelMixin, mixins.DestroyModelMixin, APIView):

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentProfileSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TeacherProfileUpdate(mixins.UpdateModelMixin, APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = TeacherProfileSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UserLogin(APIView):
    def post(self, request, **kwargs):
        data = request.data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(username=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'email': user.email, 'token': token.key}, status=status.HTTP_200_OK)
        return Response({"message": "wrong credentials"}, status=status.HTTP_400_BAD_REQUEST)
