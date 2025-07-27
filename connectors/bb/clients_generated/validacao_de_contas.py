"""
Validação de Contas v1.0
A API Validação de Contas permite acesso a consulta da situação de uma determinada conta.
"""

import requests


class ValidacaoDeContasClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def get_contas_by_agencia_by_conta_situacao(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        cpf_cnpj: int = None,
        agencia: str = None,
        conta: str = None,
    ):
        """
        Verifica a situação da conta (corrente ou poupança) em uma agência específica, se ela está ativa ou não. E também verifica se o CPF/CNPJ informado é o titular da conta.

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param cpf_cnpj: Número do CPF ou CNPJ do cliente. Somente números.
            @param agencia: Número da agência, sem digito verificador.
            @param conta: Número da conta, sem digito verificador.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if cpf_cnpj is not None:
            query["cpfCnpj"] = cpf_cnpj
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if agencia is not None:
            path_params["agencia"] = agencia
        if conta is not None:
            path_params["conta"] = conta
        path_rendered = "/contas/{agencia}-{conta}/situacao".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
