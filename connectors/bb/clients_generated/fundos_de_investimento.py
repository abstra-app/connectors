"""
Fundos de Investimento v1.0.3
API pública que permita a clientes pessoa jurídica realizar solicitações de aplicação e resgate em seus fundos de investimento exclusivos por meio da integração com o sistema ERP por ele utilizado.
"""

import requests


class FundosDeInvestimentoClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def get_saldo_agencia_by_numero_agencia_conta_by_numero_conta(
        self, *, numero_agencia: int = None, numero_conta: int = None
    ):
        """
        Lista os fundos de investimento do cliente com os valores de seus respectivos saldos bruto e líquido para resgate.

        Args:
            @param numero_agencia: Número da agência do cliente sem o dígito verificador.
            @param numero_conta: Número da conta do cliente sem o dígito verificador.
        """
        query = {}
        headers = {}
        path_params = {}
        if numero_agencia is not None:
            path_params["numeroAgencia"] = numero_agencia
        if numero_conta is not None:
            path_params["numeroConta"] = numero_conta
        path_rendered = "/saldo/agencia/{numeroAgencia}/conta/{numeroConta}".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_aplicacao(self, *, body: dict = None):
        """
        Solicita a aplicação de um valor, proveniente de Conta Corrente, em um fundo de investimento.

        Args:
            @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/aplicacao".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_resgate(self, *, body: dict = None):
        """
        Solicita o resgate de um valor, a ser crédito na Conta Corrente, em um fundo de investimento.

        Args:
            @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/resgate".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_resgate_total(self, *, body: dict = None):
        """
        Solicita resgate de todo saldo em um fundo de investimento, a ser crédito na Conta Corrente.

        Args:
            @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/resgate-total".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()
