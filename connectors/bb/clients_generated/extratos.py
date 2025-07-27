"""
Extratos API v1.0
API para gerenciar os serviços de extrato de clientes do Banco do Brasil S.A.
"""

import requests
from typing import Optional


class ExtratosClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def get_conta_corrente_agencia_by_agencia_conta_by_conta(
        self,
        *,
        gw_dev_app_key: str = None,
        numero_pagina_solicitacao: Optional[int] = None,
        quantidade_registro_pagina_solicitacao: Optional[int] = None,
        data_inicio_solicitacao: Optional[int] = None,
        data_fim_solicitacao: Optional[int] = None,
        agencia: str = None,
        conta: str = None,
    ):
        """
        Dado um código de agência e um número de conta corrente, retorna a listagem de transações efetivadas e de lançamentos futuros, no padrão definido para API BB.

        Args:
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param numero_pagina_solicitacao: Número da página solicitada. Opcionalmente, quando não informado, será atribuído página 1.
            @param quantidade_registro_pagina_solicitacao: Quantidade de registros da página solicitada (pagesize). Opcionalmente, quando não informado, será atribuído pagesize 200. Pagesize máximo: 200 registros. Pagesize mínimo: 50 registros. O pagesize informado na solicitação da primeira página deverá ser mantido nos pedidos das páginas subsequentes do extrato.
            @param data_inicio_solicitacao: Data inicial do período do extrato solicitado. Formato DDMMAAAA. Limite máximo para data inicial: 5 anos a partir da data atual. Para casos onde os campos data inicial e data final não estejam preenchidos, será retornado o extrato dos últimos 30 dias. Caso o campo data inicial seja preenchido, o preenchimento do campo data final será obrigatório.
            @param data_fim_solicitacao: Data final do período do extrato solicitado. Formato DDMMAAAA. Período máximo entre a data inicial e a data final: 31 dias. Para casos onde os campos data final e data inicial não estejam preenchidos, será retornado o extrato dos últimos 30 dias. Caso o campo data final seja preenchido, o preenchimento do campo data inicial será obrigatório.
            @param agencia: Número da agência, sem dígito verificador
            @param conta: Número da conta, sem dígito verificador
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_pagina_solicitacao is not None:
            query["numeroPaginaSolicitacao"] = numero_pagina_solicitacao
        if quantidade_registro_pagina_solicitacao is not None:
            query["quantidadeRegistroPaginaSolicitacao"] = (
                quantidade_registro_pagina_solicitacao
            )
        if data_inicio_solicitacao is not None:
            query["dataInicioSolicitacao"] = data_inicio_solicitacao
        if data_fim_solicitacao is not None:
            query["dataFimSolicitacao"] = data_fim_solicitacao
        headers = {}
        path_params = {}
        if agencia is not None:
            path_params["agencia"] = agencia
        if conta is not None:
            path_params["conta"] = conta
        path_rendered = "/conta-corrente/agencia/{agencia}/conta/{conta}".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
