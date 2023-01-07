## @package serializers
#  Ficheiro onde estao definidos os serializadores / validadores dos logs e devices

from rest_framework import serializers
from .models import Device, Log

# Serializers define the API representation.
# Serializador do device. 
class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    
    
    class Meta:
        # Ligacao ao modelo Device da base dados
        model = Device
        # Mapeia os seguintes campos da tabela Device
        fields = ['created','mac_address', 'coordinatex' , 'coordinatey','group']
        
    # Usado para criar um novo device, em que valida posteriormente
    def create(self, validated_data):
        return Device.objects.create(**validated_data)

# Serializers define the API representation.
# Serializador do Log. 
class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Ligacao ao modelo Log da base dados
        model = Log
        # Mapeia os seguintes campos da tabela Log
        fields = [
                  'device',
                  'created', 
                  'ip_address', 
                  'valled', 
                  'stateled', 
                  'valldr', 
                  'valldrnew',
                  'valpir',
                  'statepir'
                  ]
    # Usado para criar um novo Log, em que valida posteriormente
    def create(self, validated_data):
        return Log.objects.create(**validated_data)