from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewVehicleSerializer
from .models import NewVehicle

# Create your views here.

class NewVehicleViewSet(viewsets.ModelViewSet):
    queryset = NewVehicle.objects.all().order_by('id')
    serializer_class = NewVehicleSerializer
