"""
Simulação de pagar boleto v1.0
API para simular o pagamento de um boleto no ambiente de testes do Banco do Brasil S.A.
"""

import requests


class SimulacaoDePagarBoletoClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_boletos_cobranca_by_linha_digitavel_pagar(
        self, *, linha_digitavel: int = None, gw_dev_app_key: str = None
    ):
        """
        No description provided.

        Args:
            @param linha_digitavel: No description provided.
            @param gw_dev_app_key: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        path_params = {}
        if linha_digitavel is not None:
            path_params["linhaDigitavel"] = linha_digitavel
        path_rendered = "/boletos-cobranca/{linhaDigitavel}/pagar".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
