"""
Autorização de Débito Automático v3.0.3
API de serviço de autorização de débito automático (recorrente) em conta por parte de um terceiro.
"""

import requests


class AutorizacaoDebitoAutomaticoClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_direct_debit_authorizations(self, *, body: dict = None):
        """
        Autoriza débito automático (recorrente) em conta por parte de um terceiro.

        Args:
            @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/direct-debit-authorizations".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()
