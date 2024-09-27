from django.shortcuts import render, get_object_or_404
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
@api_view(http_method_names=['GET', 'PUT'])
def agendamento_detail(request, id):
    if request.method == "GET":
        obj = get_object_or_404(Agendamento, id=id)
        print(obj)
        serializer = AgendamentoSerializer(obj)
        print(serializer)
        return JsonResponse(serializer.data)
    
    if request.method == "PUT":
        obj = get_object_or_404(Agendamento, id=id)
        request.data
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            v_data = serializer.validated_data
            obj.dataHorario = v_data.get("dataHorario", obj.dataHorario)
            obj.nomeCliente = v_data.get("nomeCliente", obj.nomeCliente)
            obj.emailCliente = v_data.get("emailCliente", obj.emailCliente)
            obj.telefoneCliente = v_data.get("telefoneCliente", obj.telefoneCliente)
            obj.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)




@api_view(http_method_names=["GET", "POST"])
def agendamento_list(request):
    if request.method == "GET":
        # Buscar todos os agendamentos
        qs = Agendamento.objects.all()
        # Serializar os dados
        serializer = AgendamentoSerializer(qs, many=True)
        # Retornar resposta em formato JSON
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST":
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            Agendamento.objects.create(
                dataHorario=validated_data["dataHorario"],
                nomeCliente=validated_data["nomeCliente"],
                emailCliente=validated_data["emailCliente"],
                telefoneCliente=validated_data["telefoneCliente"]
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)