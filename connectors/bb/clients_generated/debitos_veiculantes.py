"""
Débitos Veiculares v1.0.2
API referente aos serviços de consultas e pagamentos de débitos veiculares para parceiros arrecadadores do Banco do Brasil S.A.
"""

import requests


class DebitosVeiculantesClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_solicitacoes(self, *, body: dict = None):
        """
        Cadastra uma solicitação de consulta de dados de débitos veiculares. O retorno da consulta é assíncrono, com tempo estimado de processamento superior a 1000ms, sendo enviado automaticamente por meio de webhook previamente cadastrado quando a consulta estiver finalizada.

        Args:
            @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/solicitacoes".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_pagamentos(self, *, body: dict = None):
        """
        Permite a liquidação de débitos veiculares por meio de identificadores únicos, obtidos em consulta de débitos prévia.

        Args:
            @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/pagamentos".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_solicitacoes_by_codigo_solicitacao(self, *, codigo_solicitacao: str = None):
        """
        Obtém informações de débitos veiculares de consulta previamente registrada por codigoSolicitacao.

        Args:
            @param codigo_solicitacao: Código de protocolo que identifica cada solicitação de consulta realizada.
        """
        query = {}
        headers = {}
        path_params = {}
        if codigo_solicitacao is not None:
            path_params["codigoSolicitacao"] = codigo_solicitacao
        path_rendered = "/solicitacoes/{codigoSolicitacao}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
