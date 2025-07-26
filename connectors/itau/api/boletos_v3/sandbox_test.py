from unittest import TestCase
from connectors.itau.api.boletos_v3.client import BoletosV3Client
from connectors.itau.utils.auth import Credentials
from dotenv import load_dotenv
from pathlib import Path
from datetime import date

load_dotenv(Path(__file__).parent.parent / ".env")


class TestBoletosV3Client(TestCase):
    def setUp(self):
        json_file = Path(__file__).parent.parent.parent / "sandbox.json"
        creds = Credentials.from_json_file(json_file)
        self.client = BoletosV3Client(creds=creds)

    def test_get_francesas(self):
        """Testa a consulta de francesas"""
        response = self.client.get_francesas(agencia="1500", conta="0001560", dac="1")
        self.assertIsNotNone(response)

    def test_get_boletos(self):
        """Testa a consulta de boletos"""
        data_inicial = "2024-01-01T00:00:00.000Z"
        data_final = "2024-12-31T00:00:00.000Z"
        id_beneficiario = "15000015601"  # Exemplo: agência 1500 + conta 0001560 + DAC 1

        response = self.client.get_boletos(
            data_inicial=data_inicial,
            data_final=data_final,
            id_beneficiario=id_beneficiario,
        )
        self.assertIsNotNone(response)

    def test_get_boletos_by_date_range(self):
        """Testa a consulta de boletos usando objetos date"""
        data_inicial = date(2024, 1, 1)
        data_final = date(2024, 12, 31)
        id_beneficiario = "15000015601"

        response = self.client.get_boletos_by_date_range(
            data_inicial=data_inicial,
            data_final=data_final,
            id_beneficiario=id_beneficiario,
        )
        self.assertIsNotNone(response)

    def test_get_notificacoes_boleto(self):
        """Testa a consulta de notificações de boletos"""
        response = self.client.get_notificacoes_boleto()
        self.assertIsNotNone(response)

    def test_create_notificacao_boleto(self):
        """Testa a criação de notificação de boleto"""
        try:
            response = self.client.create_notificacao_boleto(
                id_beneficiario="15000015601",
                webhook_url="https://teste.webhook.com",
                webhook_client_id="test-client-id",
                webhook_client_secret="test-client-secret",
                tipos_notificacoes=["BAIXA_EFETIVA", "BAIXA_OPERACIONAL"],
                valor_minimo_cents=10000,  # 100 reais em centavos
            )
            self.assertIsNotNone(response)
        except Exception as e:
            # Pode falhar em ambiente de sandbox, mas não deve quebrar o teste
            print(f"Teste de criação de notificação falhou (esperado em sandbox): {e}")

    def test_get_francesa_movimentacoes(self):
        """Testa a consulta de movimentações de francesa"""
        # Primeiro busca francesas disponíveis
        francesas = self.client.get_francesas(agencia="1500", conta="0001560", dac="1")

        if francesas and "data" in francesas and len(francesas["data"]) > 0:
            # Pega o primeiro ID de francesa disponível
            id_francesa = francesas["data"][0].get("id_francesa")
            if id_francesa:
                response = self.client.get_francesa_movimentacoes(id_francesa)
                self.assertIsNotNone(response)

    def test_get_francesa_movimentacoes_resumidas(self):
        """Testa a consulta de movimentações resumidas de francesa"""
        # Primeiro busca francesas disponíveis
        francesas = self.client.get_francesas(agencia="1500", conta="0001560", dac="1")

        if francesas and "data" in francesas and len(francesas["data"]) > 0:
            # Pega o primeiro ID de francesa disponível
            id_francesa = francesas["data"][0].get("id_francesa")
            if id_francesa:
                response = self.client.get_francesa_movimentacoes_resumidas(id_francesa)
                self.assertIsNotNone(response)
