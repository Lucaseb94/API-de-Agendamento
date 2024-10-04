from datetime import date, datetime, timezone, timedelta
from agenda.libs import brasil_api
from typing import Iterable
from agenda.models import Agendamento



def get_horarios_disponiveis(data:date) -> Iterable[datetime]:

    if  brasil_api.is_feriado(data):
        return []

    start = datetime(year=data.year, month=data.month, day=data.day, hour=9, minute=0, tzinfo=timezone.utc)
    end = datetime(year=data.year, month=data.month, day=data.day, hour=18, minute=0, tzinfo=timezone.utc)
    delta = timedelta(minutes=30)
    horarios_disponiveis = set()
    while start < end:
        if not Agendamento.objects.filter(dataHorario=start).exists():
            horarios_disponiveis.add(start)
        start = start + delta
        
    return horarios_disponiveis