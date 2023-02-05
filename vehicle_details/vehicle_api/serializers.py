from rest_framework import serializers
from .models import NewVehicle

class NewVehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewVehicle
        fields = ('id', 'make', 'model', 'year', 'price')