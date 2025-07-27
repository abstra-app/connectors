"""
API ACCOUNT STATEMENT v1.0.0
Accounts Statement API - get statement information of your bank account.
"""

import requests
from typing import Optional


class AccountStatementClient:
    base_url: str
    authorization: str

    def __init__(self, base_url: str, authorization: str):
        self.base_url = base_url.rstrip("/")
        self.authorization = authorization

    def get_statements_by_statement_id(
        self,
        *,
        statement_id: str = None,
        type: str = None,
        authorization: str = None,
        x_itau_correlationid: str = None,
        start_date: str = None,
        end_date: Optional[str] = None,
        page: Optional[float] = None,
        page_size: Optional[float] = None,
        statement_type: Optional[str] = None,
        filter_by: Optional[str] = None,
    ):
        """
        No description provided.

        Args:
            @param statement_id: Unique identifier that references a specific account. Use the Agency + Account + Validator Digit format, example: Ag. 1234 - CC. 5678901 - DV. 2 = Account - 123456789012
            @param type: Select type of bank account ( Example - "current_account" or "savings_account")
            @param authorization: Bearer Token authorization generated in the authorization flow in the "https://sts.rdhi.com.br/api/oauth/token" service.
            @param x_itau_correlationid: Unique identifier (UUID) that allows reference to a specific transaction or chain of events, used to help track a flow of calls.
            @param start_date: Start date of consultation
            @param end_date: End date of consultation
            @param page: Query page
            @param page_size: Query page size
            @param statement_type: Get different views of the bank statement ( summarized / complete )
            @param filter_by: Filter your search by alloweds fields in the content.
        """
        if authorization is None:
            authorization = self.authorization
        query = {
            "type": type,
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size,
            "statement_type": statement_type,
            "filter_by": filter_by,
        }
        headers = {
            "Authorization": authorization,
            "x-itau-correlationid": x_itau_correlationid,
        }
        path_params = {
            "statement_id": statement_id,
        }
        path_rendered = "/statements/{statementId}".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_statements_by_statement_id_interest_bearing_accounts(
        self,
        *,
        statement_id: str = None,
        authorization: str = None,
        x_itau_correlationid: str = None,
        start_date: str = None,
        end_date: Optional[str] = None,
    ):
        """
        No description provided.

        Args:
            @param statement_id: Unique identifier that references a specific account. Use the Agency + Account + Validator Digit format, example: Ag. 1234 - CC. 5678901 - DV. 2 = Account - 123456789012
            @param authorization: Bearer Token authorization generated in the authorization flow in the "https://sts.rdhi.com.br/api/oauth/token" service.
            @param x_itau_correlationid: Unique identifier (UUID) that allows reference to a specific transaction or chain of events, used to help track a flow of calls.
            @param start_date: Start date of consultation
            @param end_date: End date of consultation
        """
        if authorization is None:
            authorization = self.authorization
        query = {
            "start_date": start_date,
            "end_date": end_date,
        }
        headers = {
            "Authorization": authorization,
            "x-itau-correlationid": x_itau_correlationid,
        }
        path_params = {
            "statement_id": statement_id,
        }
        path_rendered = "/statements/{statementId}/interest-bearing-accounts".format(
            **path_params
        )
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
