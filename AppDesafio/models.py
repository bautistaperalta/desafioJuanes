from django.db import models

def Datos_personales():
    usuario = models.CharField(max_length=40)
    contraseña = models.IntegerField()

def Datos_registro():
    nombre_completo = models.CharField(max_length=40)
    email = models.DateEmail()
    fechaDeNacimiento = models.DateField()
    contraseña = models.IntegerField()


    