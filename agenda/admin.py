from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nomeCliente', 'dataHorario', 'emailCliente', 'telefoneCliente')
