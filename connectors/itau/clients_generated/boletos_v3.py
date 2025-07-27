"""
API Boletos (v3) v1.33.0
Api do produto de recebimentos Boletos de Cash Management (Francesa, Boletos e Notificações boleto)
"""

import requests
from typing import Optional


class BoletosV3Client:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def get_francesas(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: str = None,
        agencia: str = None,
        conta: str = None,
        dac: str = None,
        mes_referencia: Optional[str] = None,
    ):
        """
        Pesquisa das francesas disponíveis por Agência, Conta Corrente e Mês de Referência ou Data.

        Args:
            @param x_itau_apikey: Client_id gerado pela autenticação Oauth2 utilizado para autorizar o consumo de uma aplicação requisitante.
            @param x_itau_correlation_id: Identificador de correlação utilizado como um agrupar dentro da estrutura de audit trail e que permite relacionar uma mesma chamada passando em diversas aplicações/sistemas diferentes.
            @param agencia: 4 dígitos da agência.
            @param conta: 7 dígitos da conta corrente.
            @param dac: 1 dígito do dac
            @param mes_referencia: Mês de referência para consulta de datas disponíveis para visualização da francesa (formato mmyyyy). Não deve ser informado em conjunto com a Data.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta is not None:
            query["conta"] = conta
        if dac is not None:
            query["dac"] = dac
        if mes_referencia is not None:
            query["mes_referencia"] = mes_referencia
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        path_params = {}
        path_rendered = "/francesas".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_francesas_by_id_francesa_movimentacoes(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: str = None,
        data: str = None,
        tipo_cobranca: Optional[str] = None,
        tipo_movimentacao: Optional[str] = None,
        nosso_numero: Optional[str] = None,
        seu_numero: Optional[str] = None,
        numero_carteira: Optional[float] = None,
        id_francesa: float = None,
        nome_pagador: Optional[str] = None,
    ):
        """
        Lista de movimentações efetuadas na posição da francesa.

        Args:
            @param x_itau_apikey: Client_id gerado pela autenticação Oauth2 utilizado para autorizar o consumo de uma aplicação requisitante.
            @param x_itau_correlation_id: Identificador de correlação utilizado como um agrupar dentro da estrutura de audit trail e que permite relacionar uma mesma chamada passando em diversas aplicações/sistemas diferentes.
            @param data: Data da movimentação no formato yyyy-MM-dd
            @param tipo_cobranca: Tipo de Cobrança para efetuar o filtro desejado. Quando não informado, serão retornados todos. Opções: 'cobranca_digital', 'boleto', 'bolecode'
            @param tipo_movimentacao: Tipos de movimentação para efetuar o filtro desejado. Quando não informado, serão retornados todos. Opções 'entradas', 'liquidacoes', 'baixas'.
            @param nosso_numero: Consulta pelo nosso número específico
            @param seu_numero: Consulta pelo seu número específico
            @param numero_carteira: Consulta pelo número da carteira específica
            @param id_francesa: (4 dígitos agência)+(7 dígitos c/c)+(1 dígito do DAC)
            @param nome_pagador: Consulta pelo nome do pagador do título
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if data is not None:
            query["data"] = data
        if tipo_cobranca is not None:
            query["tipo_cobranca"] = tipo_cobranca
        if tipo_movimentacao is not None:
            query["tipo_movimentacao"] = tipo_movimentacao
        if nosso_numero is not None:
            query["nosso_numero"] = nosso_numero
        if seu_numero is not None:
            query["seu_numero"] = seu_numero
        if numero_carteira is not None:
            query["numero_carteira"] = numero_carteira
        if nome_pagador is not None:
            query["nome_pagador"] = nome_pagador
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        path_params = {}
        if id_francesa is not None:
            path_params["id_francesa"] = id_francesa
        path_rendered = "/francesas/{id_francesa}/movimentacoes".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_francesas_by_id_francesa_movimentacoes_resumidas(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: str = None,
        id_francesa: float = None,
        data: str = None,
    ):
        """
        Posição da francesa resumida de títulos de cobrança e títulos descontados.

        Args:
            @param x_itau_apikey: Client_id gerado pela autenticação Oauth2 utilizado para autorizar o consumo de uma aplicação requisitante.
            @param x_itau_correlation_id: Identificador de correlação utilizado como um agrupar dentro da estrutura de audit trail e que permite relacionar uma mesma chamada passando em diversas aplicações/sistemas diferentes.
            @param id_francesa: (4 dígitos agência)+(7 dígitos c/c)+(1 dígito do DAC)
            @param data: Data da movimentação no formato yyyy-MM-dd
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if data is not None:
            query["data"] = data
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        path_params = {}
        if id_francesa is not None:
            path_params["id_francesa"] = id_francesa
        path_rendered = "/francesas/{id_francesa}/movimentacoes_resumidas".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_boletos(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: str = None,
        x_itau_flowid: Optional[str] = None,
        codigo_carteira: Optional[str] = None,
        data_inicial: str = None,
        data_final: str = None,
        id_beneficiario: str = None,
        nome_pagador: Optional[str] = None,
        numero_cpf_cnpj_pagador: Optional[float] = None,
        numero_nosso_numero: Optional[float] = None,
        seu_numero: Optional[str] = None,
        situacao_geral_boleto: Optional[str] = None,
        situacao_negativacao: Optional[str] = None,
        situacao_protesto: Optional[str] = None,
        status_vencimento: Optional[str] = None,
        tipo_boleto: Optional[str] = None,
        tipo_data: str = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ):
        """
        Consulta lista de boletos por critérios específicos.

        Args:
            @param x_itau_apikey: Client_id gerado pela autenticação Oauth2 utilizado para autorizar o consumo de uma aplicação requisitante.
            @param x_itau_correlation_id: Identificador de correlação utilizado como um agrupar dentro da estrutura de audit trail e que permite relacionar uma mesma chamada passando em diversas aplicações/sistemas diferentes.
            @param x_itau_flowid: Key que identifica o fluxo
            @param codigo_carteira: Número da carteira utilizada na emissão do boleto
            @param data_inicial: Data inicial da pesquisa
            @param data_final: Data final da pesquisa
            @param id_beneficiario: (4 dígitos agência)(5 dígitos c/c)+(1 dígito DAC)
            @param nome_pagador: Nome do destinatário do boleto, pode ser informado apenas uma parte do nome para pesquisa, todavia, será pesquisado somente a frente do nome
            @param numero_cpf_cnpj_pagador: Número do CPF ou CNPJ do destinatário do boleto. Deve ser informado apenas números
            @param numero_nosso_numero: Nosso número informado na emissão do boleto, importante, sempre o último digito será considerado como DAC
            @param seu_numero: Seu número, informado pelo beneficiário de cobrança, do boleto de cobrança, provido do processor-boleto.
            @param situacao_geral_boleto: Status do boleto a ser filtrado. São aceitos somente os valores (chave) retornados no end-point de configuração na chave 'filtro_situacao_geral_boleto'.
            @param situacao_negativacao: Informa a situação da negativação do boleto. São aceitos somente os valores (chave) retornados no end-point de configuração na chave 'filtro_situacao_negativacao'.
            @param situacao_protesto: Informa a situação do protesto do boleto. São aceitos somente os valores (chave) retornados no end-point de configuração na chave 'filtro_situacao_protesto'.
            @param status_vencimento: São aceitos somente os valores (chave) retornados no end-point de configuração na chave 'filtro_status_vencimento'.
            @param tipo_boleto: Informa o tipo de boleto a ser pesquisado. São aceitos somente os valores (chave) retornados no end-point de configuração na chave 'filtro_tipo_boleto'.
            @param tipo_data: Campo que indica onde a pesquisa será realizada, na data de emissão ou na data de vencimento. São aceitos somente os valores (chave) retornados no end-point de configuração na chave 'filtro_tipo_data'.
            @param page: Definir um número de página para obter informações desta coleção
            @param page_size: Limitar o número de elementos por página
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if codigo_carteira is not None:
            query["codigo_carteira"] = codigo_carteira
        if data_inicial is not None:
            query["data_inicial"] = data_inicial
        if data_final is not None:
            query["data_final"] = data_final
        if id_beneficiario is not None:
            query["id_beneficiario"] = id_beneficiario
        if nome_pagador is not None:
            query["nome_pagador"] = nome_pagador
        if numero_cpf_cnpj_pagador is not None:
            query["numero_cpf_cnpj_pagador"] = numero_cpf_cnpj_pagador
        if numero_nosso_numero is not None:
            query["numero_nosso_numero"] = numero_nosso_numero
        if seu_numero is not None:
            query["seu_numero"] = seu_numero
        if situacao_geral_boleto is not None:
            query["situacao_geral_boleto"] = situacao_geral_boleto
        if situacao_negativacao is not None:
            query["situacao_negativacao"] = situacao_negativacao
        if situacao_protesto is not None:
            query["situacao_protesto"] = situacao_protesto
        if status_vencimento is not None:
            query["status_vencimento"] = status_vencimento
        if tipo_boleto is not None:
            query["tipo_boleto"] = tipo_boleto
        if tipo_data is not None:
            query["tipo_data"] = tipo_data
        if page is not None:
            query["page"] = page
        if page_size is not None:
            query["page_size"] = page_size
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
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

    def post_notificacoes_boletos(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
               Este endpoint tem como objetivo realizar o cadastro da url, credenciais e preferências para notificações das movimentações de baixa operacional e/ou liquidação dos boletos. Abaixo estão listados os parâmetros obrigatórios exigidos e a descrição deles. O cadastro pode ser realizado para baixa operacional e/ou efetiva (liquidação).
        <br></br>
        <b>Importante:</b> Para obter mais informações sobre x-itau-apikey e o x-itau-correlationID, acesse o tópico: Como começar -> Autenticação em Produção -> Fluxos de autenticação Webhook.

               Args:
                   @param x_itau_apikey: Client_id gerado pela autenticação Oauth2 utilizado para autorizar o consumo de uma aplicação requisitante.
                   @param x_itau_correlation_id: Identificador de correlação utilizado como um agrupar dentro da estrutura de audit trail e que permite relacionar uma mesma chamada passando em diversas aplicações/sistemas diferentes.
                   @param authorization: Token de acesso (JWT)
                   @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/notificacoes_boletos".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_notificacoes_boletos(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: str = None,
        authorization: str = None,
        id_beneficiario: str = None,
    ):
        """
        Retorna uma lista de notificações que foram cadastradas.

        Args:
            @param x_itau_apikey: Client_id gerado pela autenticação Oauth2 utilizado para autorizar o consumo de uma aplicação requisitante.
            @param x_itau_correlation_id: Identificador de correlação utilizado como um agrupar dentro da estrutura de audit trail e que permite relacionar uma mesma chamada passando em diversas aplicações/sistemas diferentes.
            @param authorization: Token de acesso (JWT)
            @param id_beneficiario: 4 dígitos da agência concatenado com os 7 dígitos da conta corrente e 1 dígito do DAC .
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if id_beneficiario is not None:
            query["id_beneficiario"] = id_beneficiario
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/notificacoes_boletos".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_notificacoes_boletos_by_id_notificacao_boleto(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: str = None,
        authorization: str = None,
        id_notificacao_boleto: str = None,
    ):
        """
        Exclui uma notificação que está cadastrada.

        Args:
            @param x_itau_apikey: Client_id gerado pela autenticação Oauth2 utilizado para autorizar o consumo de uma aplicação requisitante.
            @param x_itau_correlation_id: Identificador de correlação utilizado como um agrupar dentro da estrutura de audit trail e que permite relacionar uma mesma chamada passando em diversas aplicações/sistemas diferentes.
            @param authorization: Token de acesso (JWT)
            @param id_notificacao_boleto: Identificador do registro de notificação do boleto. Composto por Agência (4) + Conta (7) + DAC (1) + Cód. Tipo Notificação (2) Tipos de notificação: 01 - Baixa Efetiva; 02 - Baixa Operacional
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id_notificacao_boleto is not None:
            path_params["id_notificacao_boleto"] = id_notificacao_boleto
        path_rendered = "/notificacoes_boletos/{id_notificacao_boleto}".format(
            **path_params
        )
        response = requests.delete(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_notificacoes_boletos_by_id_notificacao_boleto(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: str = None,
        authorization: str = None,
        id_notificacao_boleto: str = None,
        body: dict = None,
    ):
        """
        Atualiza uma notificação que está cadastrada.

        Args:
            @param x_itau_apikey: Client_id gerado pela autenticação Oauth2 utilizado para autorizar o consumo de uma aplicação requisitante.
            @param x_itau_correlation_id: Identificador de correlação utilizado como um agrupar dentro da estrutura de audit trail e que permite relacionar uma mesma chamada passando em diversas aplicações/sistemas diferentes.
            @param authorization: Token de acesso (JWT)
            @param id_notificacao_boleto: Identificador do registro de notificação do boleto. Composto por Agência (4) + Conta (7) + DAC (1) + Cód. Tipo Notificação (2) Tipos de notificação: 01 - Baixa Efetiva; 02 - Baixa Operacional
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id_notificacao_boleto is not None:
            path_params["id_notificacao_boleto"] = id_notificacao_boleto
        path_rendered = "/notificacoes_boletos/{id_notificacao_boleto}".format(
            **path_params
        )
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()
