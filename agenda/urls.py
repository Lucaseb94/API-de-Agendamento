from django.urls import path
from agenda.views import AgendamentoDetail, AgendamentoList, relatorio_prestadores, get_horarios


urlpatterns = [
    path('agendamentos/<int:pk>/', AgendamentoDetail.as_view(), name='agendamento_detail'),
    path('agendamentos/', AgendamentoList.as_view(), name='agendamento_list'),
    path('prestadores/', relatorio_prestadores, name='prestadorList'),
    path('horarios/', get_horarios, name='horarios_disponivel'),
]