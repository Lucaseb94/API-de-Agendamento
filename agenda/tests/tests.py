from rest_framework.test import APITestCase
import json
from agenda.models import Agendamento
from datetime import datetime
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from unittest import mock
from agenda.views import IsOwnerOrCreateOnly

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
        # Faz login com o superusuário criado no setUp
        self.assertTrue(self.client.login(username='miranda', password='123'))

        # Cria um agendamento no banco de dados de teste
        Agendamento.objects.create(
            prestador=self.user,  # Use a instância de User criada no setUp
            dataHorario='2024-10-17T17:24:52Z',
            nomeCliente='Lucas Miranda Franca',
            emailCliente='lmirandaeb@gmail.com',
            telefoneCliente='11954125125'
        )

        # Faz a requisição para listar os agendamentos do prestador 'miranda'
        response = self.client.get("/api/agendamentos/?username=miranda")

        # Verifica se o status da resposta é 200
        self.assertEqual(response.status_code, 200)

        # Verifica se há dados na resposta
        data = response.json()
        self.assertTrue(len(data) > 0, "Nenhum agendamento foi retornado.")

        # Dados esperados do agendamento criado
        agendamento_serializado = {
        "id": data[0]['id'],
        "prestador": self.user.id,  
        "dataHorario": "2024-10-17T17:24:52Z",
        "nomeCliente": "Lucas Miranda Franca",
        "emailCliente": "lmirandaeb@gmail.com",
        "telefoneCliente": "11954125125"
        }

        # Verifica se o primeiro agendamento da lista é o esperado
        self.assertEqual(data[0]['dataHorario'], agendamento_serializado['dataHorario'])

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
            'id': data['id'],  # Use o ID retornado
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
    
        self.assertEqual(response.status_code, 400)



class TesteGetHorarios(APITestCase):

    @mock.patch("agenda.libs.brasil_api.is_feriado", return_value=True)
    def test_quando_e_feriado(self, _):
        """
        Se for feriado deve retornar lista vazia, pois não é permitido realizar agendamento no feriado
        """
        response = self.client.get('/api/horarios/?data=2022-12-25')
        self.assertEqual(response.data, [])

    @mock.patch("agenda.libs.brasil_api.is_feriado", return_value=False)
    def test_data_e_dia_comum_retorna_lista(self, _):

        '''
        Dias comuns deve retonar as lista com os dias disponiveis.
        '''
        response = self.client.get('/api/horarios/?data=2022-10-03')

        # Verifica se a resposta não está vazia
        self.assertNotEqual(response.data, [])


