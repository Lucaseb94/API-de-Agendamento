from django.shortcuts import render, get_object_or_404
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer, PrestadorSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics, permissions
from django.contrib.auth.models import User
from datetime import datetime, date
from agenda.utils import get_horarios_disponiveis
import csv
from django.http import HttpResponse


class IsOwnerOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        username = request.query_params.get('username', None)
        if request.user.username == username:
            return True
        return False


class IsPrestador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.prestador == request.user:
            return True
        return False

class Isadm(permissions.BasePermission):
    """
    Permissão personalizada para garantir que apenas superusuários possam acessar.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    
class IsSuperUser(permissions.BasePermission):
    """
    Permissão personalizada para garantir que apenas superusuários possam acessar.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
        


class AgendamentoList(generics.ListCreateAPIView):
    serializer_class = AgendamentoSerializer
    permission_classes = [IsOwnerOrCreateOnly | IsSuperUser]

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        return Agendamento.objects.filter(prestador__username=username)
    

class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView):  
    permission_class = [IsPrestador]
    queryset = Agendamento.objects.all()
    serializerClass = AgendamentoSerializer



class PrestadorList(generics.ListAPIView):
    permission_class = [Isadm]
    serializer_class = PrestadorSerializer
    queryset = User.objects.all()


@api_view(http_method_names=["GET"])
@permission_classes([permissions.IsAdminUser])
def relatorio_prestadores(request):
    formato = request.query_params.get("formato")
    prestadores = User.objects.all()
    serializer = PrestadorSerializer(prestadores, many=True)

    if formato == "csv":
        data_hoje = date.today()
        response = HttpResponse(
            content_type='text/csv',
            headders={'Content-Disposition' f'attachment; filename="relatorio_{data_hoje}.csv"'})
        
    writer = csv.writer(response)

    for prestador in serializer.data:
        agendamentos = prestador['agendamentos']
        for agendamento in agendamentos:
            writer.writerow([
                agendamento['prestador'],
                agendamento['nomeCliente'],
                agendamento['emailCliente'],
                agendamento['telefoneCliente']
            ])
        return response
    else:
        return Response(serializer.data)




@api_view(http_method_names=['GET'])
def get_horarios(request):
    data = request.query_params.get('data')
    
    if not data:
        data = datetime.now().date()
    else:
        try:
            data = datetime.fromisoformat(data).date()
        except ValueError:
            return Response({'error': 'Formato de data inválido. Use o formato YYYY-MM-DD.'}, status=400)


    horarios_disponiveis = get_horarios_disponiveis(data)
    horarios_list = [horario.isoformat() for horario in horarios_disponiveis]
    
    return Response(horarios_list)