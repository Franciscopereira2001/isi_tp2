from rest_framework import viewsets, status
from .models import Device, Log
from .serializers import DeviceSerializer, LogSerializer
from rest_framework.response import Response
from rest_framework import permissions

# ViewSets define the view behavior.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        r_status = status.HTTP_200_OK
        descritpion = ""
        try:
            x = DeviceSerializer(data = self.request.data)
            if x.is_valid() == True:
                x.save()
            else:
                raise Exception("Not valid")
        except Exception as e:
            r_status = status.HTTP_400_BAD_REQUEST
            descritpion = 'Error: ' + str(e)
        
        return Response({'detail': descritpion},status=r_status)
            
        

    # ViewSets define the view behavior.
class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        r_status = status.HTTP_200_OK
        descritpion = ""
        try:
            x = LogSerializer(data = self.request.data)
            if x.is_valid() == True:
                x.save()
            else:
                raise Exception("Not valid")
        except Exception as e:
            r_status = status.HTTP_400_BAD_REQUEST
            descritpion = 'Error: ' + str(e)
        
        return Response({'detail': descritpion},status=r_status)