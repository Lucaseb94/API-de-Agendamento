from django.shortcuts import render, get_object_or_404
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response


# Create your views here.
@csrf_exempt
@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def agendamento_detail(request, id):
    if request.method == "GET":
        obj = get_object_or_404(Agendamento, id=id)
        print(obj)
        serializer = AgendamentoSerializer(obj)
        print(serializer)
        return JsonResponse(serializer.data)
    
    if request.method == "PATCH":
        obj = get_object_or_404(Agendamento, id=id)
        request.data
        serializer = AgendamentoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
           
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    if request.method =="DELETE":
        obj = get_object_or_404(Agendamento,id=id)
        obj.delete()
        return Response(status=204)


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
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)