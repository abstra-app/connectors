"""
itau-ep9-gtw-pix-recebimentos-conciliacoes-v2-ext v2.145.22
APis Pix Recebimentos Complementares para Clientes e Participantes Indiretos V2.

"""

import requests
from typing import Optional


class PixRecebimentosConciliacoesV2Client:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def post_decodificacoes_qrcode(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                Operação responsável por recuperar os dados do QR Code escaneado através dos dados EMV.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

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
        path_rendered = "/decodificacoes_qrcode".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_leituras_qrcodes_pix(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        estatisticas: Optional[bool] = None,
        body: dict = None,
    ):
        """
                Operação responsável por recuperar os dados do QR Code escaneado através dos dados EMV.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param estatisticas: **Descrição:** Habilita ou desabilita o retorno dos dados de análise de fraudes.

                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "estatisticas": estatisticas,
        }
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-itau-correlationID": x_itau_correlation_id,
        }
        path_params = {}
        path_rendered = "/leituras_qrcodes_pix".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_cobrancas_imediata_pix(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                Operação responsável por emitir um novo QR Code imediato.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

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
        path_rendered = "/cobrancas_imediata_pix".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_cobrancas_imediata_pix_by_id_cobranca_imediata_pix(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        id_cobranca_imediata_pix: str = None,
        body: dict = None,
    ):
        """
                Operação responsável por alterar um QR Code imediato.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id_cobranca_imediata_pix: **Descrição:** Identificador da cobrança imediata a ser consultado.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

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
            "id_cobranca_imediata_pix": id_cobranca_imediata_pix,
        }
        path_rendered = "/cobrancas_imediata_pix/{id_cobranca_imediata_pix}".format(
            **path_params
        )
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cobrancas_imediata_pix_by_id_cobranca_imediata_pix_qrcode(
        self,
        *,
        x_itau_apikey: str = None,
        id_cobranca_imediata_pix: str = None,
        x_correlation_id: Optional[str] = None,
    ):
        """
                API descontinuada. Para verificar dados de um qrcode, por favor utilizar a API ...

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id_cobranca_imediata_pix: Id a ser consultado.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-correlationID": x_correlation_id,
        }
        path_params = {
            "id_cobranca_imediata_pix": id_cobranca_imediata_pix,
        }
        path_rendered = (
            "/cobrancas_imediata_pix/{id_cobranca_imediata_pix}/qrcode".format(
                **path_params
            )
        )
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_cobrancas_vencimento_pix(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                Operação responsável por emitir um novo QR Code com vencimento.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

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
        path_rendered = "/cobrancas_vencimento_pix".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_cobrancas_vencimento_pix_by_id_cobranca_vencimento_pix(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        id_cobranca_vencimento_pix: str = None,
        body: dict = None,
    ):
        """
                Operação responsável por alterar um QR Code com vencimento.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id_cobranca_vencimento_pix: **Descrição:** Identificador da cobrança com vencimento a ser consultado.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

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
            "id_cobranca_vencimento_pix": id_cobranca_vencimento_pix,
        }
        path_rendered = "/cobrancas_vencimento_pix/{id_cobranca_vencimento_pix}".format(
            **path_params
        )
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cobrancas_vencimento_pix_by_id_cobranca_vencimento_pix_qrcode(
        self,
        *,
        x_itau_apikey: str = None,
        id_cobranca_vencimento_pix: str = None,
        x_correlation_id: Optional[str] = None,
    ):
        """
                API descontinuada. Para verificar dados de um qrcode, por favor utilizar a API ...

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id_cobranca_vencimento_pix: Id a ser consultado.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-correlationID": x_correlation_id,
        }
        path_params = {
            "id_cobranca_vencimento_pix": id_cobranca_vencimento_pix,
        }
        path_rendered = (
            "/cobrancas_vencimento_pix/{id_cobranca_vencimento_pix}/qrcode".format(
                **path_params
            )
        )
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_cobrancas_estatico_pix(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                Operação responsável por emitir um QR Code estático.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

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
        path_rendered = "/cobrancas_estatico_pix".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_cobrancas_estatico_pix_by_id_cobranca_estatico_pix(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        id_cobranca_estatico_pix: str = None,
        body: dict = None,
    ):
        """
                Operação responsável por revisar um QR Code estático.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id_cobranca_estatico_pix: **Descrição:** Identificador da cobrança estática a ser consultado.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

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
            "id_cobranca_estatico_pix": id_cobranca_estatico_pix,
        }
        path_rendered = "/cobrancas_estatico_pix/{id_cobranca_estatico_pix}".format(
            **path_params
        )
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cobrancas_estatico_pix_by_id_cobranca_estatico_pix_qrcode(
        self,
        *,
        x_itau_apikey: str = None,
        id_cobranca_estatico_pix: str = None,
        x_correlation_id: Optional[str] = None,
    ):
        """
                API descontinuada. Para verificar dados de um qrcode, por favor utilizar a API ...

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id_cobranca_estatico_pix: Id a ser consultado.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
            "x-correlationID": x_correlation_id,
        }
        path_params = {
            "id_cobranca_estatico_pix": id_cobranca_estatico_pix,
        }
        path_rendered = (
            "/cobrancas_estatico_pix/{id_cobranca_estatico_pix}/qrcode".format(
                **path_params
            )
        )
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lancamentos_pix(
        self,
        *,
        id_conta: Optional[str] = None,
        data_criacao_lancamento: Optional[str] = None,
        data_lancamento: Optional[str] = None,
        txid: Optional[str] = None,
        e2eid: Optional[str] = None,
        visao: Optional[str] = None,
        tipo_lancamento: Optional[str] = None,
        tipo_operacao: Optional[str] = None,
        tipo: Optional[str] = None,
        id_documento: Optional[str] = None,
        valor_documento_pagador_efetivo: Optional[str] = None,
        documento: Optional[str] = None,
        chaves: Optional[str] = None,
        devolvido: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        view: Optional[str] = None,
        order_by: Optional[str] = None,
        order: Optional[str] = None,
        sub_tipo_pix: Optional[str] = None,
        sub_categoria: Optional[str] = None,
        canal_operacao: Optional[str] = None,
        operacao_credito: Optional[bool] = None,
        x_itau_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                Operação responsável por resgatar os lançamentos de Pix na visão pagadora/emissora, contemplando tanto pagamentos quanto devoluções Pix.

                Args:
                    @param id_conta: **Descrição:** ID da conta que que efetuou a operação. Campo composto por codigo ISPB + agencia (4 dígitos) + conta (13 dígitos), sem o DAC.

        Exemplo: ISPB Itaú: 60701190, Agência: 1111, Conta: 12345-3, id_conta = '6070119011110000000012345'

        Para clientes indiretos, o ID da conta deve ser preenchido com a informação do ISPB indireto.

        **Observação:** É obrigatório o preenchimento do campo id_conta.

                    @param data_criacao_lancamento: **Descrição:** Range de datas de pagamento/devolução dos pixs, no formato "2020-06-01T16:00,2020-06-05T16:15" com limite de 6 meses a partir da data da consulta. Este parâmetro filtra todos lançamentos que foram consumidos e disponibilizadas na conciliação neste intervalo.

        **Observação:** É obrigatório o preenchimento do campo data_criacao_lancamento ou do campo data_lancamento. Recomenda-se a utilização da data_criacao_lancamento.

                    @param data_lancamento: **Descrição:** Range de datas para consultar a data de lançamento, no formato "2020-06-01T16:00,2020-06-05T16:15" com limite de 6 meses a partir da data da consulta. Este parâmetro filtra todos lançamentos que aconteceram no intervalo daquela data.

        **Observação:** É obrigatório o preenchimento do campo data_lancamento. Se preenchido data_criacao_lancamento, não preencher esse campo.

                    @param txid: **Descrição:** Identificador do QR Code que possibilita a conciliação de pagamentos.

        **Observação:** Para QR Code Estático, este identificador deve conter no máximo 25 posições. Para QR Code Dinâmico, este código deve possuir entre 26 a 35 posições, podendo conter letras minúsculas (a-z), letras maiúsculas (A-Z) e números (0-9).

                    @param e2eid: **Descrição:** Id fim a fim da transação.Esse campo é o id do pagamento. Transita nas mensagens de recebimento dos QR Codes e transferências.

                    @param visao: **Descrição:** Indica se a consulta deve retornar os pix pela visão emissor (os que eu emiti e forma pagos/devolvidos) ou visão pagador (os que eu paguei/ recebi devolução).

        **Observação:** Caso não informado, vem as duas visões.

                    @param tipo_lancamento: **Descrição:** Indica se a consulta deve retornar pagamentos ou devoluções, ou ambos se não informado.

                    @param tipo_operacao: **Descrição:** Tipo da operação transacional que está sendo realizada.

                    @param tipo: **Descrição:** Tipo do lançamento do Pix, podendo ser estático, dinâmico ou transferência pix.

                    @param id_documento: **Descrição:** UUID que identifica o Documento

                    @param valor_documento_pagador_efetivo: **Descrição:** CNPJ/CPF do pagador efetivo

                    @param documento: **Descrição:** CNPJ do recebedor

                    @param chaves: **Descrição:** Lista de chaves de endereçamento do recebedor, utilizada na emissão de um PIX.

        **Observação:** Inserir no formato 'chave1,chave2'

                    @param devolvido: **Descrição:** Indica se um determinado pagamento foi devolvido (parcial ou total) ou não devolvido.

                    @param page: **Descrição:** Definir um número de página para obter informações desta coleção

                    @param page_size: **Descrição:** Limitar o número de elementos por página

                    @param view: **Descrição:** Definição a visão que irá permitir o mecanismo de agrupar dados de saída de um determinado recurso.
          -- basico: retorna somente os atributos básicos do recurso
          -- completo: retorna todos os atributos do recurso

                    @param order_by: **Descrição:** Opção para ordenação.

                    @param order: **Descrição:** Opção de ordenação ascendente ou descendente.

                    @param sub_tipo_pix: **Descrição:** Subtipo do QR Code.

        **Observação:** Para QR Codes do tipo dinâmico, o subtipo pode ser imediato e vencimento. Para o QR Code do tipo estático, o subtipo pode ser estático registrado

                    @param sub_categoria: **Descrição:** Subcategoria do QR Code para filtrar saque, troco, bolecode e qrcode estático cadastral.

                    @param canal_operacao: **Descrição:** Canal utilizado para emitir o QR Code.

                    @param operacao_credito: **Descrição:** Indica se determinado QR Code foi utilizado como garantia de uma operação de crédito ou antecipado.

        **Observação:** Atualmente, apenas os QR Codes atrelados ao bolecode podem ser utilizados na operação de crédito. Vale ressaltar que o valor da operação do QR Code liquidado, quando atrelado a uma operação de crédito, não será creditado na conta emissora do QR Code.

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "id_conta": id_conta,
            "data_criacao_lancamento": data_criacao_lancamento,
            "data_lancamento": data_lancamento,
            "txid": txid,
            "e2eid": e2eid,
            "visao": visao,
            "tipo_lancamento": tipo_lancamento,
            "tipo_operacao": tipo_operacao,
            "tipo": tipo,
            "id_documento": id_documento,
            "valor_documento_pagador_efetivo": valor_documento_pagador_efetivo,
            "documento": documento,
            "chaves": chaves,
            "devolvido": devolvido,
            "page": page,
            "page_size": page_size,
            "view": view,
            "order_by": order_by,
            "order": order,
            "sub_tipo_pix": sub_tipo_pix,
            "sub_categoria": sub_categoria,
            "canal_operacao": canal_operacao,
            "operacao_credito": operacao_credito,
        }
        headers = {
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/lancamentos_pix".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lancamentos_pix_by_id_lancamento_pix(
        self, *, id_lancamento_pix: str = None, x_itau_apikey: str = None
    ):
        """
                Operação responsável por recuperar um lançamento PIX especifico

                Args:
                    @param id_lancamento_pix: **Descrição:** ID do lancamento_pix

                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "id_lancamento_pix": id_lancamento_pix,
        }
        path_rendered = "/lancamentos_pix/{id_lancamento_pix}".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_estabelecimento_saque_troco_pix(
        self,
        *,
        ponto_atendimento_id: str = None,
        x_itau_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API responsável por efetuar a remoção de um ou mais pontos de atendimento do Saque e Troco Pix.

                Args:
                    @param ponto_atendimento_id: **Descrição:**  O campo ponto_atendimento_id determina o identificador do ponto de atendimento. O objetivo desse campo é ser um elemento que possibilite a busca de um ponto de atendimento especifico.

        **Observação:** Os caracteres permitidos no contexto do Pix para o campo txId são: Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’.

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail

                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "ponto_atendimento_id": ponto_atendimento_id,
        }
        headers = {
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/estabelecimento_saque_troco_pix".format(**path_params)
        response = requests.delete(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_estabelecimento_saque_troco_pix(
        self,
        *,
        ponto_atendimento_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        x_itau_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API responsável por recuperar os dados do(s) ponto(s) de atendimento do agente de saque. É possivel consultar um ponto de atendimento especifico atraves de seu respectivo ID. Caso o ID não seja informado na busca serão retornados todos os pontos de atendimento do agente em questão.

                Args:
                    @param ponto_atendimento_id: **Descrição:**  O campo ponto_atendimento_id determina o identificador do ponto de atendimento. O objetivo desse campo é ser um elemento que possibilite a busca de um ponto de atendimento especifico.

        **Observação:** Os caracteres permitidos no contexto do Pix para o campo txId são: Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’.

                    @param page: Número da página que está sendo requisitada
                    @param page_size: Quantidade total de registros de pontos de atendimento por página
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "ponto_atendimento_id": ponto_atendimento_id,
            "page": page,
            "page-size": page_size,
        }
        headers = {
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/estabelecimento_saque_troco_pix".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_estabelecimento_saque_troco_pix(
        self,
        *,
        x_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
        body: dict = None,
    ):
        """
                O Saque e Troco Pix permite a disponibilização do serviço de saque de dinheiro nos estabelecimento comerciais. No troco o valor do QR Code é superior ao valor da compra e o estabelecimento devolve ao cliente o valor excedente em espécie. No saque será repassado o valor total do QR Code ao cliente sacador. Essa API é responsável por efetuar o cadastro de um ou mais pontos de atendimento para esse serviço. No momento do cadastro de um ponto de atendimento, serão validados os campos obrigatórios bem como os campos de domínios definidos no contrato da API. Além disso, também serão validadas as regras de negócio de acordo com os parâmetros enviados no corpo da requisição.

                Args:
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-correlationID": x_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/estabelecimento_saque_troco_pix".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_estabelecimento_saque_troco_pix_by_ponto_atendimento_id(
        self,
        *,
        ponto_atendimento_id: str = None,
        x_itau_apikey: str = None,
        body: dict = None,
    ):
        """
                Atualiza pontos de atendimento de um agente de saque

                Args:
                    @param ponto_atendimento_id: Identificador do ponto de atendimento.
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "ponto_atendimento_id": ponto_atendimento_id,
        }
        path_rendered = (
            "/estabelecimento_saque_troco_pix/{ponto_atendimento_id}".format(
                **path_params
            )
        )
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_boletos_pix(
        self,
        *,
        x_itau_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
        body: dict = None,
    ):
        """
                API responsável por efetuar a emissão de um boleto + Pix. Obs: Por regras internas não é permitido o uso de caracter especial, tais como os exemplos: *“ [ “ , “ : “ , “ < ” , “ > ” , “ & ” , “ ; ” , “ ' “ , “ " “ , “ ` “ , “ ( “ , “ ) “ , “ # “ , “ ** “ , “ / “ , “ | “ , “ *] “ , “ ü ” , “ http “ , “ javascript “ , “ alert “

                Args:
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/boletos_pix".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_boletos_pix_indireto(
        self,
        *,
        x_itau_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
        body: dict = None,
    ):
        """
                EM CONSTRUÇÃO Emissão de bolecode para participantes indiretos do PIX

                Args:
                    @param x_itau_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/boletos_pix_indireto".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()
