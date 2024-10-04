from rest_framework import serializers
from agenda.models import Agendamento
from django.utils import timezone
from django.contrib.auth.models import User
from agenda.utils import get_horarios_disponiveis



class AgendamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento
        fields = '__all__'

    
    prestador = serializers.CharField()
    def validate_prestador(self, value):
        try:
            prestador_obj = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('Usuario não existe!')
        return prestador_obj

    def validate_dataHorario(self, value):
        """
        Verifica se o horário do agendamento está no passado ou não está disponível.
        """
        # Verifica se a data/hora está no passado
        if value < timezone.now():
            raise serializers.ValidationError('Data não disponível para agendamento.')

        # Verifica se o horário está disponível na lista de horários disponíveis
        if value not in get_horarios_disponiveis(value.date()):
            raise serializers.ValidationError('Esse horário não está disponível!!!')
        
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


class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'agendamentos']