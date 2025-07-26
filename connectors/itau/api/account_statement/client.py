from ...utils.auth import Credentials
import requests
import uuid
from datetime import date
import json
from typing import List, Optional, Literal
from dataclasses import dataclass, asdict
from ...utils.currency import str_to_cents


@dataclass
class FilteredBy:
    property: str
    operand: str
    value: str

    def to_dict(self):
        """
        Serializes the FilteredBy instance to a dictionary.
        """
        return {"property": self.property, "operand": self.operand, "value": self.value}

    def to_query_value(self):
        """
        Serializes the FilteredBy instance to a query value string.
        """
        return json.dumps(self.to_dict())


@dataclass
class StatementEventLiteral:
    """
    Event literal
    """

    code: str
    """
    Transaction reason code
    """

    shortened: str
    """
    Short description of the event
    """

    complete: str
    """
    Full description of the event
    """

    tip: str
    """
    tip
    """

    @classmethod
    def from_dict(cls, data: dict):
        """
        {
            "type": "object",
            "description": "Event literal",
            "properties": {
                "code": {
                    "description": "Transaction reason code",
                    "type": "string"
                },
                "shortened": {
                    "description": "Short description of the event",
                    "type": "string"
                },
                "complete": {
                    "description": "Full description of the event",
                    "type": "string"
                },
                "tip": {
                    "description": "tip",
                    "type": "string"
                }
            }
        }
        """
        return cls(
            code=data["code"],
            shortened=data["shortened"],
            complete=data["complete"],
            tip=data["tip"],
        )


@dataclass
class StatementEventAmout:
    """
    Amount information
    """

    value_cents: int
    """
    Amount in cents
    """

    currency: str
    """
    Currency code (e.g., "BRL")
    """

    @classmethod
    def from_dict(cls, data: dict):
        """
        {
            "type": "object",
            "description": "Amount information",
            "properties": {
                "value": {
                    "description": "Amount value of event",
                    "type": "number"
                },
                "currency": {
                    "description": "Currency code of event",
                    "type": "string"
                }
            }
        }
        """
        return cls(value_cents=str_to_cents(data["value"]), currency=data["currency"])


@dataclass
class StatementEventCounterpart:
    """
    counterpart of the event
    """

    type: str
    """
    Account type code
    """

    ispb: str
    """
    Brazilian payment system identifier
    """

    agency: str
    """
    counterpart agency number
    """

    account: str
    """
    counterpart account number
    """

    digit: str
    """
    counterpart account digit
    """

    name: str
    """
    counterpart name
    """

    person: str
    """
    counterpart person type
    """

    document: str
    """
    counterpart document number
    """

    institution: str
    """
    counterpart financial institution name
    """


@dataclass
class StatementEventOrigin:
    """
    Information about the origin of the event
    """

    identifier: str
    """
    Unique Product identifier
    """

    type: str
    """
    Origin type
    """

    operation: str
    """
    description of type operation
    """

    channel: str
    """
    information of the channel operation
    """

    complement: str
    """
    the complement informed in the operation channel
    """


@dataclass
class StatementEvent:
    id: str
    """
    Unique event id
    """

    type: str
    """
    Kind of event
    """

    operation: Literal["C", "D"]
    """
    Operation type (C - Credit / D - Debit)
    """

    reversal: bool
    """
    Chargeback entry
    """

    event_date: date
    """
    Event date
    """

    accounting_date: date
    """
    Accounting date
    """

    literal: StatementEventLiteral
    """
    Event literal
    """

    amount: StatementEventAmout
    """
    Amount information
    """

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            type=data["type"],
            operation=data["operation"],
            reversal=data["reversal"],
            event_date=date.fromisoformat(data["eventDate"]),
            accounting_date=date.fromisoformat(data["accountingDate"]),
            literal=StatementEventLiteral.from_dict(data["literal"]),
            amount=StatementEventAmout.from_dict(data["amount"]),
        )


