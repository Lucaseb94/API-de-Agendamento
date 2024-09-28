from rest_framework import serializers
from agenda.models import Agendamento
from django.utils import timezone


class AgendamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento
        fields = ['id', 'dataHorario', 'nomeCliente', 'emailCliente', 'telefoneCliente']

    def validate_dataHorario(self, value):
        """
        verifica se o horario do agendamento esta no passado
        """
        if value < timezone.now():
            raise serializers.ValidationError('Data não disponivel para agendamento')
        return value

    # object level

    def validate(self, attrs):
        """
        Se é um email brasileiro tem que estar associado a um email brasileiro
        """
        telefoneCliente = attrs.get('telefoneCliente',"")
        emailCliente = attrs.get('emailCliente', "")

        if emailCliente.endswith(".br") and telefoneCliente.startswith('+') and not telefoneCliente.startswith('+55'):
            raise serializers.ValidationError('Email deve esta associado a um numero Brasileiro')
        return attrs


