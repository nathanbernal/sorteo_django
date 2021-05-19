from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario
import logging
from api.functions import send_user_mail

logger = logging.getLogger(__name__)

class ActivacionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['contrasena']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Usuario
        fields = ['nombres', 'paterno', 'materno', 'email']

    def validate(self, data):
        usuariosCantidad=0
        if "@" in data["email"]:
            usuariosCantidad = Usuario.objects.filter(email=data["email"]).count()
        else:
            raise serializers.ValidationError("El formato del email introducido es incorrecto.")
        if usuariosCantidad>0:
            raise serializers.ValidationError("El email registrado ya se encuentra asociado a otro usuario.")

        send_user_mail(data["email"])

        return data
