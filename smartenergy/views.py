from rest_framework import viewsets
from .models import Device, Log
from .serializers import DeviceSerializer, LogSerializer

# ViewSets define the view behavior.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    # ViewSets define the view behavior.
class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer