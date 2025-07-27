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
        query = {}
        if type is not None:
            query["type"] = type
        if start_date is not None:
            query["start_date"] = start_date
        if end_date is not None:
            query["end_date"] = end_date
        if page is not None:
            query["page"] = page
        if page_size is not None:
            query["page_size"] = page_size
        if statement_type is not None:
            query["statement_type"] = statement_type
        if filter_by is not None:
            query["filter_by"] = filter_by
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        if x_itau_correlationid is not None:
            headers["x-itau-correlationid"] = x_itau_correlationid
        path_params = {}
        if statement_id is not None:
            path_params["statementId"] = statement_id
        path_rendered = "/statements/{statementId}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
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
        query = {}
        if start_date is not None:
            query["start_date"] = start_date
        if end_date is not None:
            query["end_date"] = end_date
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        if x_itau_correlationid is not None:
            headers["x-itau-correlationid"] = x_itau_correlationid
        path_params = {}
        if statement_id is not None:
            path_params["statementId"] = statement_id
        path_rendered = "/statements/{statementId}/interest-bearing-accounts".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
