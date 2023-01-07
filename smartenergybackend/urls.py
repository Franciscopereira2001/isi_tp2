"""smartenergybackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

## @package urls
#  Contem o ficheiro de mapeamento de url.
# 

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet,LoginView, LogoutView
from smartenergy.views import LogViewSet, DeviceViewSet 

# Routers provide an easy way of automatically determining the URL conf.
# O default router e utilizado pela rest framework
router = routers.DefaultRouter()
# <nomesite>/ursers  -> rest framework -> servico users
router.register(r'users', UserViewSet)
# <nomesite>/groups  -> rest framework -> servico groups
router.register(r'groups', GroupViewSet)
# <nomesite>/logs    -> rest framework -> servico logs
router.register(r'logs', LogViewSet)
# <nomesite>/devices -> rest framework -> servico devices
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    # <nomesite>/admin -> Django admin
    path('admin/', admin.site.urls),
    # Rest framework acima
    path('', include(router.urls)),
    # Rest framework Autenticacao via Rest Framework interface
    path('api-auth/', include('rest_framework.urls')),
    # Rest framework Login via servico Rest
    path('api/login', LoginView.as_view()),
    # Rest framework logout via servico Rest
    path('api/logout', LogoutView.as_view()),
]
