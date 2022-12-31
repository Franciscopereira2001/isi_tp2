from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from .serializers import GroupSerializer, UserSerializer, LoginSerializer
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

# ViewSets define the view behavior.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    # ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'status': 'Ok'}, status=status.HTTP_202_ACCEPTED)
    
class LogoutView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        logout(request)
        return Response({'status': 'Ok'}, status=status.HTTP_202_ACCEPTED)