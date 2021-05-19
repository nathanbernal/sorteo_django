from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer, GroupSerializer, UsuarioSerializer
from .models import Usuario

class ActivacionViewSet(viewsets.ModelViewSet):
    """
    Endpoint usuarios.
    """
    queryset = Usuario.objects.none()
    serializer_class = UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Endpoint usuarios.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