@dataclass
class StatementBalance:
    type: str
    """
    Type of balance amount
    """

    event_date: date
    """
    Balance date
    """

    accounting_date: date
    """
    Accounting balance date
    """

    literal_shortened: str
    """
    Short description of the balance
    """

    literal_complete: str
    """
    Full description of the balance
    """

    amount_cents: int
    """
    Amount value of event
    """

    currency: str
    """
    Currency code of event
    """

    @classmethod
    def from_dict(cls, data: dict):
        """
        {
            "description": "Account balance",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "description": "Type of balance amount",
                        "type": "string"
                    },
                    "date": {
                        "type": "object",
                        "description": "information of the event date",
                        "properties": {
                            "event": {
                                "description": "Balance date",
                                "type": "string"
                            },
                            "accounting": {
                                "description": "Accounting balance date",
                                "type": "string"
                            }
                        }
                    },
                    "literal": {
                        "type": "object",
                        "description": "balance literal",
                        "properties": {
                            "shortened": {
                                "description": "Short description of the balance",
                                "type": "string"
                            },
                            "complete": {
                                "description": "Full description of the balance",
                                "type": "string"
                            }
                        }
                    },
                    "amount": {
                        "type": "object",
                        "description": "Amount information",
                        "properties": {
                            "value": {
                                "description": "Amount value of event",
                                "type": "number"
                            },
                            "currency": {
                                "description": "Currency code of event",
                                "type": "string"
                            }
                        }
                    }
                },
                "required": [
                    "type",
                    "date",
                    "literal",
                    "amount"
                ]
            }
        }
        """

        return cls(
            type=data["type"],
            event_date=date.fromisoformat(data["date"]["event"]),
            accounting_date=date.fromisoformat(data["date"]["accounting"]),
            literal_shortened=data["literal"]["shortened"],
            literal_complete=data["literal"]["complete"],
            amount_cents=str_to_cents(data["amount"]["value"]),
            currency=data["amount"]["currency"],
        )


@dataclass
class StatementPagination:
    """
    Partner account statement pagination
    """

    page: int
    """
    Current page
    """

    total_pages: int
    """
    Total number of pages
    """

    total_elements: int
    """
    Total number of postings for the selected period
    """

    page_size: int
    """
    Page size
    """

    @classmethod
    def from_dict(cls, data: dict):
        # Example from sandbox (2025-07-26):
        # {
        #     "links": {
        #         "first": "/statements/150000999999?end_date=2024-06-26&page=1&type=current_account&start_date=2023-01-01&page_size=1000",
        #         "last": "/statements/150000999999?end_date=2024-06-26&page=10&type=current_account&start_date=2023-01-01&page_size=1000",
        #         "previous": "",
        #         "next": "/statements/150000999999?end_date=2024-06-26&page=2&type=current_account&start_date=2023-01-01&page_size=1000",
        #     },
        #     "page": 1,
        #     "total_pages": 10,
        #     "total_elements": 9109,
        #     "page_size": 1000,
        # }

        return cls(
            page=data["page"],
            total_pages=data["total_pages"],
            total_elements=data["total_elements"],
            page_size=data["page_size"],
        )


@dataclass
class Statement:
    events: List[StatementEvent]

    balances: List[StatementBalance]
    """
    Account balance
    """

    pagination: StatementPagination
    """
    Partner account statement pagination
    """

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            events=[
                StatementEvent.from_dict(event) for event in data.get("events", [])
            ],
            balances=[
                StatementBalance.from_dict(balance)
                for balance in data.get("balances", [])
            ],
            pagination=StatementPagination.from_dict(data.get("pagination", {})),
        )


@dataclass
class Error:
    """
    Error model
    """

    status: int
    """
    Error code
    """

    message: str
    """
    Error message
    """

    @property
    def exception(self):
        """
        Returns a formatted exception message.
        """
        return f"Error {self.status}: {self.message}"

    @classmethod
    def from_dict(cls, data: dict):
        """
        {
            "description": "Error model",
            "type": "object",
            "properties": {
                "status": {
                    "type": "number",
                    "description": "Error code"
                },
                "message": {
                    "type": "string",
                    "description": "Error message"
                }
            }
        }
        """
        assert "status" in data and "message" in data, f"Invalid error data: {data}"
        return cls(status=data["status"], message=data["message"])


@dataclass
class InterestBearingAccount:
    date: date
    gross_amount_cents: int
    net_amount_cents: int
    iof: float
    ir: float
    gross_income_cents: int

    @classmethod
    def from_dict(cls, data: dict):
        """
        "interestBearingAccount": {
            "type": "object",
            "description": "Partner Income Datails",
            "properties": {
                "date": {
                    "type": "string"
                },
                "grossAmountValue": {
                    "type": "string"
                },
                "netAmountValue": {
                    "type": "string"
                },
                "iof": {
                    "type": "string"
                },
                "ir": {
                    "type": "string"
                },
                "grossIncome": {
                    "type": "string"
                }
            }
        }
        """
        return cls(
            date=data["date"],
            gross_amount_cents=str_to_cents(data["grossAmountValue"]),
            net_amount_cents=str_to_cents(data["netAmountValue"]),
            iof=float(data["iof"]),
            ir=float(data["ir"]),
            gross_income_cents=str_to_cents(data["grossIncome"]),
        )


