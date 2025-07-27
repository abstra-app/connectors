"""
API Boletos - Emissão e Instrução v2.75.111
API responsável pela Emissão, Instrução e Consulta de boletos a partir de critérios específicos.
"""

import requests
from typing import Optional


class BoletosEmissaoClient:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def post_boletos(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
        Emissão ou simulação de boletos registrados na CIP

        Args:
            @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
            @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {}
        path_rendered = "/boletos".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_boletos(
        self,
        *,
        id_beneficiario: str = None,
        codigo_carteira: Optional[str] = None,
        nosso_numero: Optional[str] = None,
        data_inclusao: Optional[str] = None,
        view: Optional[str] = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
              Consulta lista de boletos por critérios específicos.

              Args:
                  @param id_beneficiario: (4 dígitos agência)+(7 dígitos c/c)+(1 dígito DAC)
                  @param codigo_carteira: Código da carteira do título
                  @param nosso_numero: Número de identificação do título
                  @param data_inclusao: Data de inclusão do boleto
                  @param view: Definição a visão que irá permitir o mecanismo de agrupar dados de saída de um determinado recurso.
        -- basic: retorna somente os atributos básicos do recurso
        -- full: retorna todos os atributos do recurso

                  @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                  @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "id_beneficiario": id_beneficiario,
            "codigo_carteira": codigo_carteira,
            "nosso_numero": nosso_numero,
            "data_inclusao": data_inclusao,
            "view": view,
        }
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {}
        path_rendered = "/boletos".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_abatimento(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                API responsável por efetuar a inclusão/alteração de abatimento para um boleto.
        O processo de abatimento consiste na diminuição concedida do valor do boleto no momento de recebimento para o cliente.
        Geralmente, o abatimento é usado quando certas condições estipuladas são encontradas pelo comprador, o que reduz o custo.
        A quantidade descontada é uma abonação determinada pela quantidade ou valor da compra.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/abatimento".format(**path_params)
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_baixa(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a baixa de um boleto.
        O processo de baixa consiste na ação de invalidar o boleto.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/baixa".format(**path_params)
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_data_vencimento(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                API responsável por efetuar a alteração da data de vencimento de um boleto.
        A data de vencimento consiste no último dia para pagamento do boleto sem acréscimo de multa, juros e outros.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/data_vencimento".format(**path_params)
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_juros(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a inclusão/alteração de juros de um boleto.
        Juros é uma cobrança que leva em consideração o tempo de atraso no recebimento do boleto com relação a data de vencimento.
        Os juros agem como uma penalidade para cada dia de inadimplência.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/juros".format(**path_params)
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_multa(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a inclusão/alteração de multa de um boleto.
        Multa é uma cobrança referente ao recebimento do boleto em atraso em relação a data de vencimento.
        A multa é cobrada independente do tenpo de atraso que o boleto se encontra.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/multa".format(**path_params)
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_valor_nominal(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                API responsável por efetuar a alteração do valor nominal do boleto.
        O valor nominal do boleto consiste no valor integral do boleto, informado pelo cliente, sem adição de outros encargos.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/valor_nominal".format(**path_params)
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_data_limite_pagamento(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                API responsável por efetuar a alteração da data limite de pagamento de um boleto.
        A data limite de pagamento para pagamento do boleto. Boleto não poderá ser pago após esta data.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/data_limite_pagamento".format(
            **path_params
        )
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_seu_numero(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                API responsável por efetuar a inclusão/alteração do seu numero do boleto.
        Seu número é a identificação do boleto que poderá ter letras e números, utilizado para
        facilitar a consulta e acompanhamento do status do boleto. Este campo é para controle do cliente.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/seu_numero".format(**path_params)
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_protesto(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a inclusão/alteração de protesto do boleto.
        O protesto é a ação através da qual o portador de um título comercial cujo pagamento não foi efetuado dentro do prazo,
        garante seu pagamento por ações judiciais.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/protesto".format(**path_params)
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_negativacao(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a inclusão/alteração de negativação do boleto.
        A negativação é o ato de inserir uma pessoa em cadastros de maus pagadores,
        tais como Serasa e o Serviço Central de Proteção ao Crédito (SCPC), porque não pagou uma conta,
        uma prestação ou outra obrigação financeira.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/negativacao".format(**path_params)
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_desconto(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a inclusão/alteração de desconto do boleto,
        possibilitando oferecer descontos para pagamentos antecipados do boleto.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/desconto".format(**path_params)
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_pagador(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a alteração de dados do Pagador do boleto.
        O Pagador é a pessoa ou a empresa que deve pagar o valor cobrado em um boleto bancário,
        normalmente por ter feito uma compra, um financiamento ou por estar pagando por um serviço.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/pagador".format(**path_params)
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_sacador_avalista(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a alteração de dados do Sacador Avalista
        O Sacador Avalista é o cedente original do título que realizou a transação.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/sacador_avalista".format(**path_params)
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_boletos_by_id_boleto_recebimento_divergente(
        self,
        *,
        id_boleto: str = None,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
                API responsável por efetuar a alteração de dados de Recebimento Divergente do boleto, ou seja,
        os parâmetros de configuração de aceite de recebimento divergente do valor do boleto.
        Estes dados são configuráveis pelo beneficiário.

                Args:
                    @param id_boleto: Dados para identificação do boleto para alteração.
        Código Agência - Obrigatório (4 caracteres)
        Código Conta Corrente - Obrigatório (7 caracteres)
        Dígito verificador (DAC) - Obrigatório (1 caracter)
        Código Carteira - Obrigatório (3 caracteres)
        Nosso Número - Obrigatório (8-16 caracteres)

                    @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {
            "id_boleto": id_boleto,
        }
        path_rendered = "/boletos/{id_boleto}/recebimento_divergente".format(
            **path_params
        )
        response = requests.patch(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
