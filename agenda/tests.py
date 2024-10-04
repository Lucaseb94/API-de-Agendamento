from rest_framework.test import APITestCase
import json
from agenda.models import Agendamento
from datetime import datetime
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class TestListegemAgendamentos(APITestCase):

    def setUp(self):
        # Cria um superusuário
        self.user = User.objects.create_superuser(
            username='miranda', 
            email='lmirandaebb@gmail.com', 
            password='123'
        )

    def test_listagem_vazia(self):
        self.assertTrue(self.client.login(username='miranda', password='123'))
        

        response = self.client.get('/api/agendamentos/?username=miranda')
        data = response.json()  # Obtém os dados da resposta como JSON
        self.assertEqual(data, [])


    def test_listagem_agendamentos_criados(self):
        self.assertTrue(self.client.login(username='miranda', password='123'))

        agendamento_serializado = {
            "id": 1,
            "dataHorario": '2025-03-01T00:00:00Z',
            "nomeCliente": "miranda",
            "emailCliente": 'lmiranda@gmail.com',
            "telefoneCliente": '+55123123123',
            "prestador": 'miranda'
        }

        response = self.client.get("/api/agendamentos/?username=lmiranda")
        self.assertEqual(response.status_code, 200)
        print(response)
        data = json.loads(response.content)
        print(data)
        
        # Verifica se o primeiro agendamento da lista é o esperado
        self.assertEqual(data, [])

class TestCriacaoAgendamento(APITestCase):

    def test_cria_agendamento(self):
        logintest = User.objects.create_user(email='lmiranda@gmail.com', username='miranda', password='123')
        self.client.login(username='miranda', password='123')
        
        agendamento_data = {
            'dataHorario': '2025-03-15T10:00:00Z',  # Verifique se esse horário está disponível
            'prestador': 'miranda',  # Use o ID do prestador criado
            'nomeCliente': 'Lucas',
            'emailCliente': 'lmiranda@gmail.com',
            'telefoneCliente': '+55123123123',
        }

        response = self.client.post('/api/agendamentos/?username=miranda', agendamento_data)
        data = json.loads(response.content)

        # Verifique o código de status da resposta
        self.assertEqual(response.status_code, 201)  # 201 Created

        # Compare os dados retornados com os dados do agendamento
        self.assertDictEqual(data, {
            'dataHorario': '2025-03-15T10:00:00Z',
            'prestador': 'miranda',
            'nomeCliente': 'Lucas',
            'emailCliente': 'lmiranda@gmail.com',
            'telefoneCliente': '+55123123123',
            'id': 1,  # Ajuste para o ID correto se necessário
        })

    def test_request_retorna_400(self):
        agendamento_data = {
            "id": 1,
            "dataHorario": '2025-03',
            "nomeCliente": "Lucas",
            "emailCliente": 'lmiranda@gmail.com',
            "telefoneCliente": '+55123123123',
        }
        response = self.client.post('/api/agendamentos/',agendamento_data)
        print(response)
        self.assertEqual(response.status_code, 400)


class TesteGetHorarios(APITestCase):
    def test_quando_e_feriado(self):
        response = self.client.get('/api/horarios/?data=2022-12-25')
        self.assertEqual(response.data, [])


def test_data_e_dia_comum_retorna_lista(self):
    response = self.client.get('/api/horarios/?data=2022-10-03')

    # Verifica se a resposta não está vazia
    self.assertNotEqual(response.data, [])

    # Converte o valor da API de string para datetime
    primeiro_horario = datetime.fromisoformat(response.data[0])
    ultimo_horario = datetime.fromisoformat(response.data[-1])

    # Compara os valores esperados
    self.assertEqual(primeiro_horario, datetime(2022, 10, 3, 11, 30, tzinfo=timezone.utc))
    self.assertEqual(ultimo_horario, datetime(2022, 10, 3, 10, 0, tzinfo=timezone.utc))
