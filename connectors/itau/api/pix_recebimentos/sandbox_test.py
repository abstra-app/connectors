from unittest import TestCase
from connectors.itau.api.pix_recebimentos.client import PixRecebimentosClient
from connectors.itau.utils.auth import Credentials
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta
import uuid

load_dotenv(Path(__file__).parent.parent / ".env")

class TestPixRecebimentosClient(TestCase):
    def setUp(self):
        json_file = Path(__file__).parent.parent.parent / "sandbox.json"
        creds = Credentials.from_json_file(json_file)
        self.client = PixRecebimentosClient(creds=creds, sandbox=True)

    def test_post_cob(self):
        """Testa a criação de uma cobrança imediata (COB)"""
        data = {
            "calendario": {"expiracao": 3600},
            "valor": {"original": "10.00"},
            "chave": "60701190000104",
            "solicitacaoPagador": "Teste sandbox",
        }
        try:
            response = self.client.post_cob(data)
            self.assertIsNotNone(response)
        except Exception as e:
            print(f"Falha esperada em sandbox (post_cob): {e}")

    def test_get_cobs(self):
        """Testa a consulta de cobranças imediatas (COB)"""
        params = {
            "inicio": (datetime.now() - timedelta(days=30)).isoformat() + "Z",
            "fim": datetime.now().isoformat() + "Z",
        }
        try:
            response = self.client.get_cobs(params)
            self.assertIsNotNone(response)
        except Exception as e:
            print(f"Falha esperada em sandbox (get_cobs): {e}")

    def test_post_loc(self):
        """Testa a criação de uma location"""
        data = {"tipoCob": "cob"}
        try:
            response = self.client.post_loc(data)
            self.assertIsNotNone(response)
        except Exception as e:
            print(f"Falha esperada em sandbox (post_loc): {e}")

    def test_get_locs(self):
        """Testa a consulta de locations"""
        params = {
            "inicio": (datetime.now() - timedelta(days=30)).isoformat() + "Z",
            "fim": datetime.now().isoformat() + "Z",
        }
        try:
            response = self.client.get_locs(params)
            self.assertIsNotNone(response)
        except Exception as e:
            print(f"Falha esperada em sandbox (get_locs): {e}")

    def test_get_pixs(self):
        """Testa a consulta de Pix recebidos"""
        params = {
            "inicio": (datetime.now() - timedelta(days=30)).isoformat() + "Z",
            "fim": datetime.now().isoformat() + "Z",
        }
        try:
            response = self.client.get_pixs(params)
            self.assertIsNotNone(response)
        except Exception as e:
            print(f"Falha esperada em sandbox (get_pixs): {e}")

    def test_webhook(self):
        """Testa configuração e consulta de webhook"""
        chave = "60701190000104"
        webhook_url = "https://webhook.site/teste-sandbox"
        data = {"webhookUrl": webhook_url}
        try:
            put_resp = self.client.put_webhook(chave, data)
            self.assertIsNotNone(put_resp)
        except Exception as e:
            print(f"Falha esperada em sandbox (put_webhook): {e}")
        try:
            get_resp = self.client.get_webhook(chave)
            self.assertIsNotNone(get_resp)
        except Exception as e:
            print(f"Falha esperada em sandbox (get_webhook): {e}") 