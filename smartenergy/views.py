
## @package views
#  Ficheiro onde estao definidas todas as views, ou seja, as funcoes que sao executadas a cada pedido htttp
from .models import Device, Log
from .serializers import DeviceSerializer, LogSerializer
from rest_framework.response import Response
from rest_framework import permissions

# ViewSets define the view behavior.
# A view dos devices
class DeviceViewSet(viewsets.ModelViewSet):
    # Fazer a query e retirar toos os objectivos
    queryset = Device.objects.all()
    # Indicar quem e o serializador, isto e, o validador do pedido
    serializer_class = DeviceSerializer
    # Apenas utilizadores autenticados podem usar este serviço
    permission_classes = [permissions.IsAuthenticated]
    
    
    # Servico post para criar um novo dispositivo
    def create(self, request):
        r_status = status.HTTP_200_OK
        descritpion = ""
        try:
            # Envia para o Serializer o pedido. Se verdadeiro, grava o Device na base de dados
            x = DeviceSerializer(data = self.request.data)
            if x.is_valid() == True:
                # Gravar na base de dados
                x.save()
            else:
                raise Exception("Not valid")
        except Exception as e:
            r_status = status.HTTP_400_BAD_REQUEST
            descritpion = 'Error: ' + str(e)
        
        # Responder ao pedido http
        return Response({'detail': descritpion},status=r_status)
            
        

    # ViewSets define the view behavior.
    # A view dos devices

class LogViewSet(viewsets.ModelViewSet):
    # Fazer a query e retirar todos os logs
    queryset = Log.objects.all()
    # Mapear o serializador
    serializer_class = LogSerializer
    # Apenas utilizadores autenticados podem usar este serviço
    permission_classes = [permissions.IsAuthenticated]
    
    # Servico post para criar um log
    def create(self, request):
        r_status = status.HTTP_200_OK
        descritpion = ""
        try:
            # Envia para o Serializer o pedido. Se verdadeiro, grava o Log na base de dados
            x = LogSerializer(data = self.request.data)
            if x.is_valid() == True:
                # Grava na base de dados
                x.save()
            else:
                raise Exception("Not valid")
        except Exception as e:
            r_status = status.HTTP_400_BAD_REQUEST
            descritpion = 'Error: ' + str(e)
        
        return Response({'detail': descritpion},status=r_status)