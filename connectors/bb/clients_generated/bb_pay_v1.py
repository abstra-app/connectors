"""
BBPay v1.7
Api para realizar consultas e solicitações de pagamentos para clientes do Banco do Brasil S.A.
"""

import requests
from typing import Optional


class BbPayV1Client:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_solicitacao_pagamento(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
        Cria uma solicitação de pagamentos para clientes

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
        path_rendered = "/solicitacao-pagamento".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_solicitacao_pagamento_by_numero_solicitacao_pagamento(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        numero_convenio: int = None,
        data_pagamento: Optional[str] = None,
        numero_ultimo_pagamento_consultado: int = None,
        numero_solicitacao_pagamento: int = None,
    ):
        """
        Listar os pagamentos de um cliente em uma data ou por uma solicitação de pagamento especifica.

        Args:
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param numero_convenio: Número de Convênio do cliente com o Checkout
            @param data_pagamento: Data do pagamento. Se não informar número da solicitação de pagamento, é obrigatório informar a data.
            @param numero_ultimo_pagamento_consultado: Número do último pagamento enviado em resposta devolvida pelo banco anteriormente, com os mesmos campos de entrada
            @param numero_solicitacao_pagamento: Número da solicitação de pagamento
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if data_pagamento is not None:
            query["dataPagamento"] = data_pagamento
        if numero_ultimo_pagamento_consultado is not None:
            query["numeroUltimoPagamentoConsultado"] = (
                numero_ultimo_pagamento_consultado
            )
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_solicitacao_pagamento is not None:
            path_params["numeroSolicitacaoPagamento"] = numero_solicitacao_pagamento
        path_rendered = "/solicitacao-pagamento/{numeroSolicitacaoPagamento}".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos_by_numero_pagamento_solicitacao(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        numero_convenio: int = None,
        numero_pagamento_solicitacao: int = None,
    ):
        """
        Consulta Informações relativas a um Pagamento específico de uma Solicitação de Pagamentos

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param numero_convenio: Número de Convênio do cliente
            @param numero_pagamento_solicitacao: Número do pagamento da solicitação
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_pagamento_solicitacao is not None:
            path_params["numeroPagamentoSolicitacao"] = numero_pagamento_solicitacao
        path_rendered = "/pagamentos/{numeroPagamentoSolicitacao}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_pagamentos_by_numero_pagamento_solicitacao_devolver(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        numero_pagamento_solicitacao: int = None,
        body: dict = None,
    ):
        """
        Devolve um pagamento

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param numero_pagamento_solicitacao: Número do pagamento da solicitação que será devolvido.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_pagamento_solicitacao is not None:
            path_params["numeroPagamentoSolicitacao"] = numero_pagamento_solicitacao
        path_rendered = "/pagamentos/{numeroPagamentoSolicitacao}/devolver".format(
            **path_params
        )
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_solicitacao_pagamentos_by_numero_solicitacao_pagamento_autorizacoes(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        numero_solicitacao_pagamento: int = None,
        body: dict = None,
    ):
        """
        Cria uma solicitação de autorização de pagamento

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param numero_solicitacao_pagamento: Número da solicitação do pagamento que será autorizado.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_solicitacao_pagamento is not None:
            path_params["numeroSolicitacaoPagamento"] = numero_solicitacao_pagamento
        path_rendered = (
            "/solicitacao-pagamentos/{numeroSolicitacaoPagamento}/autorizacoes".format(
                **path_params
            )
        )
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_by_id_marcas_ativas(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        numero_convenio: int = None,
        id: int = None,
    ):
        """
        Lista as marcas ativas participantes do Open Banking para utilização no processo de iniciação de pagamento.

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param numero_convenio: Número de convênio do cliente com o Checkout.
            @param id: Número da marca do participante Open Banking do débito para rechamada.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/{id}/marcas-ativas".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos_by_numero_pagamento_solicitacao_autorizacoes(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        numero_convenio: int = None,
        numero_pagamento_solicitacao: int = None,
    ):
        """
        Consulta a autorização de pagamento (consentimento) de um pagamento em outra instituição financeira

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param numero_convenio: Número do convênio do cliente
            @param numero_pagamento_solicitacao: Número do pagamento da solicitação que foi autorizado.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_pagamento_solicitacao is not None:
            path_params["numeroPagamentoSolicitacao"] = numero_pagamento_solicitacao
        path_rendered = "/pagamentos/{numeroPagamentoSolicitacao}/autorizacoes".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_devolucoes_pagamentos(
        self,
        *,
        authorization: Optional[str] = None,
        gw_dev_app_key: Optional[str] = None,
        numero_convenio: int = None,
        numero_solicitacao_pagamento: Optional[int] = None,
        data_pagamento: Optional[str] = None,
        numero_ultima_devolucao: Optional[int] = None,
    ):
        """
        Lista as devoluções de uma solicitação de pagamento especifica ou as devoluções realizadas em uma data. Na requisição deve ser informada a data do pagamento ou a solicitação de pagamento.

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param numero_convenio: Número de Convênio do cliente com o BB Pay
            @param numero_solicitacao_pagamento: Numero Solicitacao Pagamento, só deve ser inserido se a data não for informada
            @param data_pagamento: Data das devoluções, só deve ser inserida se o número da solicitação de pagamento não for informado
            @param numero_ultima_devolucao: Número se referente ao ultimo valor de numeroDevolucao retornado na resposta anterior, e se este é o ultimo valor da pesquisa (medida necessária devido ao limite de resposta de 250 itens por requisição)
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if numero_solicitacao_pagamento is not None:
            query["numeroSolicitacaoPagamento"] = numero_solicitacao_pagamento
        if data_pagamento is not None:
            query["dataPagamento"] = data_pagamento
        if numero_ultima_devolucao is not None:
            query["numeroUltimaDevolucao"] = numero_ultima_devolucao
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/devolucoes-pagamentos".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
