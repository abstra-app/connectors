"""
Cobranças API v2.20.0
API para gerenciar os serviços de cobranças de cliente do Banco do Brasil S.A.
"""

import requests
from typing import Optional


class CobrancasClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def get_boletos(
        self,
        *,
        indicador_situacao: str = None,
        conta_caucao: Optional[int] = None,
        agencia_beneficiario: int = None,
        conta_beneficiario: int = None,
        carteira_convenio: Optional[int] = None,
        variacao_carteira_convenio: Optional[int] = None,
        modalidade_cobranca: Optional[int] = None,
        cnpj_pagador: Optional[int] = None,
        digito_cnpj_pagador: Optional[int] = None,
        cpf_pagador: Optional[int] = None,
        digito_cpf_pagador: Optional[int] = None,
        data_inicio_vencimento: Optional[str] = None,
        data_fim_vencimento: Optional[str] = None,
        data_inicio_registro: Optional[str] = None,
        data_fim_registro: Optional[str] = None,
        data_inicio_movimento: Optional[str] = None,
        data_fim_movimento: Optional[str] = None,
        codigo_estado_titulo_cobranca: Optional[int] = None,
        boleto_vencido: Optional[str] = None,
        indice: Optional[int] = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
    ):
        """
                Listar títulos de cobrança - Em Ser, Baixados, Liquidados e Com Protesto por Beneficiário.<br /><br />Se você deseja receber informações quando seu boleto foi pago ou cancelado imediatamente, conheça nosso **serviço de notificação automática (Webhook)**, documentado abaixo.

                Args:
                    @param indicador_situacao: Situação do boleto. Campo obrigatoriamente MAIÚSCULO.
        Domínios:
        A - Em ser
        B - Baixados/Protestados/Liquidados
                    @param conta_caucao: Número da conta caução.

        Domínio:
        1 - Compõe Garantia;
        2 - Não Compõe Garantia;
        4 - Não Compõe Garantia (vencimento superior a 180 dias);
        5 - Não Compõe Garantia (Vedado);
        6 - Em análise;
        7 - Em análise;
        8 - Não Compõe Garantia.
                    @param agencia_beneficiario: Número da agência do beneficiário, sem o dígito verificador. Ex: 452. CAMPO OBRIGATÓRIO.
                    @param conta_beneficiario: Número da conta do beneficiário, sem o dígito verificador. Ex: 123873. CAMPO OBRIGATÓRIO.
                    @param carteira_convenio: Número da carteira do convênio de cobrança. Ex: 17
                    @param variacao_carteira_convenio: Número da variação da carteira do convênio de cobrança. Ex: 35
                    @param modalidade_cobranca: Código para identificar a característica dos boletos dentro das modalidades de cobrança existentes no BB.
        Domínio:
        1 - SIMPLES COM REGISTRO
        2 - SIMPLES SEM REGISTRO
        4 - VINCULADA
        6 - DESCONTADA
        8 - FINANCIADA VENDOR
                    @param cnpj_pagador: CNPJ do pagador
        Ex: 123456789012
                    @param digito_cnpj_pagador: Dígito verificador do CNPJ do pagador
        Ex: 12
                    @param cpf_pagador: CPF do pagador sem o dígito. Ex: 711285901
                    @param digito_cpf_pagador: Dígito verificador do CPF do pagador. Ex: 82
                    @param data_inicio_vencimento: Data inicial de vencimento do boleto que delimita o período da consulta. Campo não obrigatório. Se informado Data Início, deixando em branco a Data Fim, o sistema deve assumir a data atual como Data Fim. Ex: 22.04.2020
                    @param data_fim_vencimento: Data final de vencimento do boleto que delimita o período da consulta - deverá ser maior que a data de início. Campo não obrigatório. Se informado, deverá ser preenchido dataInicioVencimento. Ex: 28.04.2020
                    @param data_inicio_registro: Data inicial do registro do boleto que delimita o período da consulta. Ex: 22.04.2020
                    @param data_fim_registro: Data final do registro do boleto que delimita o período da consulta - deverá ser maior que a data de início. Campo não obrigatório. Se informado, deverá ser preenchido dataInicioRegistro. Ex: 28.04.2020
                    @param data_inicio_movimento: Delimita o período da consulta  de boletos liquidados, baixados ou protestados, caso seja informado, no campo codigoEstadoTituloCobranca os códigos 05, 06, 07 ou 09. Ex: 22.04.2020
                    @param data_fim_movimento: Data final do movimento que delimita o período da consulta  de boletos liquidados, baixados ou protestados, caso seja informado, no campo codigoEstadoTituloCobranca os códigos 05, 06, 07 ou 09. Data fim deverá ser maior que a data de início. Campo não obrigatório. Se informado, deverá ser preenchido dataInicioMovimento. Ex: 28.04.2020
                    @param codigo_estado_titulo_cobranca: Código da situação atual do boleto.

        Domínios:

        01 - NORMAL
        02 - MOVIMENTO CARTORIO
        03 - EM CARTORIO
        04 - TITULO COM OCORRENCIA DE CARTORIO
        05 - PROTESTADO ELETRONICO
        06 - LIQUIDADO
        07 - BAIXADO
        09 - TITULO PROTESTADO MANUAL
        10 - TITULO BAIXADO/PAGO EM CARTORIO
        11 - TITULO LIQUIDADO/PROTESTADO
        12 - TITULO LIQUIDADO/PAGO CARTORIO
        13 - TITULO PROTESTADO AGUARDANDO BAIXA
        18 - PAGO PARCIALMENTE
                    @param boleto_vencido: Indica se o Boleto está vencido ou não. Campo obrigatoriamente MAIÚSCULO.
        Domínio:
        S para boletos vencidos
        N para boletos não vencidos
                    @param indice: Somente deve ser utilizado em caso de pesquisas que retornem mais de 300 boletos. Caso o campo RPST "Indicador Continuidade" retorne com o valor "S", o usuário deve informar o conteúdo do campo RPST "Numero Ultimo Registro" a partir do qual será iniciada nova consulta.

                    @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
                    @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
        """
        query = {}
        if indicador_situacao is not None:
            query["indicadorSituacao"] = indicador_situacao
        if conta_caucao is not None:
            query["contaCaucao"] = conta_caucao
        if agencia_beneficiario is not None:
            query["agenciaBeneficiario"] = agencia_beneficiario
        if conta_beneficiario is not None:
            query["contaBeneficiario"] = conta_beneficiario
        if carteira_convenio is not None:
            query["carteiraConvenio"] = carteira_convenio
        if variacao_carteira_convenio is not None:
            query["variacaoCarteiraConvenio"] = variacao_carteira_convenio
        if modalidade_cobranca is not None:
            query["modalidadeCobranca"] = modalidade_cobranca
        if cnpj_pagador is not None:
            query["cnpjPagador"] = cnpj_pagador
        if digito_cnpj_pagador is not None:
            query["digitoCNPJPagador"] = digito_cnpj_pagador
        if cpf_pagador is not None:
            query["cpfPagador"] = cpf_pagador
        if digito_cpf_pagador is not None:
            query["digitoCPFPagador"] = digito_cpf_pagador
        if data_inicio_vencimento is not None:
            query["dataInicioVencimento"] = data_inicio_vencimento
        if data_fim_vencimento is not None:
            query["dataFimVencimento"] = data_fim_vencimento
        if data_inicio_registro is not None:
            query["dataInicioRegistro"] = data_inicio_registro
        if data_fim_registro is not None:
            query["dataFimRegistro"] = data_fim_registro
        if data_inicio_movimento is not None:
            query["dataInicioMovimento"] = data_inicio_movimento
        if data_fim_movimento is not None:
            query["dataFimMovimento"] = data_fim_movimento
        if codigo_estado_titulo_cobranca is not None:
            query["codigoEstadoTituloCobranca"] = codigo_estado_titulo_cobranca
        if boleto_vencido is not None:
            query["boletoVencido"] = boleto_vencido
        if indice is not None:
            query["indice"] = indice
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/boletos".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_boletos(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
        Permite incluir um novo boleto de cobrança

        Args:
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/boletos".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_boletos_by_id(
        self,
        *,
        id: str = None,
        numero_convenio: float = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
    ):
        """
        Consulta detalhes de um boleto bancário.<br /><br />Se você deseja receber informações quando seu boleto foi pago ou cancelado imediatamente, conheça nosso **serviço de notificação automática (Webhook)**, documentado abaixo.<br /><br /><b>Observação:</b> Ao consultar o mesmo boleto mais de uma vez em um intervalo de até 30 segundos, a resposta fornecida será com as mesmas informações da consulta anterior. Isso garante mais velocidade e estabilidade para todos os clientes.

        Args:
            @param id: Número do título de cobrança.
            @param numero_convenio: Número do convênio.
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
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
        if id is not None:
            path_params["id"] = id
        path_rendered = "/boletos/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id(
        self,
        *,
        id: str = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
        Realiza alterações nos valores dos campos presentes em um boleto bancário já criado.

        Args:
            @param id: Número do título de cobrança.
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/boletos/{id}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_boletos_by_id_baixar(
        self,
        *,
        id: str = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
        Permite a baixa/cancelamento de um  título de cobrança.

        Args:
            @param id: Número do boleto bancário (único e exclusivo) que identifica o título e é usado para pagá-lo.
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/boletos/{id}/baixar".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_boletos_by_id_cancelar_pix(
        self,
        *,
        id: str = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
        Cancelar Pix vinculado a um boleto de cobrança existente.

        Args:
            @param id: Número de identificação do boleto (correspondente ao NOSSO NÚMERO, numeroTituloCliente), no formato STRING, com 20 dígitos, que deverá ser formatado da seguinte forma: “000” + (número do convênio com 7 dígitos) + (10 algarismos - se necessário, completar com zeros à esquerda). Campo Obrigatório.
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/boletos/{id}/cancelar-pix".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_boletos_by_id_gerar_pix(
        self,
        *,
        id: str = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
        Gerar Pix vinculado a um boleto de cobrança através de um QRCode Dinâmico ou Estático.

        Args:
            @param id: Número de identificação do boleto (correspondente ao NOSSO NÚMERO, numeroTituloCliente), no formato STRING, com 20 dígitos, que deverá ser formatado da seguinte forma: “000” + (número do convênio com 7 dígitos) + (10 algarismos - se necessário, completar com zeros à esquerda). Campo Obrigatório.
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/boletos/{id}/gerar-pix".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_boletos_by_id_pix(
        self,
        *,
        id: str = None,
        numero_convenio: float = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
    ):
        """
        Consultar os dados de um Pix vinculado a um boleto de cobrança.

        Args:
            @param id: Número de identificação do boleto (correspondente ao NOSSO NÚMERO, numeroTituloCliente), no formato STRING, com 20 dígitos, que deverá ser formatado da seguinte forma:  “000” +  (número do convênio com 7 dígitos) + (10 algarismos - se necessário, completar com zeros à esquerda). Campo Obrigatório.
            @param numero_convenio: Número do convênio de Cobrança do Cliente
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
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
        if id is not None:
            path_params["id"] = id
        path_rendered = "/boletos/{id}/pix".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_convenios_by_id_listar_retorno_movimento(
        self,
        *,
        id: str = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
        Lista os dados do retorno de movimento do convênio de Cobranças.<br /><br /><b>ATENÇÃO:</b> Este recurso faz parte de um programa piloto. Para obter acesso, entre em contato com seu Gerente de Cash ou Gerente de Relacionamento.

        Args:
            @param id: Número identificador do convênio de intercambio de dados em meio eletrônico, pelo qual serão fornecidos os dados dos títulos de um ou mais serviços de cobrança contratados.
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/convenios/{id}/listar-retorno-movimento".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_boletos_baixa_operacional(
        self,
        *,
        agencia: int = None,
        conta: int = None,
        carteira: int = None,
        variacao: int = None,
        estado_baixa_operacional: Optional[int] = None,
        modalidade_titulo: Optional[int] = None,
        data_inicio_vencimento_titulo: Optional[str] = None,
        data_fim_vencimento_titulo: Optional[str] = None,
        data_inicio_registro_titulo: Optional[str] = None,
        data_fim_registro_titulo: Optional[str] = None,
        data_inicio_agendamento_titulo: str = None,
        data_fim_agendamento_titulo: str = None,
        horario_inicio_agendamento_titulo: Optional[str] = None,
        horario_fim_agendamento_titulo: Optional[str] = None,
        id_proximo_titulo: Optional[str] = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
    ):
        """
                Lista as informações de baixa operacional de boletos de uma carteira de cobrança.<br /><br />Se você deseja receber informações quando seu boleto foi pago ou cancelado imediatamente, conheça nosso **serviço de notificação automática (Webhook)**, documentado abaixo.<br /><br />_Observação_: A utilização do recurso depende da habilitação através do PATCH /convenios/{id}/ativar-consulta-baixa-operacional.<br />Para desativar o o recurso, utilize o PATCH /convenios/{id}/desativar-consulta-baixa-operacional.

                Args:
                    @param agencia: Número da agência do beneficiário, sem o dígito verificador.
                    @param conta: Número da conta do beneficiário, sem o dígito verificador.
                    @param carteira: Número da carteira do convênio de cobrança.
                    @param variacao: Número da variação da carteira do convênio de cobrança.
                    @param estado_baixa_operacional: Código para identificar o estado da baixa operacional. Domínio:1 - BAIXA OPERACIONAL BB; 2 - BAIXA OPERACIONAL OUTROS BANCOS; 10- CANCELAMENTO DE BAIXA OPERACIONAL
                    @param modalidade_titulo: Código para identificar a característica dos boletos dentro das modalidades de cobrança existentes no banco.

        Domínio:
        1 - SIMPLES
        4 - VINCULADA
                    @param data_inicio_vencimento_titulo: Data de vencimento inicial para delimitar período da consulta.
                    @param data_fim_vencimento_titulo: Data de vencimento final para delimitar período da consulta.
                    @param data_inicio_registro_titulo: Data de registro inicial para delimitar período da consulta.
                    @param data_fim_registro_titulo: Data de registro final para delimitar período da consulta.
                    @param data_inicio_agendamento_titulo: Data de agendamento inicial para delimitar período da consulta.
                    @param data_fim_agendamento_titulo: Data de agendamento final para delimitar período da consulta.
                    @param horario_inicio_agendamento_titulo: Hora de agendamento inicial para delimitar período da consulta.
                    @param horario_fim_agendamento_titulo: Hora de agendamento final para delimitar período da consulta.
                    @param id_proximo_titulo: Identificador do próximo título da próxima paginação a ser consultado. Somente deve ser utilizado em caso de pesquisas que retornem mais de 650 boletos.
        Se na resposta da primeira consulta, ou consulta anterior, o campo "possuiMaisTitulos" retorne o valor "S", então na próxima chamada, o usuário deve informar o valor do campo "proximoTitulo" que veio na resposta, a partir do qual será iniciada nova consulta.
                    @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
                    @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
        """
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta is not None:
            query["conta"] = conta
        if carteira is not None:
            query["carteira"] = carteira
        if variacao is not None:
            query["variacao"] = variacao
        if estado_baixa_operacional is not None:
            query["estadoBaixaOperacional"] = estado_baixa_operacional
        if modalidade_titulo is not None:
            query["modalidadeTitulo"] = modalidade_titulo
        if data_inicio_vencimento_titulo is not None:
            query["dataInicioVencimentoTitulo"] = data_inicio_vencimento_titulo
        if data_fim_vencimento_titulo is not None:
            query["dataFimVencimentoTitulo"] = data_fim_vencimento_titulo
        if data_inicio_registro_titulo is not None:
            query["dataInicioRegistroTitulo"] = data_inicio_registro_titulo
        if data_fim_registro_titulo is not None:
            query["dataFimRegistroTitulo"] = data_fim_registro_titulo
        if data_inicio_agendamento_titulo is not None:
            query["dataInicioAgendamentoTitulo"] = data_inicio_agendamento_titulo
        if data_fim_agendamento_titulo is not None:
            query["dataFimAgendamentoTitulo"] = data_fim_agendamento_titulo
        if horario_inicio_agendamento_titulo is not None:
            query["horarioInicioAgendamentoTitulo"] = horario_inicio_agendamento_titulo
        if horario_fim_agendamento_titulo is not None:
            query["horarioFimAgendamentoTitulo"] = horario_fim_agendamento_titulo
        if id_proximo_titulo is not None:
            query["idProximoTitulo"] = id_proximo_titulo
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/boletos-baixa-operacional".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_convenios_by_id_ativar_consulta_baixa_operacional(
        self, *, id: str = None, gw_dev_app_key: str = None, authorization: str = None
    ):
        """
        Habilita a personalização de convênio, permitindo realizar consulta das informações de baixa operacional de boletos da carteira de cobranças do cliente no mesmo dia.

        Args:
            @param id: Número do convênio de Cobrança do Cliente
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/convenios/{id}/ativar-consulta-baixa-operacional".format(
            **path_params
        )
        response = requests.patch(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_convenios_by_id_desativar_consulta_baixa_operacional(
        self, *, id: str = None, gw_dev_app_key: str = None, authorization: str = None
    ):
        """
        Desativa a personalização de convênio, não permitindo realizar consulta das informações de baixa operacional de boletos da carteira de cobranças do cliente no mesmo dia.

        Args:
            @param id: Número do convênio de Cobrança do Cliente
            @param gw_dev_app_key: Chave da aplicação. É a developer_application_key que pode ser encontrada acessando o item Credenciais dentro da sua aplicação no Portal Developers BB.
            @param authorization: É um "token" de acesso fornecido pelo OAuth 2.0.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/convenios/{id}/desativar-consulta-baixa-operacional".format(
            **path_params
        )
        response = requests.patch(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
