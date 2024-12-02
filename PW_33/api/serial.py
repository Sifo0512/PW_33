from rest_framework import serializers
from .models import Equipo

class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id','nombre','fundacion','apodo','estadio']
