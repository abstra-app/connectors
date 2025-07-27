"""
Serviços de Arrecadação v2.0.9
API referente aos serviços de arrecadação para parceiros arrecadadores do Banco do Brasil S.A.
Utiliza autenticação mútua do certificado.
"""

import requests


class ServicosDeArrecadacaoClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_arrecadacoes(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
        A partir do código de barras (digitado OU capturado), valor, consulta o parceiro arrecadador

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/arrecadacoes".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_liquidar_guia(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
        Liquidar Guia do Parceiro Arrecadador

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/liquidar-guia".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        codigo_parceiro: float = None,
        codigo_conciliacao: str = None,
    ):
        """
        Consultar pagamento de Parceiro Arrecadador

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param codigo_parceiro: Código do Parceiro de Arrecadação junto ao BB.
            @param codigo_conciliacao: Este campo determina o identificador da transação. O objetivo desse campo é ser um elemento que possibilite ao parceiro a funcionalidade de conciliação da sua solicitação de pagamento junto ao BB.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if codigo_parceiro is not None:
            query["codigoParceiro"] = codigo_parceiro
        if codigo_conciliacao is not None:
            query["codigoConciliacao"] = codigo_conciliacao
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/pagamentos".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
