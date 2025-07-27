"""
API Cash Management v1.14.14
Aqui você visualiza as APIs do SISPAG, que possibilita a gestão dos pagamentos da sua empresa de forma segura e ainda mais rápida. A inclusão é exclusiva para Pix e as consultas estão disponíveis todas as formas de pagamento.
"""

import requests
from typing import Optional


class SispagClient:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def post_transferencias(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_flow_id: Optional[str] = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
        API responsável por inserir transferências de Pix e pagamentos de Pix QR Code na plataforma SISPAG do Banco Itaú.

        Args:
            @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
            @param x_itau_flow_id: Identificador da funcionalidade de negócio sendo executada na aplicação
            @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-flowID": x_itau_flow_id,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {}
        path_rendered = "/transferencias".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos_sispag(
        self,
        *,
        agencia_operacao: str = None,
        conta_operacao: str = None,
        cnpj_empresa: str = None,
        numero_lote: Optional[str] = None,
        valor_minimo: Optional[float] = None,
        valor_maximo: Optional[float] = None,
        referencia_empresa: Optional[str] = None,
        nome_beneficiario: Optional[str] = None,
        data_inicial: Optional[str] = None,
        data_final: Optional[str] = None,
        tipo_lista: str = None,
        modalidade_fornecedores: Optional[bool] = None,
        modalidade_impostos: Optional[bool] = None,
        modalidade_salario: Optional[bool] = None,
        status: Optional[str] = None,
        tipo_pagamento: Optional[str] = None,
        order_by: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[float] = None,
        page_size: Optional[float] = None,
        x_itau_apikey: str = None,
        x_itau_flow_id: Optional[str] = None,
        x_itau_correlation_id: Optional[str] = None,
    ):
        """
              Detalhe da consulta de pagamentos e transferências

              Args:
                  @param agencia_operacao: Agência da operação
                  @param conta_operacao: Conta bancária da operação
                  @param cnpj_empresa: Documento do Pagador
                  @param numero_lote: Número de lote SISPAG
                  @param valor_minimo: Valor mínimo do pagamento
                  @param valor_maximo: Valor máximo do pagamento
                  @param referencia_empresa: Referência da empresa
                  @param nome_beneficiario: Nome do Beneficiário
                  @param data_inicial: Data de pagamento/transferência inicial para consulta
                  @param data_final: Data de pagamento/transferência final para consulta
                  @param tipo_lista: Tipo da lista
                  @param modalidade_fornecedores: Filtro do tipo de modalidade de pagamento para fornecedores
                  @param modalidade_impostos: Filtro do tipo de modalidade de pagamento para impostos e tributos
                  @param modalidade_salario: Filtro do tipo de modalidade de pagamento para salário
                  @param status: Filtro do código do tipo do status<br/>
        * `AE` - A Efetuar
        * `EF` - Efetuados
        * `TD` - Todos
        * `NE` - Não Efetuados
                  @param tipo_pagamento: Filtro do tipo de transação bancária<br/>
        * `01` - Conta Corrente
        * `02` - Cheque pagamento
        * `03` - DOC
        * `04` - OP (duas vias)
        * `05` - Conta Poupança
        * `06` - Conta Corrente Mesma Titularidade
        * `07` - DOC D mesma titularidade
        * `10` - OP (uma via)
        * `11` - OP (acerto)
        * `13` - Concessionária
        * `16` - DARF normal
        * `17` - GPS
        * `18` - DARF simples
        * `19` - IPTU/ISS e outros tributos
        * `22` - GARE ICMS-SP
        * `23` - GARE ICMS-SP Importação
        * `25` - Banco Múltiplo
        * `27` - DPVAT
        * `30` - Boleto Itaú
        * `31` - Boleto outros bancos
        * `32` - Nota fiscal eletrônica
        * `35` - FGTS
        * `38` - Boleto outros bancos online
        * `41` - TED outro titular
        * `43` - TED mesmo titular
        * `51` - Licenciamento
        * `53` - Multa
        * `63` - Concessionária com moeda variável
        * `91` - Tributos com código de barras
        * `92` - DARF código de barras
        * `93` - DAS código barras
        * `94` - GNRE ICMS-SP Importação
        * `95` - IPVA
        * `45` - PIX Transferências
        * `47` - PIX Qr Code
        * `60` - Cartão Salário
                  @param order_by: Opção para ordenação.
                  @param order: Opção de ordenação ascendente ou descendente.
                  @param page: Numero da página da consulta que deseja receber.
                  @param page_size: Quantidade de pagamentos por página.
                  @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
                  @param x_itau_flow_id: Identificador da funcionalidade de negócio sendo executada na aplicação
                  @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "agencia_operacao": agencia_operacao,
            "conta_operacao": conta_operacao,
            "cnpj_empresa": cnpj_empresa,
            "numero_lote": numero_lote,
            "valor_minimo": valor_minimo,
            "valor_maximo": valor_maximo,
            "referencia_empresa": referencia_empresa,
            "nome_beneficiario": nome_beneficiario,
            "data_inicial": data_inicial,
            "data_final": data_final,
            "tipo_lista": tipo_lista,
            "modalidade_fornecedores": modalidade_fornecedores,
            "modalidade_impostos": modalidade_impostos,
            "modalidade_salario": modalidade_salario,
            "status": status,
            "tipo_pagamento": tipo_pagamento,
            "order_by": order_by,
            "order": order,
            "page": page,
            "page_size": page_size,
        }
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-flowID": x_itau_flow_id,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {}
        path_rendered = "/pagamentos_sispag".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos_sispag_by_id_pagamento_sispag(
        self, *, id_pagamento_sispag: str = None, x_itau_apikey: str = None
    ):
        """
        Operação responsável por recuperar o detalhamento do pagamento

        Args:
            @param id_pagamento_sispag: Identificador único do Pagamento
            @param x_itau_apikey: Chave da API utilizado para autorizar o consumo de uma aplicação requisitante
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "id_pagamento_sispag": id_pagamento_sispag,
        }
        path_rendered = "/pagamentos_sispag/{id_pagamento_sispag}".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
