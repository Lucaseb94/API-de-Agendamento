from django.db import models

# Create your models here.
class Agendamento(models.Model):
    dataHorario = models.DateTimeField()
    nomeCliente = models.CharField(max_length=200)
    emailCliente = models.EmailField()
    telefoneCliente = models.CharField(max_length=20)