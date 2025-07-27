"""
API - Emissão de QR Code Pix Automático v1.0.0
Documentação do fluxo de Geração de QR Code com Recorrência de Pagamentos - PIX Automático
"""

import requests
from typing import Optional


class QrcodePixAutomaticoV1Client:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def post_cobrancas(
        self,
        *,
        x_itau_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
        body: dict = None,
    ):
        """
                Endpoint para emitir um QR Code imediato ou QR Code de vencimento de Pix Automático.

                Args:
                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_apikey: **Descrição:** Chave de API fornecida pelo Itaú para autenticação e autorização das requisições.

        **RegEx:** `^[a-zA-Z0-9]{32}$`

                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        path_rendered = "/cobrancas".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_cobrancas_by_cobranca_id(
        self,
        *,
        x_itau_correlation_id: Optional[str] = None,
        cobranca_id: str = None,
        x_itau_apikey: str = None,
        body: dict = None,
    ):
        """
                Endpoint para Cancelar um QR Code imediato ou QR Code de vencimento de Pix Automático.

                Args:
                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param cobranca_id: **Descrição:** Identificador do QR Code que possibilita a conciliação de pagamentos.

        **Observação:** Este código deve possuir entre 26 e 35 posições, podendo conter letras minúsculas (a-z), letras maiúsculas (A-Z) e números (0-9).

                    @param x_itau_apikey: **Descrição:** Chave de API fornecida pelo Itaú para autenticação e autorização das requisições.

        **RegEx:** `^[a-zA-Z0-9]{32}$`

                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if cobranca_id is not None:
            path_params["cobrancaId"] = cobranca_id
        path_rendered = "/cobrancas/{cobrancaId}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()
