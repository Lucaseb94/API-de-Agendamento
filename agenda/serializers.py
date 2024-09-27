from rest_framework import serializers

class AgendamentoSerializer(serializers.Serializer):
    dataHorario = serializers.DateTimeField()
    nomeCliente = serializers.CharField(max_length=200)
    emailCliente = serializers.EmailField()
    telefoneCliente = serializers.CharField(max_length=200)