## @package models
#  Ficheiro onde estao definidas as tabelas / modelos, Device e log
# 

from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
# Tabela device
class Device(models.Model):
    # Chave estrangeira para um grupo do Django
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # Campo que guarda automicatimente a data quando um registo for criado
    created = models.DateTimeField(auto_now_add=True)
    # Campo que guarda o MAC
    mac_address = models.CharField(max_length=30)
    # Campo das coordenadas x
    coordinatex = models.CharField(max_length=30)
    # Campo das coordenadas y
    coordinatey = models.CharField(max_length=30)
    
    # Mostra a referencia a um registo, apenas com o mac (usada no django admin)
    def __str__(self):
        return self.mac_address
    
# Tabela Log
class Log(models.Model):
    # Chave estrangeira para um Device. Um log tem um device, e um device varios logs
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    # Campo que guarda automicatimente a data quando um registo for criado
    created = models.DateTimeField(auto_now_add=True)
    # IP
    ip_address = models.CharField(max_length=30)
    # Valor led
    valled = models.IntegerField()
    # Estado led
    stateled = models.IntegerField()
    # Valor enviado pelo poste
    valldr = models.IntegerField()
    # Valor enviado pelo poste
    valldrnew = models.IntegerField()
    # Valor enviado pelo poste
    valpir = models.IntegerField()
    # Valor enviado pelo poste
    statepir = models.IntegerField()
    
    def __str__(self):
        return self.ip_address