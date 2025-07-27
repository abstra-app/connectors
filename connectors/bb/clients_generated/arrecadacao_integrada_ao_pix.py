"""
PIX-BB v1.9
API para gerenciar os serviços referentes ao PIX (Sistema de Pagamentos Instantâneos) no BB.
"""

import requests


class ArrecadacaoIntegradaAoPixClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_arrecadacao_qrcodes(
        self, *, gw_app_key: str = None, authorization: str = None, body: dict = None
    ):
        """
                Gera um QR Code de pagamento instantâneo (PIX) para uma guia de arrecadação (com ou sem código de barras).

                Args:
                    @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo. Em produção o nome do parâmetro deve ser alterado para gw-dev-app-key.
                    @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
        Ex: Bearer [ACCESS_TOKEN]
                    @param body: No description provided.
        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/arrecadacao-qrcodes".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_arrecadacao_qrcodes(
        self,
        *,
        authorization: str = None,
        gw_app_key: str = None,
        numero_convenio: int = None,
        codigo_guia_recebimento: str = None,
    ):
        """
        Consulta um QR Code de pagamentos instantâneos (PIX) por guia de recebimento (com ou sem código de barras).

        Args:
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.Ex: Bearer [ACCESS_TOKEN]
            @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo. Em produção o nome do parâmetro deve ser alterado para gw-dev-app-key.
            @param numero_convenio: Número do convenio registrado no Banco do Brasil.  No ambiente de testes utilize o número de convênio de arrecadação: 78806
            @param codigo_guia_recebimento: Código de Barras  ou outro identificador do cliente informado no momento da criação da solicitação de pagamento.
        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        if codigo_guia_recebimento is not None:
            query["codigoGuiaRecebimento"] = codigo_guia_recebimento
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/arrecadacao-qrcodes".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_arrecadacao_qrcodes_by_id(
        self,
        *,
        gw_app_key: str = None,
        authorization: str = None,
        id: str = None,
        body: dict = None,
    ):
        """
                Altera um QR Code de pagamento instantâneo (PIX) de uma guia de arrecadação (com ou sem código de barras).

                Args:
                    @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo. Em produção o nome do parâmetro deve ser alterado para gw-dev-app-key.
                    @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
        Ex: Bearer [ACCESS_TOKEN]
                    @param id: Identificador da transação. O objetivo desse campo é ser um elemento que possibilite ao PSP do recebedor apresentar ao usuário recebedor a funcionalidade de conciliação de pagamentos.

        Na pacs.008, é referenciado como TransactionIdentification <txId> ou idConciliacaoRecebedor. O preenchimento do campo txid é limitado a 35 caracteres na pacs.008.

        Em termos de fluxo de funcionamento, o txid é lido pelo aplicativo do PSP do pagador e, depois de confirmado o pagamento, é enviado para o SPI via pacs.008. Uma pacs.008 também é enviada ao PSP do recebedor, contendo, além de todas as informações usuais do pagamento, o txid. Ao perceber um recebimento dotado de txid, o PSP do recebedor está apto a se comunicar com o usuário recebedor, informando que um pagamento específico foi liquidado.

                    @param body: No description provided.
        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/arrecadacao-qrcodes/{id}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_arrecadacao_qrcodes_by_id(
        self,
        *,
        authorization: str = None,
        gw_app_key: str = None,
        numero_convenio: int = None,
        id: str = None,
    ):
        """
                Consulta um QR Code de pagamento instantâneo (PIX) de uma guia de arrecadação (com ou sem código de barras).

                Args:
                    @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
        Ex: Bearer [ACCESS_TOKEN]
                    @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo. Em produção o nome do parâmetro deve ser alterado para gw-dev-app-key.
                    @param numero_convenio: Número do convenio registrado no Banco do Brasil.  No ambiente de testes utilize o número de convênio de arrecadação: 78806
                    @param id: Identificador da transação. O objetivo desse campo é ser um elemento que possibilite ao PSP do recebedor apresentar ao usuário recebedor a funcionalidade de conciliação de pagamentos.

        Na pacs.008, é referenciado como TransactionIdentification <txId> ou idConciliacaoRecebedor. O preenchimento do campo txid é limitado a 35 caracteres na pacs.008.

        Em termos de fluxo de funcionamento, o txid é lido pelo aplicativo do PSP do pagador e, depois de confirmado o pagamento, é enviado para o SPI via pacs.008. Uma pacs.008 também é enviada ao PSP do recebedor, contendo, além de todas as informações usuais do pagamento, o txid. Ao perceber um recebimento dotado de txid, o PSP do recebedor está apto a se comunicar com o usuário recebedor, informando que um pagamento específico foi liquidado.

        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/arrecadacao-qrcodes/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_arrecadacao_qrcodes_by_id_baixar(
        self,
        *,
        gw_app_key: str = None,
        authorization: str = None,
        id: str = None,
        body: dict = None,
    ):
        """
                Dar baixa em um QR Code de pagamento instantâneo (PIX) de uma guia de arrecadação (com ou sem código de barras).

                Args:
                    @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo. Em produção o nome do parâmetro deve ser alterado para gw-dev-app-key.
                    @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
        Ex: Bearer [ACCESS_TOKEN]
                    @param id: Identificador da transação. O objetivo desse campo é ser um elemento que possibilite ao PSP do recebedor apresentar ao usuário recebedor a funcionalidade de conciliação de pagamentos.Na pacs.008, é referenciado como TransactionIdentification <txId> ou idConciliacaoRecebedor. O preenchimento do campo txid é limitado a 35 caracteres na pacs.008.Em termos de fluxo de funcionamento, o txid é lido pelo aplicativo do PSP do pagador e, depois de confirmado o pagamento, é enviado para o SPI via pacs.008. Uma pacs.008 também é enviada ao PSP do recebedor, contendo, além de todas as informações usuais do pagamento, o txid. Ao perceber um recebimento dotado de txid, o PSP do recebedor está apto a se comunicar com o usuário recebedor, informando que um pagamento específico foi liquidado.
                    @param body: No description provided.
        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/arrecadacao-qrcodes/{id}/baixar".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_arrecadacao_qrcodes_pagamentos_by_id(
        self, *, authorization: str = None, gw_app_key: str = None, id: str = None
    ):
        """
        A partir do código de pagamento, consulta dados do registro de Pagamento PIX QRCode de uma Guia de Arrecadação

        Args:
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.Ex: Bearer [ACCESS_TOKEN]
            @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo. Em produção o nome do parâmetro deve ser alterado para gw-dev-app-key.
            @param id: EndToEndIdentification que transita na PACS002, PACS004 e PACS008
        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/arrecadacao-qrcodes/pagamentos/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos_codigo_barras_by_id(
        self,
        *,
        authorization: str = None,
        gw_app_key: str = None,
        numero_convenio: int = None,
        id: str = None,
    ):
        """
        Retorna uma lista de pagamentos Pix na arrecadação quando informado o código de barras.

        Args:
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.Ex: Bearer [ACCESS_TOKEN]
            @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo. Em produção o nome do parâmetro deve ser alterado para gw-dev-app-key.
            @param numero_convenio: Número do convenio registrado no Banco do Brasil.  No ambiente de testes utilize o número de convênio de arrecadação: 78806
            @param id: Texto código de barras.
        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/pagamentos/codigo-barras/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos_transacao_by_id(
        self,
        *,
        authorization: str = None,
        gw_app_key: str = None,
        numero_convenio: int = None,
        id: int = None,
    ):
        """
        Retorna uma lista de pagamentos Pix na arrecadação quando informado o ID de transação.

        Args:
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.Ex: Bearer [ACCESS_TOKEN]
            @param gw_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo. Em produção o nome do parâmetro deve ser alterado para gw-dev-app-key.
            @param numero_convenio: Número do convenio registrado no Banco do Brasil.  No ambiente de testes utilize o número de convênio de arrecadação: 78806
            @param id: Identificador da transação. O objetivo desse campo é ser um elemento que possibilite ao PSP do recebedor apresentar ao usuário recebedor a funcionalidade de conciliação de pagamentos.Na pacs.008, é referenciado como TransactionIdentification <txId> ou idConciliacaoRecebedor. O preenchimento do campo txid é limitado a 35 caracteres na pacs.008.Em termos de fluxo de funcionamento, o txid é lido pelo aplicativo do PSP do pagador e, depois de confirmado o pagamento, é enviado para o SPI via pacs.008. Uma pacs.008 também é enviada ao PSP do recebedor, contendo, além de todas as informações usuais do pagamento, o txid. Ao perceber um recebimento dotado de txid, o PSP do recebedor está apto a se comunicar com o usuário recebedor, informando que um pagamento específico foi liquidado.
        """
        query = {}
        if gw_app_key is not None:
            query["gw-app-key"] = gw_app_key
        if numero_convenio is not None:
            query["numeroConvenio"] = numero_convenio
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/pagamentos/transacao/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
