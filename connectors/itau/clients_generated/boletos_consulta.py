"""
API Boletos - Consulta de detalhe do Boleto v1.2.0
API responsável pela consulta detalhada do estado do boleto, a partir de critérios específicos.
"""

import requests
from typing import Optional


class BoletosConsultaClient:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def get_boletos(
        self,
        *,
        authorization: str = None,
        x_itau_correlationid: str = None,
        x_itau_apikey: str = None,
        x_itau_flowid: Optional[str] = None,
        id_beneficiario: Optional[str] = None,
        codigo_carteira: str = None,
        nosso_numero: str = None,
        view: Optional[str] = None,
    ):
        """
        No description provided.

        Args:
            @param authorization: Token de acesso a API
            @param x_itau_correlationid: UUID que identifica a transação
            @param x_itau_apikey: Key que identifica o chamador
            @param x_itau_flowid: Key que identifica o fluxo
            @param id_beneficiario: (4 dígitos agência)+(7 dígitos c/c)+(1 dígito DAC)
            @param codigo_carteira: Código da carteira do título
            @param nosso_numero: Número de identificação do título
            @param view: Nivel de detalhe de uma cobrança
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if id_beneficiario is not None:
            query["id_beneficiario"] = id_beneficiario
        if codigo_carteira is not None:
            query["codigo_carteira"] = codigo_carteira
        if nosso_numero is not None:
            query["nosso_numero"] = nosso_numero
        if view is not None:
            query["view"] = view
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        if x_itau_correlationid is not None:
            headers["x-itau-correlationid"] = x_itau_correlationid
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_flowid is not None:
            headers["x-itau-flowid"] = x_itau_flowid
        path_params = {}
        path_rendered = "/boletos".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
