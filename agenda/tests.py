from rest_framework.test import APITestCase
import json
from agenda.models import Agendamento
from datetime import datetime
from django.utils import timezone

class TestListegemAgendamentos(APITestCase):


    def test_listagem_vazia(self):
        response = self.client.get('/api/agendamentos/')
        data = json.loads(response.content)
        self.assertEqual(data, [])


    def test_listagem_agendamentos_criados(self):

        Agendamento.objects.create(
            dataHorario=timezone.make_aware(datetime(2025, 3, 15)),
            nomeCliente = "Lucas",
            emailCliente = 'lmiranda@gmail.com',
            telefoneCliente = '+55123123123',
        )

        agendamento_serializado = {
            "id": 1,
            "dataHorario": '2025-03-15T00:00:00Z',
            "nomeCliente": "Lucas",
            "emailCliente": 'lmiranda@gmail.com',
            "telefoneCliente": '+55123123123',
        }

        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)

        self.assertDictEqual(data[0], agendamento_serializado)

class TestCriacaoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        agendamento_data = {
            "id": 1,
            "dataHorario": '2025-03-15T00:00:00Z',
            "nomeCliente": "Lucas",
            "emailCliente": 'lmiranda@gmail.com',
            "telefoneCliente": '+55123123123',
        }
        response = self.client.post('/api/agendamentos/',agendamento_data)
        data = json.loads(response.content)
        self.assertDictEqual(data, agendamento_data)

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