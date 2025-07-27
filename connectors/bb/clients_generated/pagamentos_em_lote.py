"""
Pagamentos em Lote v1.42.15
API para realizar consultas, requisições, liberações, cancelamentos, etc., de pagamento/transferências em lote.
"""

import requests
from typing import Optional


class PagamentosEmLoteClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_liberar_pagamentos(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
                Permite que a empresa efetue a liberação dos lotes de pagamentos diretamente de seu sistema de gestão - ERP.

        Após o comando de liberação, o processamento do pagamento de todos os lançamentos do lote liberado dependerá da existência de saldo em conta até o horário limite para efetivação de cada um deles, da validação dos dados e demais regras pactuadas na contratação do serviço.

        A situação de cada lançamento deverá se consultada posteriormente.

        O mesmo lote poderá ser liberado mais de uma vez. Por exemplo: Foi enviado lançamentos com data de pagamento do dia anterior e do dia corrente. Após foi comandada a liberação do lote. Nesse caso, apenas os lançamentos com data do dia corrente seriam efetivados. Mas a empresa poderá alterar a data de pagamento dos lançamentos com data incorreta e após solicitar novamente a liberação do lote.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/liberar-pagamentos".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_transferencias(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        numero_contrato_pagamento: Optional[int] = None,
        agencia_debito: Optional[int] = None,
        conta_corrente_debito: Optional[int] = None,
        digito_verificador_conta_corrente: str = None,
        data_inicio: Optional[int] = None,
        data_fim: Optional[int] = None,
        tipo_pagamento: Optional[int] = None,
        estado_requisicao: Optional[int] = None,
        indice: Optional[int] = None,
    ):
        """
                Realiza consulta a um Lote de Pagamentos realizados via Tranferência Bancária

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param numero_contrato_pagamento: Contrato de pagamento entre o terceiro e o Banco do Brasil. Opcionalmente, quando não informado, será considerado o contrato vinculado à identificação interna do cliente.
        Quando utilizado Login Máquina Máquina: É opcional.
        Quando utilizado Login Explícito: É obrigatório. É extraído do token.
                    @param agencia_debito: Código da agência para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.
        Quando utilizado Login Máquina Máquina: É opcional.
        Quando utilizado Login Explícito: É obrigatório. É extraído do token.
                    @param conta_corrente_debito: Conta corrente de débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.
        Quando utilizado Login Máquina Máquina: É opcional.
        Quando utilizado Login Explícito: É obrigatório. É extraído do token.
                    @param digito_verificador_conta_corrente: Dígito do verificador da conta corrente para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.
        Quando utilizado Login Máquina Máquina: É opcional.
        Quando utilizado Login Explícito: É obrigatório. É extraído do token.
                    @param data_inicio: Data inicial de envio da requisição a ser pesquisada.
                    @param data_fim: Data final de envio da requisição a ser pesquisada.
                    @param tipo_pagamento: A modalidade que representa o tipo de pagamento, descrita a seguir:
        126 significa pagamento de fornecedores;
        127 significa pagamento de salário;
        128 significa pagamento diverso.
                    @param estado_requisicao: Código que identifica o estado da solicitação.

         1 - Requisição com todos os lançamentos com dados consistentes;

         2 - Requisição com ao menos um dos lançamentos com dados inconsistentes;

         3 - Requisição com todos os lançamentos com dados inconsistentes;

         4 - Requisição pendente de ação pelo Conveniado - falta autorizar o pagamento;

         5 - Requisição em processamento pelo Banco;

         6 - Requisição Processada;

         7 - Requisição Rejeitada,

         8 - Preparando remessa não liberada,

         9 - Requisição liberada via API,

         10 -  Preparando remessa liberada.

         As situações 1, 2 e 8 são transitórias e não requerem qualquer ação do Cliente Conveniado.

         situação 3 sempre será migrada para situação 7.

         A situação 4 Significa que, ao menos um lançamento, depende de ação do Cliente Conveniado, seja liberando ou cancelando os pagamentos.

         As situações 5, 6, 7, 9 e 10 não requerem qualquer ação do Cliente Conveniado.

         A situação 5 significa que, ao menos um lançamento, está agendado.

         As situações 6 e 7 são definitivas não havendo alteração posterior da situação da requisição.
                    @param indice: Posição do índice. Cada resposta tem um limite de 300 ocorrências na lista paymentList, iniciada a partir do valor do índice fornecido. Para todas as ocorrências, itere sobre esse recurso usando o valor do campo nextIndex da resposta.

        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_contrato_pagamento is not None:
            query["numeroContratoPagamento"] = numero_contrato_pagamento
        if agencia_debito is not None:
            query["agenciaDebito"] = agencia_debito
        if conta_corrente_debito is not None:
            query["contaCorrenteDebito"] = conta_corrente_debito
        if digito_verificador_conta_corrente is not None:
            query["digitoVerificadorContaCorrente"] = digito_verificador_conta_corrente
        if data_inicio is not None:
            query["dataInicio"] = data_inicio
        if data_fim is not None:
            query["dataFim"] = data_fim
        if tipo_pagamento is not None:
            query["tipoPagamento"] = tipo_pagamento
        if estado_requisicao is not None:
            query["estadoRequisicao"] = estado_requisicao
        if indice is not None:
            query["indice"] = indice
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/lotes-transferencias".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_lotes_transferencias(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
                Efetua o envio de um Lote de Pagamentos a serem realizados via Tranferência Bancária

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/lotes-transferencias".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_lotes_transferencias_pix(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
                Efetua pagamentos em lote via tranferência PIX.

        Atualmente, a requisição pode ser enviada a qualquer horário, mas a liberação é permitida a partir das 7h30.

        Quando não se tratar de liberação automática, a liberação manual poderá ser feita por meio do recurso "/liberar-pagamentos".

        Não haverá recurso para confirmação de titularidade da chave PIX.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/lotes-transferencias-pix".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_cancelar_pagamentos(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
                Efetua o Cancelamento de um Lote de Pagamentos

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/cancelar-pagamentos".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_darf_preto_by_id(
        self,
        *,
        agencia: Optional[float] = None,
        conta_corrente: Optional[float] = None,
        digito_verificador: Optional[str] = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        id: str = None,
    ):
        """
                A partir de um código identificador de pagamento de um DARF Preto, retorna os detalhes do pagamento desta, como estado do pagamento, data do pagamento, forma do pagamento, valor, descrição, código de devolução, entre outros.

                Args:
                    @param agencia: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.

                    @param conta_corrente: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param digito_verificador: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param id: Identificação da solicitação de pagamento. É um número único, não sequencial, controlado pelo cliente, cujo valor vai de 1 a 999999.
        """
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/darf-preto/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_guias_codigo_barras_by_id(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        agencia: Optional[float] = None,
        conta_corrente: Optional[float] = None,
        digito_verificador: Optional[str] = None,
        id: str = None,
    ):
        """
                A partir de um código identificador de pagamento de uma Guia com Código de Barras, retorna os detalhes do pagamento desta, como estado do pagamento, data do pagamento, forma do pagamento, valor, descrição, código de devolução, entre outros.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param agencia: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param conta_corrente: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param digito_verificador: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param id: Identificação da solicitação de pagamento. É um número único, não sequencial, controlado pelo cliente, cujo valor vai de 1 a 999999.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/guias-codigo-barras/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_guias_codigo_barras_by_id_solicitacao(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        agencia: Optional[float] = None,
        conta_corrente: Optional[float] = None,
        digito_verificador: Optional[str] = None,
        id: str = None,
    ):
        """
                Permite consultar a resposta de uma solicitação de pagamento em lote de guias de recolhimento com código de barras. Utilizada quando a empresa não recebeu a confirmação da solicitação de pagamento de guia com barras ou precisar recuperar a resposta original ou quer confirmar se o número da solicitação de pagamento já foi utilizada.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param agencia: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param conta_corrente: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param digito_verificador: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param id: Numero que identifica a solicitação de pagamento. É um número único, não sequencial, cujo valor vai de 1 a 999999999.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotes-guias-codigo-barras/{id}/solicitacao".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_gru_by_id(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        agencia: Optional[float] = None,
        digito_verificador: Optional[str] = None,
        conta_corrente: Optional[float] = None,
        id: str = None,
    ):
        """
                A partir de um código identificador de pagamento de uma Guia de Recolhimento da União, retorna os detalhes do pagamento desta, como estado do pagamento, data do pagamento, forma do pagamento, valor, descrição, código de devolução, entre outros.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param agencia: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.

                    @param digito_verificador: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param conta_corrente: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param id: Identificação da solicitação de pagamento. É um número único, não sequencial, controlado pelo cliente, cujo valor vai de 1 a 999999.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if agencia is not None:
            query["agencia"] = agencia
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/gru/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_gps_by_id(
        self,
        *,
        agencia: Optional[int] = None,
        conta_corrente: Optional[int] = None,
        digito_verificador: Optional[str] = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        id: str = None,
    ):
        """
                A partir de um código identificador de pagamento de uma Guia da Previdência Social, retorna os detalhes do pagamento desta, como estado do pagamento, data do pagamento, forma do pagamento, valor, descrição, código de devolução, entre outros.

                Args:
                    @param agencia: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param conta_corrente: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param digito_verificador: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.

                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param id: Identificação da solicitação de pagamento. É um número único, não sequencial, controlado pelo cliente, cujo valor vai de 1 a 999999.
        """
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/gps/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_pagamentos_gru(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
                Gera uma requisição de pagamento de guias com código de barras, do tipo GRU.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/pagamentos-gru".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        agencia_debito: Optional[int] = None,
        conta_corrente_debito: Optional[int] = None,
        digito_verificador_conta_corrente: Optional[str] = None,
        numero_contrato_pagamento: Optional[int] = None,
        data_inicio: int = None,
        data_fim: int = None,
        estado_pagamento: Optional[str] = None,
        indice: int = None,
    ):
        """
                Consulta os pagamentos e transferências devolvidos.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param agencia_debito: Número da agência da conta corrente de débito. Obrigatoriedade conforme fluxo OAuth: 1) Client Credentials: campo opcional; 2) Authorization Code: informação extraída do token.
                    @param conta_corrente_debito: Número da conta corrente de débito. Obrigatoriedade conforme fluxo OAuth: 1) Client Credentials: campo opcional; 2) Authorization Code: informação extraída do token.
                    @param digito_verificador_conta_corrente: Dígito verificador da conta corrente de débito. Obrigatoriedade conforme fluxo OAuth: 1) Client Credentials: campo opcional; 2) Authorization Code: informação extraída do token.
                    @param numero_contrato_pagamento: Contrato de pagamento entre o terceiro e o Banco do Brasil. Obrigatoriedade conforme fluxo OAuth: 1) Client Credentials: campo opcional; 2) Authorization Code: informação extraída do token.
                    @param data_inicio: Data inicial de envio da requisição a ser pesquisada.
                    @param data_fim: Data final de envio da requisição a ser pesquisada. Não pode ser um intervalo maior que 30 dias.
                    @param estado_pagamento: Estados dos pagamentos. Domínio: 1) Agendado: Pagamento aguardando a data para efetivação do crédito; 2) Cancelado: Pagamento cancelado pelo Cliente Conveniado antes da data do crédito;  3) Consistente: Dados recebidos pelo Banco sem ocorrências quanto ao formato. Aguardando validação dos dados para liberação/efetivação dos pagamentos;  4) Devolvido: Pagamento efetuado e posteriormente recusado pelo recebedor. O valor é devolvida para a Conta corrente onde ocorreu o débito da requisição; 5) Inconsistente: Dados recebidos pelo Banco com ocorrências quanto ao formato. A situação será alterada para rejeitado; 6) Pago: Pagamento efetuado;  7) Pendente: Falta autorização para o débito do pagamento na conta do cliente conveniado;  8) Rejeitado: Dados do pagamento não passaram na validações físicas e/ou lógicas. Ex: agência e conta não existem, conta não pertence ao CPF informado; 9) Vencido: Pagamento não efetuado na data indicada por falta de saldo ou falta de autorização para débito do pagamento na conta do cliente conveniado.
                    @param indice: Posição do índice na pesquisa, utilizado para fazer a paginação. A primeira consulta deve ter o valor zerado. Cada resposta tem um limite de 100 registros, e inicia-se a partir do valor do índice fornecido. Para consultar todos os registros, itere sobre este recurso usando o valor do campo "indice" que vem na da resposta.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if agencia_debito is not None:
            query["agenciaDebito"] = agencia_debito
        if conta_corrente_debito is not None:
            query["contaCorrenteDebito"] = conta_corrente_debito
        if digito_verificador_conta_corrente is not None:
            query["digitoVerificadorContaCorrente"] = digito_verificador_conta_corrente
        if numero_contrato_pagamento is not None:
            query["numeroContratoPagamento"] = numero_contrato_pagamento
        if data_inicio is not None:
            query["dataInicio"] = data_inicio
        if data_fim is not None:
            query["dataFim"] = data_fim
        if estado_pagamento is not None:
            query["estadoPagamento"] = estado_pagamento
        if indice is not None:
            query["indice"] = indice
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

    def get_transferencias_by_id(
        self,
        *,
        agencia: Optional[int] = None,
        conta_corrente: Optional[int] = None,
        digito_verificador: Optional[str] = None,
        authorization: str = None,
        gw_dev_app_key: str = None,
        id: str = None,
    ):
        """
                Consulta sobre um Pagamento específico em um Lote de Transferências

                Args:
                    @param agencia: Código da agência para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param conta_corrente: Conta corrente de débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param digito_verificador: Dígito do verificador da conta corrente para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param id: Número único gerado pelo Banco. Deve ser utilizado pelo Cliente Conveniado para efetivar consultas posteriores ao lançamento.
        """
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/transferencias/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_by_id(
        self, *, authorization: str = None, gw_dev_app_key: str = None, id: str = None
    ):
        """
                Consulta um lote de pagamentos.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param id: No description provided.
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
        path_rendered = "/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_by_id_solicitacao(
        self, *, authorization: str = None, gw_dev_app_key: str = None, id: str = None
    ):
        """
                Consulta sobre uma solicitação de requisição para efetuar um lote de pagamentos via transferência e os pagamentos deste lote.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param id: Identificação da solicitação de pagamento. É um número único, não sequencial, controlado pelo cliente, cujo valor vai de 1 a 999999.
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
        path_rendered = "/{id}/solicitacao".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_gru_by_id_solicitacao(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        numero_agencia_debito: Optional[int] = None,
        numero_conta_corrente_debito: Optional[int] = None,
        digito_verificador_conta_corrente_debito: Optional[str] = None,
        id: str = None,
    ):
        """
                Consulta a resposta de uma solicitação de pagamentos de GRU em lote.

        Recurso utilizado quando do não recebimento da confirmação da Solicitação de Pagamento de Guia GRU em Lote, ou quando houver a necessidade de recuperar a resposta original de uma solicitação, ou quando for necessário confirmar se determinado número da solicitação de pagamento já fora utilizada.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer $
                    @param numero_agencia_debito: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.

                    @param numero_conta_corrente_debito: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.
                    @param digito_verificador_conta_corrente_debito: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.
                    @param id: Identificação da solicitação de pagamento. É um número único, não sequencial, controlado pelo cliente, cujo valor vai de 1 a 999999.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_agencia_debito is not None:
            query["numeroAgenciaDebito"] = numero_agencia_debito
        if numero_conta_corrente_debito is not None:
            query["numeroContaCorrenteDebito"] = numero_conta_corrente_debito
        if digito_verificador_conta_corrente_debito is not None:
            query["digitoVerificadorContaCorrenteDebito"] = (
                digito_verificador_conta_corrente_debito
            )
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotes-gru/{id}/solicitacao".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_gps_by_id_solicitacao(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        numero_agencia_debito: Optional[int] = None,
        numero_conta_corrente_debito: Optional[int] = None,
        digito_verificador_conta_corrente_debito: Optional[str] = None,
        id: str = None,
    ):
        """
                Consulta a resposta de uma solicitação de pagamentos de GPS em lote.

        Recurso utilizado quando do não recebimento da confirmação da Solicitação de Pagamento de Guia de Previdência Social - GPS em Lote, ou quando houver a necessidade de recuperar a resposta original de uma solicitação, ou quando for necessário confirmar se determinado número da solicitação de pagamento já fora utilizado.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer $
                    @param numero_agencia_debito: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.

                    @param numero_conta_corrente_debito: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.
                    @param digito_verificador_conta_corrente_debito: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.
                    @param id: Identificação da solicitação de pagamento. É um número único, não sequencial, controlado pelo cliente, cujo valor vai de 1 a 999999.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_agencia_debito is not None:
            query["numeroAgenciaDebito"] = numero_agencia_debito
        if numero_conta_corrente_debito is not None:
            query["numeroContaCorrenteDebito"] = numero_conta_corrente_debito
        if digito_verificador_conta_corrente_debito is not None:
            query["digitoVerificadorContaCorrenteDebito"] = (
                digito_verificador_conta_corrente_debito
            )
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotes-gps/{id}/solicitacao".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_darf_preto_normal_by_id_solicitacao(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        numero_agencia_debito: Optional[int] = None,
        numero_conta_corrente_debito: Optional[int] = None,
        digito_verificador_conta_corrente_debito: Optional[str] = None,
        id: str = None,
    ):
        """
                Consulta a resposta de uma solicitação de pagamentos de DARF Preto Normal em Lote.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer $
                    @param numero_agencia_debito: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.

                    @param numero_conta_corrente_debito: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.
                    @param digito_verificador_conta_corrente_debito: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é opcionalmente informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do Token.
                    @param id: Identificação da solicitação de pagamento. É um número único, não sequencial, controlado pelo cliente, cujo valor vai de 1 a 999999.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if numero_agencia_debito is not None:
            query["numeroAgenciaDebito"] = numero_agencia_debito
        if numero_conta_corrente_debito is not None:
            query["numeroContaCorrenteDebito"] = numero_conta_corrente_debito
        if digito_verificador_conta_corrente_debito is not None:
            query["digitoVerificadorContaCorrenteDebito"] = (
                digito_verificador_conta_corrente_debito
            )
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotes-darf-preto-normal/{id}/solicitacao".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_lotes_darf_normal_preto(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
                Permite efetuar solicitação de pagamentos em lote de Darf Normal e Darf Preto.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/lotes-darf-normal-preto".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_lotes_gps(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
                Permite efetuar solicitação de pagamentos em lote de Guia da Previdência Social - GPS.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/lotes-gps".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_pagamentos_codigo_barras_by_id(
        self,
        *,
        agencia_debito: Optional[int] = None,
        conta_corrente_debito: Optional[int] = None,
        digito_verificador_conta_corrente: Optional[str] = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        id: str = None,
    ):
        """
                Consulta todos os Pagamentos Efetuados e Vinculados a um Código de Barras Específico em um Lote de Pagamentos

                Args:
                    @param agencia_debito: Código da agência para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.
                    @param conta_corrente_debito: Conta corrente de débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.
                    @param digito_verificador_conta_corrente: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param id: Codigo de barras do Pagamento
        """
        query = {}
        if agencia_debito is not None:
            query["agenciaDebito"] = agencia_debito
        if conta_corrente_debito is not None:
            query["contaCorrenteDebito"] = conta_corrente_debito
        if digito_verificador_conta_corrente is not None:
            query["digitoVerificadorContaCorrente"] = digito_verificador_conta_corrente
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/pagamentos-codigo-barras/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_beneficiarios_by_id_transferencias(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        agencia_debito: Optional[int] = None,
        conta_corrente_debito: Optional[int] = None,
        digito_verificador_conta_corrente: Optional[str] = None,
        tipo_pagamento: Optional[int] = None,
        numero_compe: Optional[int] = None,
        numero_ispb: Optional[int] = None,
        agencia_credito: Optional[int] = None,
        conta_corrente_credito: Optional[int] = None,
        digito_verificador_conta_corrente_credito: Optional[str] = None,
        conta_pagamento_credito: Optional[str] = None,
        data_inicio: int = None,
        data_fim: int = None,
        indice: int = None,
        tipo_beneficiario: int = None,
        id: str = None,
    ):
        """
                Consultar Tranferências Bancárias realizadas por Beneficiário

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param agencia_debito: Número da agência da Conta Corrente onde foi efetuado o débito para efetivação do pagamento consultado.
                    @param conta_corrente_debito: Número da Conta Corrente onde foi efetuado o débito para efetivação do pagamento consultado.
                    @param digito_verificador_conta_corrente: Digito verificador da Conta corrente onde foi efetuado o débito para efetivação do pagamento consultado.
                    @param tipo_pagamento: Modalidade que representa o tipo de pagamento, sendo: 126 pagamento de fornecedores; 127 pagamento de salário e 128 pagamentos diversos
                    @param numero_compe: Número COMPE (Código do Sistema de Operações Monetárias e Compensações de Outros Papéis) da instituição detentora da conta do favorecido. Uma lista de códigos permitidos é obtida através do site do Banco Central (https://dadosabertos.bcb.gov.br/dataset/lista-de-participantes-do-str).
                    @param numero_ispb: Número ISPB (Identificador de Sistema de Pagamento Brasileiro) da instituição detentora da conta do favorecido. Uma lista de códigos permitidos é obtida através do site do Banco Central (https://dadosabertos.bcb.gov.br/dataset/lista-de-participantes-do-str).Se atentar para o código "0" que é existente na relação do Banco Central.
                    @param agencia_credito: Número da agência da Conta Corrente onde foi efetuado o crédito do pagamento consultado. Quando informado, o campo contaPagamentoCredito, este deve ser branco.
                    @param conta_corrente_credito: Número da Conta Corrente onde foi efetuado o crédito do pagamento consultado. Quando informado, o campo contaPagamentoCredito, este deve ser branco.
                    @param digito_verificador_conta_corrente_credito: Digito verificador da Conta corrente onde foi efetuado o crédito do pagamento consultado. Quando informado, o campo contaPagamentoCredito, este deve ser branco.
                    @param conta_pagamento_credito: Número da Conta Pagamento dos pagamentos a serem pesquisados.
        Quando informado, os campos agenciaCredito, contaCorrenteCredito e digitoVerificadorContaCorrenteCredito, este campo não deve ser informado.

                    @param data_inicio: Data inicial de envio da requisição a ser pesquisada (formato: ddmmaaaa).
                    @param data_fim: Data final de envio da requisição a ser pesquisada (formato: ddmmaaaa).
                    @param indice: Posição do índice de paginação.  Indica a posição a partir da qual a pesquisa tratá os registros (ex: valor 0, indica que está trazendo a partir do registro 1, valor 300 indica que está trazendo a partir do 301). Cada resposta tem um limite de 300 ocorrências na lista paymentList, iniciada a partir do valor do índice fornecido. Para todas as ocorrências, itere sobre esse recurso usando o valor do campo indice da resposta.
                    @param tipo_beneficiario: Tipo do número de inscrição da pessoa favorecida do crédito. Quando 1 é uma Pessoa Física (CPF) e 2 é Pessoa Jurídica (CNPJ).
        1 - CPF
        2 - CNPJ
                    @param id: Numero de inscrição do Beneficiário (CPF) ou (CNPJ) do favorecido do crédito a ser pesquisado.

        Pode ser pesquisado só pelo CPF ou CNPJ sem ser informado os dados da Agência e Conta de Crédito.

        Quando informado CPF, não deverá ser informado um CNPJ como id, e vice-versa.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if agencia_debito is not None:
            query["agenciaDebito"] = agencia_debito
        if conta_corrente_debito is not None:
            query["contaCorrenteDebito"] = conta_corrente_debito
        if digito_verificador_conta_corrente is not None:
            query["digitoVerificadorContaCorrente"] = digito_verificador_conta_corrente
        if tipo_pagamento is not None:
            query["tipoPagamento"] = tipo_pagamento
        if numero_compe is not None:
            query["numeroCOMPE"] = numero_compe
        if numero_ispb is not None:
            query["numeroISPB"] = numero_ispb
        if agencia_credito is not None:
            query["agenciaCredito"] = agencia_credito
        if conta_corrente_credito is not None:
            query["contaCorrenteCredito"] = conta_corrente_credito
        if digito_verificador_conta_corrente_credito is not None:
            query["digitoVerificadorContaCorrenteCredito"] = (
                digito_verificador_conta_corrente_credito
            )
        if conta_pagamento_credito is not None:
            query["contaPagamentoCredito"] = conta_pagamento_credito
        if data_inicio is not None:
            query["dataInicio"] = data_inicio
        if data_fim is not None:
            query["dataFim"] = data_fim
        if indice is not None:
            query["indice"] = indice
        if tipo_beneficiario is not None:
            query["tipoBeneficiario"] = tipo_beneficiario
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/beneficiarios/{id}/transferencias".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_boletos_by_id(
        self,
        *,
        agencia: Optional[float] = None,
        conta_corrente: Optional[float] = None,
        digito_verificador: Optional[str] = None,
        gw_dev_app_key: str = None,
        authorization: str = None,
        id: str = None,
    ):
        """
                Consulta sobre um Pagamento específico em um Lote de Boletos

                Args:
                    @param agencia: Número da agência da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.

                    @param conta_corrente: Número da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param digito_verificador: Dígito verificador da conta corrente de débito do valor total de cada requisição. Quando utilizado o fluxo Client Credentials, esse campo é informado pelo cliente. Quando utilizado o fluxo Authorization Code, essa informação é do token.
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param id: Identificação do pagamento específico. É um número único, retornado pelo Banco, na solicitação de pagamento de boletos
        """
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
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

    def post_lotes_boletos(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
                Permite efetuar solicitação de pagamentos em lote de Boletos.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/lotes-boletos".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_lotes_guias_codigo_barras(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        body: dict = None,
    ):
        """
                Permite efetuar solicitação de pagamento em lote de Guias de Recolhimento com código de barras.

                Args:
                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/lotes-guias-codigo-barras".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_transferencias_pix_by_id_solicitacao(
        self,
        *,
        agencia: Optional[int] = None,
        conta_corrente: Optional[int] = None,
        digito_verificador: Optional[str] = None,
        authorization: str = None,
        gw_dev_app_key: str = None,
        id: str = None,
    ):
        """
                Permite ao cliente recuperar a resposta da Solicitação de Transferência em lote para pagamentos realizados via PIX.

        Utilizada quando a empresa não recebeu a confirmação da Solicitação de Transferência em lote ou quando precisar recuperar a resposta original ou queira confirmar que o número da Solicitação de Pagamento já foi utilizado.

                Args:
                    @param agencia: Código da agência para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param conta_corrente: Conta corrente de débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param digito_verificador: Dígito do verificador da conta corrente para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param id: Numero do lote de transferências enviado via API a ser consultado.
        """
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotes-transferencias-pix/{id}/solicitacao".format(
            **path_params
        )
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pix_by_id(
        self,
        *,
        agencia: Optional[int] = None,
        conta_corrente: Optional[int] = None,
        digito_verificador: Optional[str] = None,
        authorization: str = None,
        gw_dev_app_key: str = None,
        id: str = None,
    ):
        """
                Detalha todos os dados de um pagamento efetuado na modalidade PIX.

                Args:
                    @param agencia: Código da agência para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param conta_corrente: Conta corrente de débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param digito_verificador: Dígito do verificador da conta corrente para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param id: Número único gerado pelo Banco. Utilizado pelo Cliente Conveniado para efetivar as consultas posteriores ao lançamento.
        """
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/pix/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lotes_boletos_by_id_solicitacao(
        self,
        *,
        agencia: Optional[int] = None,
        conta_corrente: Optional[int] = None,
        digito_verificador: Optional[str] = None,
        authorization: str = None,
        gw_dev_app_key: str = None,
        id: str = None,
    ):
        """
                Permite ao cliente recuperar a resposta da Solicitação de Transferência em lote para pagamentos realizados via boletos.

        Utilizada quando a empresa não recebeu a confirmação da Solicitação de Transferência em lote ou quando precisar recuperar a resposta original ou queira confirmar que o número da Solicitação de Pagamento já foi utilizado.

                Args:
                    @param agencia: Código da agência para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param conta_corrente: Conta corrente de débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param digito_verificador: Dígito do verificador da conta corrente para débito. Não é necessário quando a solicitação é acessada pelo código de autorização no fluxo do OAuth.

                    @param authorization: É o valor do token de acesso fornecido pelo OAuth.
        Exemplo: Bearer <acess_token>
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor.
        Essa chave será usada para identificação do aplicativo.
                    @param id: Numero do lote de transferências enviado via API a ser consultado.
        """
        query = {}
        if agencia is not None:
            query["agencia"] = agencia
        if conta_corrente is not None:
            query["contaCorrente"] = conta_corrente
        if digito_verificador is not None:
            query["digitoVerificador"] = digito_verificador
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotes-boletos/{id}/solicitacao".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lancamentos_periodo(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        codigo_cliente_conveniado: Optional[int] = None,
        numero_agencia_debito: int = None,
        numero_conta_corrente_debito: int = None,
        digito_verificador_conta_corrente_debito: str = None,
        data_inicialde_envioda_requisicao: int = None,
        data_finalde_envioda_requisicao: Optional[int] = None,
        codigodo_estadodo_pagamento: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_da_posicao_de_pesquisa: Optional[int] = None,
    ):
        """
        Evento utilizado para requisicao e resposta da transacao negocial da operação "Listar Lançamentos por Período de Pagamento".

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.Exemplo: Bearer <acess_token>
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param codigo_cliente_conveniado: Campo preenchido pela API. Identificação do cliente conveniado.
            @param numero_agencia_debito: Número da agência da conta corrente onde deverá ser efetuado o débito do pagamento.                                 Quando utilizado Login M2M: não é iformado.                                                                                                     Quanto utilizado login explícito: é informado, sendo extraído do
            @param numero_conta_corrente_debito: Número da conta corrente onde deverá ser efetuado o débito do pagamento.                                                         Quando utilizado login M2M: não é informado.                                                                                                    Quando utilizado login explícito: é informado, sendo extraído
            @param digito_verificador_conta_corrente_debito: Digito verificador da conta corrente onde deverá ser efetuado o débito do pagamento.
            @param data_inicialde_envioda_requisicao: Data inicial de envio da requisição (formato "ddmmaaaaa").
            @param data_finalde_envioda_requisicao: Data final de envio da requisição (formato "ddmmaaaaa"). Quando não informado sistema  assume Data Final igual a Data Inicial.
            @param codigodo_estadodo_pagamento: Codigo do estado do pagamento.
            @param codigo_produto: Código atribuído pelo sistema PRD ao produto a ser comercializado pelo BB (ativo/passivo/prestação de serviços) EX.: 0=Todos os tipos de produto; 126=Pagamento a Fornecedores; 127=Pagamento de Salários; 128=Pagamentos Diversos.
            @param numero_da_posicao_de_pesquisa: Numero da posição, do registro, de continuidade da pesquisa (Valor zerado indica uma pesquisa inicial).
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        if codigo_cliente_conveniado is not None:
            query["codigoClienteConveniado"] = codigo_cliente_conveniado
        if numero_agencia_debito is not None:
            query["numeroAgenciaDebito"] = numero_agencia_debito
        if numero_conta_corrente_debito is not None:
            query["numeroContaCorrenteDebito"] = numero_conta_corrente_debito
        if digito_verificador_conta_corrente_debito is not None:
            query["digitoVerificadorContaCorrenteDebito"] = (
                digito_verificador_conta_corrente_debito
            )
        if data_inicialde_envioda_requisicao is not None:
            query["dataInicialdeEnviodaRequisicao"] = data_inicialde_envioda_requisicao
        if data_finalde_envioda_requisicao is not None:
            query["dataFinaldeEnviodaRequisicao"] = data_finalde_envioda_requisicao
        if codigodo_estadodo_pagamento is not None:
            query["codigodoEstadodoPagamento"] = codigodo_estadodo_pagamento
        if codigo_produto is not None:
            query["codigoProduto"] = codigo_produto
        if numero_da_posicao_de_pesquisa is not None:
            query["numeroDaPosicaoDePesquisa"] = numero_da_posicao_de_pesquisa
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/lancamentos-periodo".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_by_id_data_pagamentos(
        self,
        *,
        authorization: str = None,
        gw_dev_app_key: str = None,
        id: str = None,
        body: dict = None,
    ):
        """
        Este recurso permite alterar a data original do pagamento.

        Args:
            @param authorization: É o valor do token de acesso fornecido pelo OAuth.Exemplo: Bearer <acess_token>
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor. Essa chave será usada para identificação do aplicativo.
            @param id: Número da requisição do pagamento. Número único controlado pelo cliente conveniado.
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
        path_rendered = "/{id}/data-pagamentos".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()
