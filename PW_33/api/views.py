from django.shortcuts import render

# Create your views here.
from .models import Equipo
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import EquipoSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().order_by('-fundacion')
    serializer_class = EquipoSerializer
