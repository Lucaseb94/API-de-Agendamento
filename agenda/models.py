from django.db import models

# Create your models here.
class Agendamento(models.Model):
    prestador = models.ForeignKey('auth.User', related_name='agendamentos', on_delete=models.CASCADE)

    dataHorario = models.DateTimeField()
    nomeCliente = models.CharField(max_length=200)
    emailCliente = models.EmailField()
    telefoneCliente = models.CharField(max_length=20)

    class Meta:
        app_label = 'agenda'