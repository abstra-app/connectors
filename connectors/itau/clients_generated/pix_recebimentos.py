"""
APIs Regulatórias Pix Recebimentos v2.69.36
API Emissão/Alteração, Devolução, Location, Lote e Devolução de QRCodes PIX para Participantes Diretos

"""

import requests
from typing import Optional


class PixRecebimentosClient:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def put_cob_by_txid(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        txid: str = None,
        body: dict = None,
    ):
        """
                API para emitir um QR Code imediato.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param txid: **Descrição:** Identificador do QR Code que possibilita a conciliação de pagamentos.

        **Observação:** Este código deve possuir entre 26 e 35 posições, podendo conter letras minúsculas (a-z), letras maiúsculas (A-Z) e números (0-9).

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
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cob/{txid}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_cob_by_txid(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        txid: str = None,
        body: dict = None,
    ):
        """
                API para alterar ou cancelar um QR Code imediato.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param txid: **Descrição:** Identificador do QR Code que possibilita a conciliação de pagamentos.

        **Observação:** Este código deve possuir entre 26 e 35 posições, podendo conter letras minúsculas (a-z), letras maiúsculas (A-Z) e números (0-9).

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
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cob/{txid}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cob_by_txid(
        self,
        *,
        txid: str = None,
        revisao: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API para consultar um QR Code imediato específico através do identificador do QR Code (txid).

                Args:
                    @param txid: Txid a ser consultado.
                    @param revisao: Id de transação do documento, utilizado para a sua identificação no banco central
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if revisao is not None:
            query["revisao"] = revisao
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cob/{txid}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_cob(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                API para emitir um QR Code imediato em que o Itaú é responsável por criar o identificador do QR Code (txid).

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
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        path_params = {}
        path_rendered = "/cob".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cob(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        cpf: Optional[str] = None,
        cnpj: Optional[str] = None,
        location_presente: Optional[bool] = None,
        status: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
        x_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API para consultar uma listagem de QR Codes imediatos.

                Args:
                    @param inicio: Data inicial. Respeita RFC 3339.
                    @param fim: Data de fim. Respeita RFC 3339.
                    @param cpf: CPF do pagador cadastrado na cobrança.
                    @param cnpj: CNPJ do pagador cadastrado na cobrança.
                    @param location_presente: Indicador se localização está presente.
                    @param status: Filtro pelo Status da cobrança. Pode ser ATIVA, CONCLUIDA, REMOVIDA_PELO_PSP OU REMOVIDA_PELO_USUARIO_RECEBEDOR
                    @param paginacao_pagina_atual: Numero da Página que deseja realizar o acesso, valor considerado por default 0.
                    @param paginacao_itens_por_pagina: Quantidade de ocorrência retornadas por pagina, valor por default 100.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if cpf is not None:
            query["cpf"] = cpf
        if cnpj is not None:
            query["cnpj"] = cnpj
        if location_presente is not None:
            query["locationPresente"] = location_presente
        if status is not None:
            query["status"] = status
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        if x_correlation_id is not None:
            headers["x-correlationID"] = x_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        path_rendered = "/cob".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_cob_by_txid_qrcode(
        self,
        *,
        txid: str = None,
        x_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API descontinuada. Para verificar dados de um qrcode, por favor utilizar a API **GET /cob/{txid}**.

                Args:
                    @param txid: Txid a ser consultado.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_correlation_id is not None:
            headers["x-correlationID"] = x_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cob/{txid}/qrcode".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_cobv_by_txid(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        txid: str = None,
        body: dict = None,
    ):
        """
                API para emitir um QR Code com vencimento.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param txid: **Descrição:** Identificador do QR Code que possibilita a conciliação de pagamentos.

        **Observação:** Este código deve possuir entre 26 e 35 posições, podendo conter letras minúsculas (a-z), letras maiúsculas (A-Z) e números (0-9).

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
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobv/{txid}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_cobv_by_txid(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        txid: str = None,
        body: dict = None,
    ):
        """
                API para alterar ou cancelar um QR Code com vencimento.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param txid: **Descrição:** Identificador do QR Code que possibilita a conciliação de pagamentos.

        **Observação:** Este código deve possuir entre 26 e 35 posições, podendo conter letras minúsculas (a-z), letras maiúsculas (A-Z) e números (0-9).

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
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobv/{txid}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cobv_by_txid(
        self,
        *,
        txid: str = None,
        revisao: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API para consultar um QR Code com vencimento específico através do identificador do QR Code (txid).

                Args:
                    @param txid: Txid a ser consultado.
                    @param revisao: Revisão do documento, utilizado para a sua identificação no banco central
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if revisao is not None:
            query["revisao"] = revisao
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobv/{txid}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_cobv(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        cpf: Optional[str] = None,
        cnpj: Optional[str] = None,
        location_presente: Optional[bool] = None,
        status: Optional[str] = None,
        lote_cob_v_id: Optional[int] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
        x_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API para consultar uma listagem de QR Codes com vencimento.

                Args:
                    @param inicio: Data inicial. Respeita RFC 3339.
                    @param fim: Data de fim. Respeita RFC 3339.
                    @param cpf: CPF do devedor cadastrado na cobrança.
                    @param cnpj: CNPJ do devedor cadastrado na cobrança.
                    @param location_presente: Indicador se localização está presente.
                    @param status: Filtro pelo Status da cobrança. Pode ser ATIVA, CONCLUIDA, REMOVIDA_PELO_PSP OU REMOVIDA_PELO_USUARIO_RECEBEDOR
                    @param lote_cob_v_id: Id do lote de cobrança com vencimento.
                    @param paginacao_pagina_atual: Numero da Página que deseja realizar o acesso, valor considerado por default 0.
                    @param paginacao_itens_por_pagina: Quantidade de ocorrência retornadas por pagina, valor por default 100.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if cpf is not None:
            query["cpf"] = cpf
        if cnpj is not None:
            query["cnpj"] = cnpj
        if location_presente is not None:
            query["locationPresente"] = location_presente
        if status is not None:
            query["status"] = status
        if lote_cob_v_id is not None:
            query["loteCobVId"] = lote_cob_v_id
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        if x_correlation_id is not None:
            headers["x-correlationID"] = x_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        path_rendered = "/cobv".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_cobv_by_txid_qrcode(
        self,
        *,
        txid: str = None,
        x_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API descontinuada. Para verificar dados de um qrcode, por favor utilizar a API **GET /cobv/{txid}**.

                Args:
                    @param txid: Txid a ser consultado.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_correlation_id is not None:
            headers["x-correlationID"] = x_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobv/{txid}/qrcode".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_lotecobv_by_id(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        id: str = None,
        body: dict = None,
    ):
        """
                API para emitir ou alterar um lote de QR Codes com vencimento.

        Para o caso de uso de alteração de QR Code, o array a ser atribuído na requisição e deve ser composto pelas exatas requisições de criação de QR Code com vencimento que constaram no array atribuído na requisição originária.

        Não se pode utilizar esta API para alterar um lote de QR Code com vencimento agregando ou removendo um QR Code já existente dentro do conjunto de QR Codes criados na requisição originária do lote.

        Em outras palavras, se originalmente criou-se um lote, por exemplo, com QR Codes [`a`, `b` e `c`], não se pode alterar esse conjunto de QR Codes originais que o lote representa para [`a`, `b`, `c`, `d`], ou para [`a`, `b`]. Por outro lado, pode-se alterar, em lote os QR Codes [`a`, `b`, `c`], conforme originalmente constam na requisição originária do lote.

        Uma solicitação de criação de QR Code com status "EM_PROCESSAMENTO" ou "NEGADA" está associada a um QR Code não existe de fato, portanto não será listada em `GET /cobv` ou `GET /cobv/{txid}`.

        Um QR Code, uma vez criado via `PUT /cobv/{txid}`, não pode ser associada a um lote posteriormente.

        Um QR Code, uma vez criada via `PUT /lotecobv/{id}`, não pode ser associada a um novo lote posteriormente.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id: **Descrição:** Identificador da lotecobv.

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
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotecobv/{id}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_lotecobv_by_id(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        id: str = None,
        body: dict = None,
    ):
        """
                API para revisar um QR Code com vencimento específico dentro de um lote de QR Codes com vencimento.

        A diferença desta API para a API PUT correlato é que esta API admite um array `cobsv` com menos solicitações de criação ou alteração de QR Code do que o array atribuído na requisição originária do lote.

        Não se pode, entretanto, utilizar essa API  para agregar ou remover solicitações de alteração ou criação de QR Codes conforme constam na requisição originária do lote.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id: **Descrição:** Identificador da lotecobv.

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
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotecobv/{id}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_lotecobv_by_id(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        id: str = None,
    ):
        """
                API para consultar um lote de QR Codes com vencimento.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id: **Descrição:** Identificador da lotecobv.

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotecobv/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_lotecobv(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        inicio: str = None,
        fim: str = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                API para consultar uma listagem de lotes de QR Codes com vencimento.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param inicio: **Descrição:** Data inicial.

        **Observação:** Respeita RFC 3339.

                    @param fim: **Descrição:** Data de fim.

        **Observação:** Respeita RFC 3339.

                    @param paginacao_pagina_atual: **Descrição:** Numero da Página que deseja realizar o acesso.

        **Observação:** Valor considerado por default 0.

                    @param paginacao_itens_por_pagina: **Descrição:** Quantidade de ocorrência retornadas por pagina.

        **Observação:** valor por default 100.

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        path_params = {}
        path_rendered = "/lotecobv".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_loc(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        body: dict = None,
    ):
        """
                API para criar uma location.

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
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        path_params = {}
        path_rendered = "/loc".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_loc(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        tx_id_presente: Optional[bool] = None,
        tipo_cob: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
        x_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API para consultar uma listagem de locations cadastradas.

                Args:
                    @param inicio: Data inicial. Respeita RFC 3339.
                    @param fim: Data de fim. Respeita RFC 3339.
                    @param tx_id_presente: Filtro pela existência de txid.
                    @param tipo_cob: Define se o tipo do documento é imediata ou vencimento
        <table><tr><td>ENUM</td></tr><tr><td>cob</td></tr><tr><td>cobv</td></tr></table>

                    @param paginacao_pagina_atual: Numero da Página que deseja realizar o acesso, valor considerado por default 0.
                    @param paginacao_itens_por_pagina: Quantidade de ocorrência retornadas por pagina, valor por default 100.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if tx_id_presente is not None:
            query["txIdPresente"] = tx_id_presente
        if tipo_cob is not None:
            query["tipoCob"] = tipo_cob
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        if x_correlation_id is not None:
            headers["x-correlationID"] = x_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        path_rendered = "/loc".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_loc_by_id(self, *, id: str = None, x_itau_apikey: str = None):
        """
                API para consultar uma location específica através do identificador da location.

                Args:
                    @param id: id da devolução
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/loc/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_loc_by_id_txid(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        id: str = None,
    ):
        """
                API para desvincular um QR Code de uma location.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param id: **Descrição:** Identificador da location.

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        if x_itau_correlation_id is not None:
            headers["x-itau-correlationID"] = x_itau_correlation_id
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/loc/{id}/txid".format(**path_params)
        response = requests.delete(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pix_by_e2eid(self, *, e2eid: str = None, x_itau_apikey: str = None):
        """
                API para consultar um Pix recebido, seja QR Code ou transferência Pix, através do identificador do pagamento (e2eid).

                Args:
                    @param e2eid: Id fim a fim da transação.
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if e2eid is not None:
            path_params["e2eid"] = e2eid
        path_rendered = "/pix/{e2eid}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pix(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        txid: Optional[str] = None,
        txid_presente: Optional[bool] = None,
        devolucao_presente: Optional[bool] = None,
        cpf: Optional[str] = None,
        cnpj: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
        x_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API para consultar uma listagem de Pix recebidos, seja QR Code ou transferência Pix.

                Args:
                    @param inicio: Data inicial. Respeita RFC 3339.
                    @param fim: Data de fim. Respeita RFC 3339.
                    @param txid: ID de identificação do documento entre os bancos e o cliente emissor. O campo txid é obrigatório e determina o identificador da transação.O objetivo desse campo é ser um elemento que possibilite a conciliação de pagamentos. O txid é criado exclusivamente pelo usuário recebedor e está sob sua responsabilidade. Deve ser único por CNPJ do recebedor. Apesar de possuir o tamanho de 35 posições (PAC008), para QR Code Estático o tamanho máximo permitido é de 25 posições (limitação EMV). No caso do QR Code dinâmico o campo deve possuir de 26 posição até 35 posições. Os caracteres permitidos no contexto do Pix para o campo txId são:Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’
                    @param txid_presente: Indicador do indentificador da taxa.
                    @param devolucao_presente: Indicador de devolução.
                    @param cpf: CPF do pagador cadastrado na cobrança
                    @param cnpj: CNPJ do pagador cadastrado na cobrança.
                    @param paginacao_pagina_atual: Numero da Página que deseja realizar o acesso, valor considerado por default 0.
                    @param paginacao_itens_por_pagina: Quantidade de ocorrência retornadas por pagina, valor por default 100.
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if txid is not None:
            query["txid"] = txid
        if txid_presente is not None:
            query["txidPresente"] = txid_presente
        if devolucao_presente is not None:
            query["devolucaoPresente"] = devolucao_presente
        if cpf is not None:
            query["cpf"] = cpf
        if cnpj is not None:
            query["cnpj"] = cnpj
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        if x_correlation_id is not None:
            headers["x-correlationID"] = x_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        path_rendered = "/pix".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_pix_by_e2eid_devolucao_by_id(
        self,
        *,
        x_itau_apikey: str = None,
        x_itau_correlation_id: Optional[str] = None,
        e2eid: str = None,
        id: str = None,
        body: dict = None,
    ):
        """
                API para solicitar uma devolução através do identificador de pagamento (e2eid) e do identificador da devolução (id). A configuração de timeout dessa api não pode ser inferior a 30 segundos.

                Args:
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param x_itau_correlation_id: **Descrição:** Identificador de correlação que serve como um agrupador dentro da estrutura de audit trail.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param e2eid: **Descrição:** Identificador fim a fim da transação.

                    @param id: **Descrição:** Identificador da devolução.

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
        path_params = {}
        if e2eid is not None:
            path_params["e2eid"] = e2eid
        if id is not None:
            path_params["id"] = id
        path_rendered = "/pix/{e2eid}/devolucao/{id}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_pix_by_e2eid_devolucao_by_id(
        self, *, e2eid: str = None, id: str = None, x_itau_apikey: str = None
    ):
        """
                API para consultar uma devolução através do identificador de pagamento (e2eid) e do identificador da devolução (id).

                Args:
                    @param e2eid: Id fim a fim da transação.
                    @param id: id da devolução
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if e2eid is not None:
            path_params["e2eid"] = e2eid
        if id is not None:
            path_params["id"] = id
        path_rendered = "/pix/{e2eid}/devolucao/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_webhook_by_chave(
        self, *, chave: str = None, x_itau_apikey: str = None, body: dict = None
    ):
        """
                API para configurar o serviço de notificações via webhook dos QR Codes recebidos e das transferências Pix recebidas via chave Pix para uma chave Pix.

        **Observação:** Transferências Pix recebidas com inserção manual (agência e conta) não serão notificadas.

                Args:
                    @param chave: Chave de endereçamento do recebedor
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if chave is not None:
            path_params["chave"] = chave
        path_rendered = "/webhook/{chave}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_webhook_by_chave(self, *, chave: str = None, x_itau_apikey: str = None):
        """
                API para consultar o serviço de notificações via webhook de uma chave Pix específica.

                Args:
                    @param chave: Chave de endereçamento do recebedor
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if chave is not None:
            path_params["chave"] = chave
        path_rendered = "/webhook/{chave}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_webhook_by_chave(self, *, chave: str = None, x_itau_apikey: str = None):
        """
                API para excluir uma o serviço de notificação de recebimento de chave Pix via webhook.

                Args:
                    @param chave: Chave de endereçamento do recebedor
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {}
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        if chave is not None:
            path_params["chave"] = chave
        path_rendered = "/webhook/{chave}".format(**path_params)
        response = requests.delete(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_webhook(
        self,
        *,
        inicio: Optional[str] = None,
        fim: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
        x_correlation_id: Optional[str] = None,
        x_itau_apikey: str = None,
    ):
        """
                API para consultar a listagem dos serviço de notificações via webhook cadastrados.

                Args:
                    @param inicio: Data de inicio da pesquisa de webhooks, no formato de acordo com RFC3339
                    @param fim: Data fim da pesquisa de webhooks, no formato de acordo com RFC3339
                    @param paginacao_pagina_atual: Numero da Página que deseja realizar o acesso, valor considerado por default 0
                    @param paginacao_itens_por_pagina: Quantidade de ocorrência retornadas por pagina, valor por default 100
                    @param x_correlation_id: Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail
                    @param x_itau_apikey: **Descrição:** Chave da API utilizado para autorizar o consumo de uma aplicação requisitante.

        **RegEx:** `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        if x_correlation_id is not None:
            headers["x-correlationID"] = x_correlation_id
        if x_itau_apikey is not None:
            headers["x-itau-apikey"] = x_itau_apikey
        path_params = {}
        path_rendered = "/webhook".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
