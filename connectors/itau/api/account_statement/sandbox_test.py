from unittest import TestCase
from .client import AccountStatementClient, Statement, InterestBearingAccount
from ...utils.auth import Credentials
from dotenv import load_dotenv
from pathlib import Path
from datetime import date

load_dotenv(Path(__file__).parent.parent / ".env")


class TestAccountStatementClient(TestCase):
    def setUp(self):
        json_file = Path(__file__).parent.parent.parent / "sandbox.json"
        creds = Credentials.from_json_file(json_file)
        self.client = AccountStatementClient(creds=creds)

    def test_get_statement(self):
        response = self.client.get_statement(
            statement_id="123456789012",
            statement_type="current_account",
            type="current_account",
            start_date=date.today(),
        )
        self.assertIsInstance(response, Statement)

    def test_get_interest_bearing_accounts(self):
        response = self.client.get_interest_bearing_accounts(
            statement_id="123456789012",
            type="current_account",
            start_date=date.today(),
        )
        self.assertIsInstance(response, list)
        if response:
            all(
                self.assertIsInstance(item, InterestBearingAccount) for item in response
            )