@dataclass
class AccountStatementClient:
    """
    Cliente para a API de Extrato de Conta do Itaú.
    """

    creds: Credentials

    def __init__(self, creds: Credentials, base_url: str = None):
        self.creds = creds
        # URL padrão para sandbox, pode ser sobrescrita
        self.base_url = (
            base_url
            or "https://sandbox.devportal.itau.com.br/itau-x0-api-account-statement-v1-externo/v1"
        )

    def _get_headers(self, correlation_id=None):
        """
        Monta os headers necessários para autenticação e rastreio.
        """
        return {
            "Authorization": f"Bearer {self.creds.get_token().access_token}",
            "x-itau-correlationid": correlation_id or str(uuid.uuid4()),
            "User-Agent": "Collection-by-itaú-for-developers",
            "Accept": "application/json",
        }

    def get_statement(
        self,
        statement_id: str,
        type: Literal["current_account", "savings_account"],
        start_date: date,
        correlation_id: Optional[uuid.UUID] = None,
        end_date: Optional[date] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        statement_type: Optional[str] = None,
        filter_by: Optional[List[FilteredBy]] = None,
    ):
        """
        Consulta o extrato de conta bancária.
        Corresponde ao endpoint GET /statements/{statementId}

        @param statement_id: str - Unique identifier that references a specific account. Use the Agency + Account + Validator Digit format, example: Ag. 1234 - CC. 5678901 - DV. 2 = Account - 123456789012
        @param type: Literal["current_account", "savings_account"] - Select type of bank account ( Example - "current_account" or "savings_account")
        @param start_date: date - Start date of consultation
        @param correlation_id: Optional[uuid.UUID] - Unique identifier (UUID) that allows reference to a specific transaction or chain of events, used to help track a flow of calls.
        @param end_date: Optional[date] - End date of consultation
        @param page: Optional[int] - Query page
        @param page_size: Optional[int] - Query page size
        @param statement_type: Optional[str] - Get different views of the bank statement ( summarized / complete )
        @param filter_by: Optional[List[FilteredBy]] - List of FilteredBy to filter the results.
        """
        url = f"{self.base_url}/statements/{statement_id}"
        params = {
            "type": type,
            "start_date": start_date.isoformat()
            if isinstance(start_date, date)
            else start_date,
        }
        if end_date:
            params["end_date"] = (
                end_date.isoformat() if isinstance(end_date, date) else end_date
            )
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if statement_type:
            params["statement_type"] = statement_type
        if filter_by:
            # Serializa a lista de FilteredBy para o formato esperado pela API
            import json

            params["filter_by"] = json.dumps([asdict(f) for f in filter_by])

        headers = self._get_headers(correlation_id)
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return Statement.from_dict(data)
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            raise Exception(
                f"Unexpected response status: {response.status_code}, content: {response.text}"
            )

    def get_interest_bearing_accounts(
        self,
        statement_id: str,
        type: Literal["current_account", "savings_account"],
        start_date: date,
        correlation_id: Optional[uuid.UUID] = None,
        end_date: Optional[date] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        statement_type: Optional[str] = None,
        filter_by: Optional[List[FilteredBy]] = None,
    ):
        """
        Consulta os dados de rendimento de conta remunerada.
        Corresponde ao endpoint GET /statements/{statementId}/interest-bearing-accounts

        @param statement_id: str - Unique identifier that references a specific account. Use the Agency + Account + Validator Digit format, example: Ag. 1234 - CC. 5678901 - DV. 2 = Account - 123456789012
        @param type: Literal["current_account", "savings_account"] - Select type of bank account ( Example - "current_account" or "savings_account")
        @param correlation_id: Optional[uuid.UUID] - Unique identifier (UUID) that allows reference to a specific transaction or chain of events, used to help track a flow of calls.
        @param start_date: date - Start date of consultation
        @param end_date: Optional[date] - End date of consultation
        @param page: Optional[int] - Query page
        @param page_size: Optional[int] - Query page size
        @param statement_type: Optional[str] - Get different views of the bank statement ( summarized / complete )
        @param filter_by: Optional[List[FilteredBy]] - List of FilteredBy to filter the results.
        """
        url = f"{self.base_url}/statements/{statement_id}/interest-bearing-accounts"
        params = {
            "start_date": start_date.isoformat()
            if isinstance(start_date, date)
            else start_date,
        }

        if type:
            params["type"] = type

        if end_date:
            params["end_date"] = (
                end_date.isoformat() if isinstance(end_date, date) else end_date
            )

        if page is not None:
            params["page"] = page

        if page_size is not None:
            params["page_size"] = page_size

        if statement_type:
            params["statement_type"] = statement_type

        if filter_by:
            params["filter_by"] = json.dumps([f.to_dict() for f in filter_by])

        headers = self._get_headers(correlation_id)
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            # The API returns {"data": [ ... ]}, so parse as a list
            return [
                InterestBearingAccount.from_dict(item) for item in data.get("data", [])
            ]
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            raise Exception(
                f"Unexpected response status: {response.status_code}, content: {response.text}"
            )
