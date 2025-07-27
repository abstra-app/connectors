"""
PagBB v1.0.3
A API de pagamentos em lote permite que, de forma automatizada, realize o envio de pagamentos a fornecedores, prestadores de serviços e colaboradores.
 - Receba seus dados de pagamentos agrupados de forma rápida e segura.
- Ideal para clientes que já utilizam o sistema de pagamentos em lote do Banco do Brasil.
- Envie pagamentos de forma eficiente e automatizada.

"""

import requests


class PagBbClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_lotes_pix(self, *, gw_dev_app_key: str = None, body: dict = None):
        """
        Permite a inclusão de um lote contendo lançamentos do tipo PIX.

        Args:
            @param gw_dev_app_key: Chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        path_params = {}
        path_rendered = "/lotes/pix".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_by_id_lote_pix_lancamentos(
        self, *, gw_dev_app_key: str = None, contrato: int = None, id_lote: str = None
    ):
        """
        Permite detalhar as informações de um lote PIX.

        Args:
            @param gw_dev_app_key: Chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param contrato: Número do contrato PagBB do cliente com o Banco do Brasil.
            @param id_lote: Número identificador do lote informado pelo cliente no momento da inclusão.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if contrato is not None:
            query["contrato"] = contrato
        headers = {}
        path_params = {}
        if id_lote is not None:
            path_params["id-lote"] = id_lote
        path_rendered = "/lotes/{id-lote}/pix/lancamentos".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_by_id_lote_pix_lancamentos_by_id_lancamento(
        self,
        *,
        gw_dev_app_key: str = None,
        contrato: int = None,
        id_lote: str = None,
        id_lancamento: str = None,
    ):
        """
        Permite detalhar os dados de um lançamento específico realizado dentro de um lote PIX.

        Args:
            @param gw_dev_app_key: Chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param contrato: Número do contrato PagBB do cliente com o Banco do Brasil.
            @param id_lote: Número identificador do lote informado pelo cliente no momento da inclusão.
            @param id_lancamento: Número identificador do lançamento em um lote.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if contrato is not None:
            query["contrato"] = contrato
        headers = {}
        path_params = {}
        if id_lote is not None:
            path_params["id-lote"] = id_lote
        if id_lancamento is not None:
            path_params["id-lancamento"] = id_lancamento
        path_rendered = "/lotes/{id-lote}/pix/lancamentos/{id-lancamento}".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_lotes_by_id_lote_liberacoes(
        self, *, gw_dev_app_key: str = None, contrato: int = None, id_lote: str = None
    ):
        """
        Autoriza o pagamento dos lançamentos de um lote.

        Args:
            @param gw_dev_app_key: Chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param contrato: Número do contrato PagBB do cliente com o Banco do Brasil.
            @param id_lote: Número identificador do lote informado pelo cliente no momento da inclusão.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if contrato is not None:
            query["contrato"] = contrato
        headers = {}
        path_params = {}
        if id_lote is not None:
            path_params["id-lote"] = id_lote
        path_rendered = "/lotes/{id-lote}/liberacoes".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_lotes_by_id_lote_cancelamentos(
        self, *, gw_dev_app_key: str = None, contrato: int = None, id_lote: str = None
    ):
        """
        Cancela um lote e todos os seus lançamentos.

        Args:
            @param gw_dev_app_key: Chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param contrato: Número do contrato PagBB do cliente com o Banco do Brasil.
            @param id_lote: Número identificador do lote informado pelo cliente no momento da inclusão.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if contrato is not None:
            query["contrato"] = contrato
        headers = {}
        path_params = {}
        if id_lote is not None:
            path_params["id-lote"] = id_lote
        path_rendered = "/lotes/{id-lote}/cancelamentos".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
