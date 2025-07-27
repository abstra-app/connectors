"""
BB Pay API v2 v2.0.0
O sistema BB Pay do Banco do Brasil é uma solução que permite o recebimento de valores por intermédio de diversos meios de pagamento. Ao se integrar com o BB Pay, você pode habilitar diversos meios de pagamento para disponibilizá-los a um cliente (pagador), conforme a necessidade de seu negócio e da venda em questão.

Esta API permite o gerenciamento e consultas de pagamentos e recebimentos de clientes PJ BB que utilizam o BB Pay.
"""

import requests
from typing import Optional


class BbPayV2Client:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def get_solicitacoes(
        self,
        *,
        numero_convenio: int = None,
        codigo_conciliacao_solicitacao: Optional[str] = None,
        data_solicitacao: Optional[str] = None,
        codigo_estado_solicitacao: Optional[list] = None,
        token_paginacao: Optional[str] = None,
        itens_por_pagina: Optional[int] = None,
        numero_participante: Optional[int] = None,
        authorization: Optional[str] = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param codigo_conciliacao_solicitacao: Código de conciliação informado pelo convênio na criação da solicitação
            @param data_solicitacao: Data de criação das solicitações
            @param codigo_estado_solicitacao: Lista de códigos de estado das solicitações
            @param token_paginacao: Token para continuação de pesquisa (paginação)
            @param itens_por_pagina: Número de itens retornados na consulta
            @param numero_participante: Número identificador único do Participante
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if codigo_conciliacao_solicitacao is not None:
            query["codigoConciliacaoSolicitacao"] = codigo_conciliacao_solicitacao
        if data_solicitacao is not None:
            query["dataSolicitacao"] = data_solicitacao
        if codigo_estado_solicitacao is not None:
            query["codigoEstadoSolicitacao"] = codigo_estado_solicitacao
        if token_paginacao is not None:
            query["tokenPaginacao"] = token_paginacao
        if itens_por_pagina is not None:
            query["itensPorPagina"] = itens_por_pagina
        if numero_participante is not None:
            query["numeroParticipante"] = numero_participante
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/solicitacoes".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_solicitacoes(
        self,
        *,
        authorization: Optional[str] = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """


        Args:
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/solicitacoes".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos_by_numero_pagamento(
        self,
        *,
        numero_pagamento: int = None,
        numero_convenio: int = None,
        authorization: Optional[str] = None,
        numero_pagamento: int = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param numero_pagamento: Número identificador do pagamento
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_pagamento: Número identificador do pagamento
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_pagamento is not None:
            path_params["numeroPagamento"] = numero_pagamento
        if numero_pagamento is not None:
            path_params["numeroPagamento"] = numero_pagamento
        path_rendered = "/pagamentos/{numeroPagamento}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos(
        self,
        *,
        numero_convenio: int = None,
        numero_solicitacao: Optional[int] = None,
        codigo_conciliacao_solicitacao: Optional[str] = None,
        codigo_tipo_pagamento: Optional[list] = None,
        codigo_estado_pagamento: Optional[list] = None,
        data_pagamento: Optional[str] = None,
        numero_documento_pagador: Optional[int] = None,
        token_paginacao: Optional[str] = None,
        itens_por_pagina: Optional[int] = None,
        authorization: Optional[str] = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param numero_solicitacao: Número identificador da solicitação
            @param codigo_conciliacao_solicitacao: Código de conciliacao da solicitação de pagamento

            @param codigo_tipo_pagamento: Lista de códigos de tipo dos pagamentos
            @param codigo_estado_pagamento: Lista de códigos de estado dos pagamentos
            @param data_pagamento: Data do pagamento
            @param numero_documento_pagador: Número do CPF ou CNPJ do pagador
            @param token_paginacao: Token para continuação de pesquisa (paginação)
            @param itens_por_pagina: Limite de itens por pagina
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if numero_solicitacao is not None:
            query["numeroSolicitacao"] = numero_solicitacao
        if codigo_conciliacao_solicitacao is not None:
            query["codigoConciliacaoSolicitacao"] = codigo_conciliacao_solicitacao
        if codigo_tipo_pagamento is not None:
            query["codigoTipoPagamento"] = codigo_tipo_pagamento
        if codigo_estado_pagamento is not None:
            query["codigoEstadoPagamento"] = codigo_estado_pagamento
        if data_pagamento is not None:
            query["dataPagamento"] = data_pagamento
        if numero_documento_pagador is not None:
            query["numeroDocumentoPagador"] = numero_documento_pagador
        if token_paginacao is not None:
            query["tokenPaginacao"] = token_paginacao
        if itens_por_pagina is not None:
            query["itensPorPagina"] = itens_por_pagina
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
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

    def get_devolucoes_by_numero_devolucao(
        self,
        *,
        numero_convenio: int = None,
        authorization: Optional[str] = None,
        numero_devolucao: int = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay

            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_devolucao: Número identificador da devolução
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_devolucao is not None:
            path_params["numeroDevolucao"] = numero_devolucao
        path_rendered = "/devolucoes/{numeroDevolucao}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_devolucoes(
        self,
        *,
        numero_convenio: int = None,
        numero_pagamento: Optional[int] = None,
        data_devolucao: Optional[str] = None,
        token_paginacao: Optional[str] = None,
        itens_por_pagina: Optional[int] = None,
        gw_dev_app_key: str = None,
        authorization: Optional[str] = None,
    ):
        """
        No description provided.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param numero_pagamento: Número identificador do pagamento
            @param data_devolucao: Data da devolução
            @param token_paginacao: Token para continuação de pesquisa (paginação)
            @param itens_por_pagina: Número de itens retornados na consulta
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
            @param authorization: Token de acesso fornecido pelo OAuth BB.
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if numero_pagamento is not None:
            query["numeroPagamento"] = numero_pagamento
        if data_devolucao is not None:
            query["dataDevolucao"] = data_devolucao
        if token_paginacao is not None:
            query["tokenPaginacao"] = token_paginacao
        if itens_por_pagina is not None:
            query["itensPorPagina"] = itens_por_pagina
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/devolucoes".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_devolucoes(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: Optional[str] = None,
        body: dict = None,
    ):
        """
        No description provided.

        Args:
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/devolucoes".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_participantes(
        self,
        *,
        numero_convenio: int = None,
        codigo_estado_participante: Optional[list] = None,
        itens_por_pagina: Optional[int] = None,
        token_paginacao: Optional[str] = None,
        numero_solicitacao: Optional[int] = None,
        authorization: Optional[str] = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param codigo_estado_participante: Código do estado do Participante. (0 - Ativo, 1 - Pendente, 900 - Cancelado)
            @param itens_por_pagina: Número de itens retornados na consulta
            @param token_paginacao: Token para continuação de pesquisa (paginação)
            @param numero_solicitacao: Número identificador da solicitação de pagamento
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if codigo_estado_participante is not None:
            query["codigoEstadoParticipante"] = codigo_estado_participante
        if itens_por_pagina is not None:
            query["itensPorPagina"] = itens_por_pagina
        if token_paginacao is not None:
            query["tokenPaginacao"] = token_paginacao
        if numero_solicitacao is not None:
            query["numeroSolicitacao"] = numero_solicitacao
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/participantes".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_participantes(
        self,
        *,
        authorization: Optional[str] = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
        No description provided.

        Args:
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/participantes".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_participantes_by_numero_participante(
        self,
        *,
        authorization: Optional[str] = None,
        numero_participante: int = None,
        numero_convenio: int = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_participante: Número identificador único do Participante
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_participante is not None:
            path_params["numeroParticipante"] = numero_participante
        path_rendered = "/participantes/{numeroParticipante}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_participantes_by_numero_participante(
        self,
        *,
        authorization: Optional[str] = None,
        numero_participante: int = None,
        numero_convenio: int = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
        Altera nome e/ou dados bancários de um participante

        Args:
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_participante: Número identificador único do Participante
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
            @param body: No description provided.
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_participante is not None:
            path_params["numeroParticipante"] = numero_participante
        path_rendered = "/participantes/{numeroParticipante}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def delete_participantes_by_numero_participante(
        self,
        *,
        authorization: Optional[str] = None,
        numero_participante: int = None,
        numero_convenio: int = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_participante: Número identificador único do Participante
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_participante is not None:
            path_params["numeroParticipante"] = numero_participante
        path_rendered = "/participantes/{numeroParticipante}".format(**path_params)
        response = requests.delete(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_openfinance_autorizacoes(
        self,
        *,
        authorization: Optional[str] = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
        Esse recurso inicia o fluxo de pagamento no Open Finance, após pagador escolher a instituição detentora da sua conta (marca). Enquanto o pagador espera o redirecionamento, esse recurso deve ser chamado para dar ciência à instituição detentora da conta do pagador de sua intenção, para que ela crie uma autorização (que será confirmada pelo pagador em ambiente de sua confiança)

        Args:
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/openfinance/autorizacoes".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_openfinance_autorizacoes_by_numero_pagamento(
        self,
        *,
        numero_convenio: float = None,
        authorization: Optional[str] = None,
        numero_pagamento: float = None,
        gw_dev_app_key: str = None,
    ):
        """
        Esse recurso verifica se a autorização foi criada pela instituição escolhida pelo pagador e, em caso positivo, devolve a url para direcionamento do pagador ao ambiente da instituição escolhida, por ela fornecida

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay

            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_pagamento: Número do pagamento da solicitação que foi autorizado
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_pagamento is not None:
            path_params["numeroPagamento"] = numero_pagamento
        path_rendered = "/openfinance/autorizacoes/{numeroPagamento}".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_openfinance_marcas_ativas(
        self,
        *,
        numero_convenio: float = None,
        token_paginacao: Optional[str] = None,
        authorization: Optional[str] = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param token_paginacao: Token para continuação de pesquisa (paginação)
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if token_paginacao is not None:
            query["tokenPaginacao"] = token_paginacao
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/openfinance/marcas-ativas".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_solicitacoes_by_numero_solicitacao(
        self,
        *,
        numero_convenio: int = None,
        authorization: Optional[str] = None,
        numero_solicitacao: int = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_solicitacao: Número identificador da solicitação de pagamento
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_solicitacao is not None:
            path_params["numeroSolicitacao"] = numero_solicitacao
        path_rendered = "/solicitacoes/{numeroSolicitacao}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_solicitacoes_by_numero_solicitacao(
        self,
        *,
        numero_convenio: int = None,
        authorization: Optional[str] = None,
        numero_solicitacao: int = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
        Altera data de vencimento, data limite para pagamento, valor e/ou descrição de uma solicitação de pagamento, bem como o QRCode Pix e o boleto associados à solicitação. Não é possível fazer alterações em solicitações com split de valor fixo.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_solicitacao: Número identificador da solicitação de pagamento
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
            @param body: No description provided.
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_solicitacao is not None:
            path_params["numeroSolicitacao"] = numero_solicitacao
        path_rendered = "/solicitacoes/{numeroSolicitacao}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def delete_solicitacoes_by_numero_solicitacao(
        self,
        *,
        numero_convenio: int = None,
        authorization: Optional[str] = None,
        numero_solicitacao: int = None,
        gw_dev_app_key: str = None,
    ):
        """
        No description provided.

        Args:
            @param numero_convenio: Número do convênio do cliente no BB Pay
            @param authorization: Token de acesso fornecido pelo OAuth BB.
            @param numero_solicitacao: Número identificador da solicitação de pagamento
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo
        """
        query = {}
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if numero_solicitacao is not None:
            path_params["numeroSolicitacao"] = numero_solicitacao
        path_rendered = "/solicitacoes/{numeroSolicitacao}".format(**path_params)
        response = requests.delete(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
