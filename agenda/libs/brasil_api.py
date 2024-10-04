import requests
from datetime import date
from django.conf import settings


def is_feriado(data: date) -> bool:
    # Testes em modo de desenvolvimento
    if settings.TESTING:
        if data.day == 25 and data.month == 12:
            return True
        return False

    ano = data.year
    # Tenta fazer a requisição para a API de feriados
    r = requests.get(f'https://brasilapi.com.br/api/feriados/v1/{ano}')

    # Verifica se a requisição foi bem-sucedida
    if r.status_code != 200:
        raise ValueError('Não foi possível consultar os feriados')

    # Obtém os feriados como uma lista de dicionário
    feriados = r.json()

    # Verifica se a data fornecida coincide com algum feriado
    for feriado in feriados:
        data_feriado_as_str = feriado['date']
        data_feriado = date.fromisoformat(data_feriado_as_str)
        if data == data_feriado:
            return True

    # Caso não seja um feriado, retorna False
    return False

