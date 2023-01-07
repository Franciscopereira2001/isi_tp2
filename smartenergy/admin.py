## @package admin
#  Permite mapear os modelos criados nesta aplicacao / pasta (Devices, log), e mostrar no django admin
# 
from django.contrib import admin

# Register your models here.
from .models import *

# Registar Device
@admin.register(Device)
# Dizer que campos devem aparecer
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('mac_address','coordinatex','coordinatey','created','group')
    
# Registar administrador
@admin.register(Log)
# Dizer que campos devem aparecer
class LogAdmin(admin.ModelAdmin):
    list_display = ('device','created','ip_address','valled','stateled', 'valldr', 'valldrnew', 'valpir','statepir')