## @package urls
#  Contem o ficheiro de com as views a serem procedadas a cada pedido
# 

from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from .serializers import GroupSerializer, UserSerializer, LoginSerializer
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

# ViewSets define the view behavior.
# Permitir aceder a tabela groups via Rest Framework
class GroupViewSet(viewsets.ModelViewSet):
    # Query sera obter todos os grupos
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # So utilizadores autenticados podem utilizar o servico
    permission_classes = [permissions.IsAuthenticated]

    # ViewSets define the view behavior.
# Permitir aceder a tabela Users via Rest Framework
class UserViewSet(viewsets.ModelViewSet):
    # Query sera obter todos os users
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # So utilizadores autenticados podem utilizar o servico
    permission_classes = [permissions.IsAuthenticated]
    
# Permitir fazer autenticacao via Rest Framework
class LoginView(views.APIView):
    # Todos os nao autenticados podem tentar utilizar este serviço
    permission_classes = (permissions.AllowAny,)

    # Via http post:
    def post(self, request, format=None):
        # Deseriaziar o pedido
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        # Ver se pedido e valido
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # Fazer login
        login(request, user)
        return Response({'status': 'Ok'}, status=status.HTTP_202_ACCEPTED)
    
# Permitir fazer logout via Rest Framework
class LogoutView(views.APIView):
    #  O pedido tem que vir de um utilizador autenticado
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        # Dizer ao django que o utilizador nao esta mais logado
        logout(request)
        return Response({'status': 'Ok'}, status=status.HTTP_202_ACCEPTED)