from unittest import TestCase
import uuid
from .clients_generated.account_statement import AccountStatementClient
from .utils.auth import Credentials
from pathlib import Path
from datetime import date


class TestAccountStatement(TestCase):
    def test_account_statement(self):
        creds = Credentials.from_json_file(
            Path(__file__).parent.joinpath("sandbox.json")
        )
        client = AccountStatementClient(
            base_url="https://sandbox.devportal.itau.com.br/itau-x0-api-account-statement-v1-externo/v1",
            authorization=f"Bearer {creds.get_token().access_token}",
        )
        response = client.get_statements_by_statement_id(
            statement_id="150000581085",
            x_itau_correlationid=uuid.uuid4().hex,
            type="current_account",
            start_date=date.today(),
        )
        print(response)
