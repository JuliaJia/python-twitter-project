from django.contrib.auth.models import User,Group
from rest_framework import viewsets,permissions
from accounts.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.contrib.auth import (
    authenticate as django_authenticate,
    login as django_login,
    logout as django_logout,
)
from accounts.api.serializers import SignupSerializer,LoginSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer
    @action(methods=["GET"],detail=False)
    def login_status(self,request):
        data = {'has_logged_in': request.user.is_authenticated}
        if request.user.is_authenticated:
            data['user'] = UserSerializer(request.user,context={'request': request}).data
        return Response(data)
    @action(methods=['POST'],detail=False)
    def signup(self,request):
        serializer = SignupSerializer(data=request.data,context={'request': request})
        if not serializer.is_valid():
            return Response({
                "success": False,
                "message": "Please check input",
                "errors": serializer.errors,
            },status=400)

        user = serializer.save()
        django_login(request,user)
        return Response({
            'success': True,
            'user': UserSerializer(user,context={'request': request}).data,
        }, status=201)

    @action(methods=["POST"],detail=False)
    def login(self,request):
        serializer = LoginSerializer(data=request.data,context={'request': request})
        if not serializer.is_valid():
            return Response({
                "success": False,
                "message": "Please check input",
                "errors": serializer.errors,
            },status=400)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = django_authenticate(username=username,password=password)
        if not user or user.is_anonymous:
            return Response({
                "success": False,
                "message": "username and password does not match"
            },status=400)

        django_login(request,user)
        return Response({
            "success": True,
            "user": UserSerializer(instance=user,context={'request': request}).data
        })



    @action(methods=['POST'],detail=False)
    def logout(self,request):
        django_logout(request)
        return Response({"success": True})

