"""
API Login BB (Entrar com o BB) v1.0.0
A API Login BB, provê uma interface para facilitar o processo de login do seu sistema.
"""

import requests


class LoginBbClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def get_oauth_jwks(self):
        """
        Este endpoint retorna as chaves publicas usadas para verificar a assinatura dos IDs Tokens emitidos pelo OAUth 2.0.

        Args:
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/oauth/jwks".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_oauth_v2_userinfo(self, *, gw_app_key: str = None):
        """
        Este endpoint é utilizado para recuperar o objeto JWT assinado pelo servidor de autorização OAuth BB, contendo a informação do usuário logado. Para mais informações sobre este endpoint, gentileza verificar a documentação do OpenID Connect (OIDC) disponível em https://openid.net/specs/openid-connect-core-1_0.html#UserInfo

        Args:
            @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor (developer_application_key) criada no portal do desenvolvedor. Você pode consultar este valor acessando no Portal do Desenvolvedor -> Aplicações -> Credenciais -> developer_application_key.
        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        headers = {}
        path_params = {}
        path_rendered = "/oauth/v2/userinfo".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
