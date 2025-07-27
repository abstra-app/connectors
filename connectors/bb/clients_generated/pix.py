"""
Pix v2.8.6
A API Pix padroniza serviços oferecidos pelo PSP recebedor no contexto do arranjo Pix, como criação de cobrança, verificação de Pix recebidos, devolução e conciliação. Os serviços expostos pelo PSP recebedor permitem ao usuário recebedor estabelecer integração de sua automação com os serviços Pix do PSP.
<br><br>
Documentação de referência Bacen: [2.8.2](https://github.com/bacen/pix-api/releases/tag/2.8.2).
"""

import requests
from typing import Optional


class PixClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def get_webhookcobr(self):
        """
                Endpoint para recuperação de informações sobre o Webhook.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/webhookcobr".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_webhookcobr(self):
        """
                Endpoint para cancelamento do webhook. Não é a única forma pela qual um webhook pode ser removido.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/webhookcobr".format(**path_params)
        response = requests.delete(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_webhookcobr(self, *, body: dict = None):
        """
                Endpoint para configuração do serviço de notificações acerca de cobranças recorrentes. Somente cobranças recorrentes associadas ao usuário recebedor serão notificadas.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/WebhookOperacaoInvalida",
          "title": "Webhook inválido.",
          "status": 400,
          "detail": "A presente requisição busca criar um webhook sem respeitar o _schema_ ou, ainda, com sentido semanticamente inválido."
        }
        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/webhookcobr".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_pix(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        txid: Optional[str] = None,
        tx_id_presente: Optional[bool] = None,
        devolucao_presente: Optional[bool] = None,
        cpf: Optional[str] = None,
        cnpj: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                Endpoint para consultar Pix recebidos
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Data inicial da pesquisa. Intervalo máximo: 5 dias.
                    @param fim: Data final da pesquisa. Intervalo máximo: 5 dias.
                    @param txid: txid
                    @param tx_id_presente: txIdPresente
                    @param devolucao_presente: devolucaoPresente
                    @param cpf: cpf
                    @param cnpj: cnpj
                    @param paginacao_pagina_atual: paginacao.paginaAtual
                    @param paginacao_itens_por_pagina: paginacao.itensPorPagina
        """
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if txid is not None:
            query["txid"] = txid
        if tx_id_presente is not None:
            query["txIdPresente"] = tx_id_presente
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
        path_params = {}
        path_rendered = "/pix".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_locrec_by_id_id_rec(self, *, id: str = None):
        """
                Endpoint utilizado para desvincular uma recorrência de uma location.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id: Id da location cadastrada para servir um payload
        """
        query = {}
        headers = {}
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/locrec/{id}/idRec".format(**path_params)
        response = requests.delete(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_cob_by_txid(self, *, txid: str = None, body: dict = None):
        """
                Endpoint para revisar uma cobrança imediata.
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/CobOperacaoInvalida",
            "title": "Operação inválida.",
            "status": 400,
            "detail": "A requisição que busca alterar ou criar uma cobrança para pagamento imediato não respeita o _schema_ ou está semanticamente errada."
        }
        ```
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: txid
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cob/{txid}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cob_by_txid(self, *, txid: str = None):
        """
                Endpoint para consultar uma cobrança através de um determinado txid.
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }

                Args:
                    @param txid: txid
        """
        query = {}
        headers = {}
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

    def put_cob_by_txid(self, *, txid: str = None, body: dict = None):
        """
                Endpoint para criar uma cobrança imediata.
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/CobOperacaoInvalida",
          "title": "Cobrança inválida.",
          "status": 400,
          "detail": "A requisição que busca alterar ou criar uma cobrança para pagamento imediato não respeita o _schema_ ou está semanticamente errada.",
          "violacoes": [
            {}
          ]
        }
        ```
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: txid
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cob/{txid}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def delete_loc_by_id_txid(self, *, id: str = None):
        """
                Endpoint utilizado para desvincular uma cobrança de uma location.

        Se executado com sucesso, a entidade loc não apresentará mais um txid, se apresentava anteriormente à chamada. Adicionalmente, a entidade cob ou cobv associada ao txid desvinculado também passará a não mais apresentar um location. Esta operação não altera o status da cob ou cobv em questão.
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id: Id da location cadastrada para servir um payload
        """
        query = {}
        headers = {}
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

    def patch_lotecobv_by_id(self, *, id: str = None, body: dict = None):
        """
                Endpoint utilizado para revisar cobranças específicas dentro de um lote de cobranças com vencimento.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/CobVOperacaoInvalida",
          "title": "Operação inválida.",
          "status": 400,
          "detail": "Cobrança não encontra-se mais com o status ATIVA, somente cobranças ativas podem ser revisadas."
        }
        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id: Identificador do lote de cobranças com vencimento, em formato de texto.
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotecobv/{id}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_lotecobv_by_id(self, *, id: str = None):
        """
                Endpoint para consultar um lote de cobranças com vencimento.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id: Identificador do lote de cobranças com vencimento
        """
        query = {}
        headers = {}
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

    def put_lotecobv_by_id(self, *, id: str = None, body: dict = None):
        """
                Endpoint utilizado para criar ou alterar um lote de cobranças com vencimento.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/LoteCobVOperacaoInvalida",
          "title": "Lote de cobranças inválido.",
          "status": 400,
          "detail": "A requisição que busca alterar ou criar um lote de cobranças com vencimento não respeita o _schema_ ou está semanticamente errada.",
          "violacoes": [
            {
              "razao": "O objeto loteCobV.cobsV não respeita o _schema_.",
              "propriedade": "loteCobV.cobsV"
            },
            {
              "razao": "O campo loteCobV.descricao não respeita o _schema_.",
              "propriedade": "loteCobV.descricao"
            }
          ]
        }
        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id: Identificador do lote de cobranças com vencimento, em formato de texto.
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/lotecobv/{id}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_rec(self, *, body: dict = None):
        """
                Endpoint utilizado para criar recorrência.
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/RecOperacaoInvalida",
          "title": "Operação inválida.",
          "status": 400,
          "detail": "A recorrência não respeita o schema.",
          "violacoes": [
            {
              "razao": "O campo rec.calendario.dataInicial não respeita o schema.",
              "propriedade": "rec.calendario.dataInicial"
            }
          ]
        }
        ```
        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/rec".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_rec(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        cpf: Optional[str] = None,
        cnpj: Optional[str] = None,
        location_presente: Optional[bool] = None,
        status: Optional[str] = None,
        convenio: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                Endpoint utilizado para consultar lista de recorrências.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Data de início - Filtra os registros cuja data de criação seja maior ou igual que a data de início. Respeita RFC 3339.
                    @param fim: Data de fim - Filtra os registros cuja data de criação seja menor ou igual que a data de fim. Respeita RFC 3339.
                    @param cpf: CPF - Filtro pelo CPF do devedor. Não pode ser utilizado ao mesmo tempo que o CNPJ.
                    @param cnpj: CNPJ - Filtro pelo CNPJ do devedor. Não pode ser utilizado ao mesmo tempo que o CPF.
                    @param location_presente: Filtro pela existência de location vinculada.
                    @param status: Status do registro da recorrência - Filtro pelo status da recorrência.
                    @param convenio: Convênio entre usuário e participante recebedor.
                    @param paginacao_pagina_atual: Página atual - Página a ser retornada pela consulta. Se não for informada, o PSP assumirá que será 0.
        Default: 0
                    @param paginacao_itens_por_pagina: Itens por Página - Quantidade máxima de registros retornados em cada página. Apenas a última página pode conter uma quantidade menor de registros.
        Default: 100
        """
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
        if convenio is not None:
            query["convenio"] = convenio
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        path_params = {}
        path_rendered = "/rec".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pix_by_e2eid_devolucao_by_id(self, *, e2eid: str = None, id: str = None):
        """
                Endpoint para consultar uma devolução através de um End To End ID do Pix e do ID da devolução
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param e2eid: e2eid
                    @param id: id
        """
        query = {}
        headers = {}
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

    def put_pix_by_e2eid_devolucao_by_id(
        self, *, e2eid: str = None, id: str = None, body: dict = None
    ):
        """
                Endpoint para solicitar uma devolução através de um e2eid do Pix e do ID da devolução. O motivo que será atribuído à PACS.004 será "Devolução solicitada pelo usuário recebedor do pagamento original" cuja sigla é "MD06" de acordo com a aba RTReason da PACS.004 que consta no Catálogo de Mensagens do Pix.
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/PixDevolucaoInvalida",
            "title": "Devolução inválida.",
            "status": 400,
            "detail": "A presente requisição de devolução não respeita o _schema_ ou não faz sentido semanticamente."
        }
        ```
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param e2eid: e2eid
                    @param id: id
                    @param body: No description provided.
        """
        query = {}
        headers = {}
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

    def post_solicrec(self, *, body: dict = None):
        """
                Endpoint utilizado para criar solicitação de confirmação de recorrência.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/SolicRecOperacaoInvalida",
          "title": "Operação inválida.",
          "status": 400,
          "detail": "A solicitação de confirmação de recorrência não respeita o schema.",
          "violacoes": [
            {
              "razao": "O objeto solicrec.destinatario não respeita o schema.",
              "propriedade": "solicrec.destinatario"
            }
          ]
        }

        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/solicrec".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_cobv_by_txid(self, *, txid: str = None, body: dict = None):
        """
                Endpoint para revisar uma cobrança com vencimento.
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/CobVOperacaoInvalida",
            "title": "Operação inválida.",
            "status": 400,
            "detail": "Cobrança não encontra-se mais com o status ATIVA, somente cobranças ativas podem ser revisadas."
        }
        ```
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: txid
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobv/{txid}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cobv_by_txid(self, *, txid: str = None, revisao: Optional[int] = None):
        """
                Endpoint para consultar uma cobrança com vencimento através de um determinado txid.
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: txid
                    @param revisao: revisao
        """
        query = {}
        if revisao is not None:
            query["revisao"] = revisao
        headers = {}
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

    def put_cobv_by_txid(self, *, txid: str = None, body: dict = None):
        """
                Endpoint para criar uma cobrança com vencimento.
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/CobVOperacaoInvalida",
            "title": "Cobrança inválida.",
            "status": 400,
            "detail": "A requisição que busca alterar ou criar uma cobrança com vencimento não respeita o _schema_ ou está semanticamente errada.",
            "violacoes": [
                {
                    "razao": "O objeto cobv.devedor não respeita o _schema_.",
                    "propriedade": "cobv.devedor"
                }
            ]
        }
        ```
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: txid
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobv/{txid}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_webhook(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                Endpoint para consultar Webhooks cadastrados
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: data inicial da pesquisa. Intervalo máximo: 5 dias.
                    @param fim: data final da pesquisa. Intervalo máximo: 5 dias.
                    @param paginacao_pagina_atual: Default value : 0
                    @param paginacao_itens_por_pagina: Default value : 100
        """
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
        path_params = {}
        path_rendered = "/webhook".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_locrec(self):
        """
                Endpoint para criar location do payload
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/locrec".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_locrec(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        id_rec_presente: Optional[bool] = None,
        convenio: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                Endpoint para consultar locations cadastradas
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Data de início - Filtra os registros cuja data de criação seja maior ou igual que a data de início. Respeita RFC 3339.
                    @param fim: Data de fim - Filtra os registros cuja data de criação seja menor ou igual que a data de fim. Respeita RFC 3339.
                    @param id_rec_presente: Filtro pela existência de id da recorrência:
        true  traz somente location com idRec
        false  traz somente location sem idRec
                    @param convenio: Convenio
                    @param paginacao_pagina_atual: Página atual - Página a ser retornada pela consulta. Se não for informada, o PSP assumirá que será 0.
        Default: 0
                    @param paginacao_itens_por_pagina: Itens por Página - Quantidade máxima de registros retornados em cada página. Apenas a última página pode conter uma quantidade menor de registros.
        Default: 100
        """
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if id_rec_presente is not None:
            query["idRecPresente"] = id_rec_presente
        if convenio is not None:
            query["convenio"] = convenio
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        path_params = {}
        path_rendered = "/locrec".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_webhook_by_chave(self, *, chave: str = None):
        """
                Endpoint para recuperação de informações sobre o Webhook Pix
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada.",
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param chave: chave
        """
        query = {}
        headers = {}
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

    def delete_webhook_by_chave(self, *, chave: str = None):
        """
                Endpoint para cancelamento do webhook. Não é a única forma pela qual um webhook pode ser removido.

        O PSP recebedor está livre para remover unilateralmente um webhook que esteja associado a uma chave que não pertence mais a este usuário recebedor.
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param chave: chave
        """
        query = {}
        headers = {}
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

    def put_webhook_by_chave(self, *, chave: str = None, body: dict = None):
        """
                Endpoint para configuração do serviço de notificações acerca de Pix recebidos. Somente Pix associados a um txid serão notificados.
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param chave: chave
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if chave is not None:
            path_params["chave"] = chave
        path_rendered = "/webhook/{chave}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_cobr_by_txid(self, *, txid: str = None, body: dict = None):
        """
                Endpoint para revisar uma cobrança recorrente.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/CobROperacaoInvalida",
          "title": "Operação inválida.",
          "status": 400,
          "detail": "Não é possível cancelar uma cobrança em uma data igual ou maior que a data prevista da primeira tentativa de liquidação."
        }
        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: Id da Transação
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobr/{txid}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cobr_by_txid(self, *, txid: str = None):
        """
                Endpoint para consultar uma cobrança recorrente através de um determinado txid.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: Id da Transação - Identificador da transação único por CPF/CNPJ do usuário recebedor.
        """
        query = {}
        headers = {}
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobr/{txid}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_cobr_by_txid(self, *, txid: str = None, body: dict = None):
        """
                Endpoint para criar uma cobrança recorrente.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/CobROperacaoInvalida",
          "title": "Operação inválida.",
          "status": 400,
          "detail": "A cobrança não respeita o schema.",
          "violacoes": [
            {
              "razao": "O objeto cobr.calendario não respeita o schema.",
              "propriedade": "cobr.calendario"
            }
          ]
        }
        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: Id da Transação
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        path_rendered = "/cobr/{txid}".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def patch_rec_by_id_rec(self, *, id_rec: str = None, body: dict = None):
        """
                Endpoint utilizado para revisar recorrência.
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/RecOperacaoInvalida",
          "title": "Operação inválida.",
          "status": 400,
          "detail": "A recorrência não respeita o schema.",
          "violacoes": [
            {
              "razao": "O campo rec.calendario.dataInicial não respeita o schema.",
              "propriedade": "rec.calendario.dataInicial"
            }
          ]
        }
        ```
        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id_rec: ID Recorrência - Id da location cadastrada para servir um payload
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if id_rec is not None:
            path_params["idRec"] = id_rec
        path_rendered = "/rec/{idRec}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_rec_by_id_rec(self, *, id_rec: str = None, txid: Optional[str] = None):
        """
                Endpoint utilizado para consultar recorrência.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id_rec: ID Recorrência - Id da location cadastrada para servir um payload
                    @param txid: TxId da cobrança associada a recorrência
        """
        query = {}
        if txid is not None:
            query["txid"] = txid
        headers = {}
        path_params = {}
        if id_rec is not None:
            path_params["idRec"] = id_rec
        path_rendered = "/rec/{idRec}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_loc(self, *, body: dict = None):
        """
                Endpoint para criar location do payload
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/PayloadLocationOperacaoInvalida",
            "title": "PayloadLocation inválido.",
            "status": 400,
            "detail": "A presente requisição busca criar uma location sem respeitar o _schema_ estabelecido."
        }
        ```
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param body: No description provided.
        """
        query = {}
        headers = {}
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
    ):
        """
                Endpoint para consultar locations cadastradas
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada.",
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Filtra os registros cuja data de criação seja maior ou igual que a data de início. Respeita RFC 3339.
                    @param fim: Filtra os registros cuja data de criação seja menor ou igual que a data de fim. Respeita RFC 3339.
                    @param tx_id_presente: txIdPresente
                    @param tipo_cob: Available values : "cob", "cobv"
                    @param paginacao_pagina_atual: Página a ser retornada pela consulta. Se não for informada, o PSP assumirá que será 0.

        Default value : 0
                    @param paginacao_itens_por_pagina: Quantidade máxima de registros retornados em cada página. Apenas a última página pode conter uma quantidade menor de registros.

        Default value : 100
        """
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
        path_params = {}
        path_rendered = "/loc".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_loc_by_id(self, *, id: str = None):
        """
                Recupera a location do payload
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id: Id da location cadastrada para servir um payload
        """
        query = {}
        headers = {}
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

    def post_cobr_by_txid_retentativa_by_data(
        self, *, txid: str = None, data: str = None
    ):
        """
                Endpoint para solicitar retentativa de uma cobrança recorrente.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://pix.bcb.gov.br/api/v2/error/CobROperacaoInvalida",
          "title": "Cobrança não encontrada.",
          "status": 400,
          "detail": "A política configurada na recorrência não permite retentativa de cobrança."
        }

        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param txid: Id da Transação
                    @param data: Data prevista para liquidação da ordem de pagamento correspondente. Trata-se de uma data, no formato YYYY-MM-DD, segundo ISO 8601.
        """
        query = {}
        headers = {}
        path_params = {}
        if txid is not None:
            path_params["txid"] = txid
        if data is not None:
            path_params["data"] = data
        path_rendered = "/cobr/{txid}/retentativa/{data}".format(**path_params)
        response = requests.post(
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
    ):
        """
                Endpoint para consultar cobranças com vencimento através de parâmetros como início, fim, cpf, cnpj e status.
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Data inicial da pesquisa. Intervalo máximo: 5 dias.
                    @param fim: Data final da pesquisa. Intervalo máximo: 5 dias.
                    @param cpf: cpf
                    @param cnpj: cnpj
                    @param location_presente: locationPresente
                    @param status: status
                    @param lote_cob_v_id: loteCobVId
                    @param paginacao_pagina_atual: paginacao.paginaAtual
                    @param paginacao_itens_por_pagina: paginacao.itensPorPagina
        """
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
        path_params = {}
        path_rendered = "/cobv".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pix_bb_devolucoes(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        estado_devolucao: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                Consulta Pix recebidos com devolução. O parâmetro data início/fim da pesquisa considera a data da devolução.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Data inicial utilizada na consulta. Respeita RFC 3339.
                    @param fim: Data de fim utilizada na consulta. Respeita RFC 3339.
                    @param estado_devolucao: Estado da devolução.
                    @param paginacao_pagina_atual: paginacao.paginaAtual
                    @param paginacao_itens_por_pagina: paginacao.itensPorPagina
        """
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if estado_devolucao is not None:
            query["estadoDevolucao"] = estado_devolucao
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        path_params = {}
        path_rendered = "/pix-bb/devolucoes".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_cobr(self, *, body: dict = None):
        """
                Endpoint para criar uma cobrança recorrente, neste caso, o txid deve ser definido pelo PSP.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/CobROperacaoInvalida",
          "title": "Operação inválida.",
          "status": 400,
          "detail": "A cobrança não respeita o schema.",
          "violacoes": [
            {
              "razao": "O objeto cobr.calendario não respeita o schema.",
              "propriedade": "cobr.calendario"
            }
          ]
        }
        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/cobr".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cobr(
        self,
        *,
        inicio: str = None,
        fim: str = None,
        id_rec: Optional[str] = None,
        cpf: Optional[str] = None,
        cnpj: Optional[str] = None,
        status: Optional[str] = None,
        convenio: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                Endpoint para consultar cobranças recorrentes através de parâmetros como início, fim, idRec, cpf, cnpj e status.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }

                Args:
                    @param inicio: Data de início - Filtra os registros cuja data de criação seja maior ou igual que a data de início. Respeita RFC 3339.
                    @param fim: Data de fim - Filtra os registros cuja data de criação seja menor ou igual que a data de fim. Respeita RFC 3339.
                    @param id_rec: ID Recorrência - Filtro pelo Identificador da Recorrência.
                    @param cpf: CPF - Filtro pelo CPF do devedor. Não pode ser utilizado ao mesmo tempo que o CNPJ.
                    @param cnpj: CNPJ - Filtro pelo CNPJ do devedor. Não pode ser utilizado ao mesmo tempo que o CPF.
                    @param status: Status do registro da cobrança.
                    @param convenio: Campo opcional para o caso de mais de um convênio dentro de um mesmo PSP recebedor, por CNPJ
                    @param paginacao_pagina_atual: Página atual - Página a ser retornada pela consulta. Se não for informada, o PSP assumirá que será 0.
        Default: 0
                    @param paginacao_itens_por_pagina: Itens por Página - Quantidade máxima de registros retornados em cada página. Apenas a última página pode conter uma quantidade menor de registros.
        Default: 100
        """
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if id_rec is not None:
            query["idRec"] = id_rec
        if cpf is not None:
            query["cpf"] = cpf
        if cnpj is not None:
            query["cnpj"] = cnpj
        if status is not None:
            query["status"] = status
        if convenio is not None:
            query["convenio"] = convenio
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        path_params = {}
        path_rendered = "/cobr".format(**path_params)
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
        inicio: str = None,
        fim: str = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                Endpoint para consultar lista de lotes de cobranças com vencimento.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Data de início - Filtra os registros cuja data de criação seja maior ou igual que a data de início. Respeita RFC 3339.
                    @param fim: Data de fim - Filtra os registros cuja data de criação seja menor ou igual que a data de fim. Respeita RFC 3339.
                    @param paginacao_pagina_atual: Página atual - Página a ser retornada pela consulta. Se não for informada, o PSP assumirá que será 0.
        Default: 0
                    @param paginacao_itens_por_pagina: Itens por Página - Quantidade máxima de registros retornados em cada página. Apenas a última página pode conter uma quantidade menor de registros.
        Default: 100
        """
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
        path_params = {}
        path_rendered = "/lotecobv".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_cob(self, *, body: dict = None):
        """
                Endpoint para criar uma cobrança imediata, neste caso, o txid deve ser definido pelo PSP.
        <br><br>**Responses**<br>
        <br>
        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/CobOperacaoInvalida",
          "title": "Cobrança inválida.",
          "status": 400,
          "detail": "A requisição que busca alterar ou criar uma cobrança para pagamento imediato não respeita o _schema_ ou está semanticamente errada.",
          "violacoes": [
            {}
          ]
        }
        ```
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param body: No description provided.
        """
        query = {}
        headers = {}
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
    ):
        """
                Endpoint para consultar cobranças imediatas através de parâmetros como início, fim, cpf, cnpj e status.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Data inicial da pesquisa. Intervalo máximo: 5 dias
                    @param fim: Data final da pesquisa. Intervalo máximo: 5 dias.
                    @param cpf: cpf
                    @param cnpj: cnpj
                    @param location_presente: locationPresente
                    @param status: status
                    @param paginacao_pagina_atual: paginacao.paginaAtual
                    @param paginacao_itens_por_pagina: paginacao.itensPorPagina
        """
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
        path_params = {}
        path_rendered = "/cob".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_locrec_by_id(self, *, id: str = None):
        """
                Endpoint utilizado para recuperar location do payload.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id: Id da location cadastrada para servir um payload
        """
        query = {}
        headers = {}
        path_params = {}
        if id is not None:
            path_params["id"] = id
        path_rendered = "/locrec/{id}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_pix_by_e2eid(self, *, e2eid: str = None):
        """
                Endpoint para consultar um Pix através de um e2eid
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param e2eid: e2eid
        """
        query = {}
        headers = {}
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

    def patch_solicrec_by_id_solic_rec(
        self, *, id_solic_rec: str = None, body: dict = None
    ):
        """
                Endpoint utilizado para revisar solicitação de confirmação de recorrência.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://pix.bcb.gov.br/api/v2/error/SolicRecOperacaoInvalida",
          "title": "Operação inválida.",
          "status": 400,
          "detail": "Não é possível cancelar uma solicitação de recorrência com o status diferente de CRIADA ou RECEBIDA."
        }

        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id_solic_rec: "string (ID Solicitação da Recorrência) 29 characters [a-zA-Z0-9]{29}
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        if id_solic_rec is not None:
            path_params["idSolicRec"] = id_solic_rec
        path_rendered = "/solicrec/{idSolicRec}".format(**path_params)
        response = requests.patch(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_solicrec_by_id_solic_rec(self, *, id_solic_rec: str = None):
        """
                Endpoint utilizado para consultar solicitação de confirmação de recorrência.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param id_solic_rec: ID Solicitação da Recorrência - Identificador da Solicitação da Recorrência
        """
        query = {}
        headers = {}
        path_params = {}
        if id_solic_rec is not None:
            path_params["idSolicRec"] = id_solic_rec
        path_rendered = "/solicrec/{idSolicRec}".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_webhookrec(self):
        """
                Endpoint para recuperação de informações sobre o Webhook.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/webhookrec".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_webhookrec(self):
        """
                Endpoint para cancelamento do webhook. Não é a única forma pela qual um webhook pode ser removido.
        <br><br>**Responses**<br>
        <br>

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```

        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/webhookrec".format(**path_params)
        response = requests.delete(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_webhookrec(self, *, body: dict = None):
        """
                Endpoint para configuração do serviço de notificações acerca de recorrências. Somente recorrências associadas a chave e conta serão notificadas.
        <br><br>**Responses**<br>
        <br>

        **400**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/WebhookOperacaoInvalida",
          "title": "Webhook inválido.",
          "status": 400,
          "detail": "A presente requisição busca criar um webhook sem respeitar o _schema_ ou, ainda, com sentido semanticamente inválido."
        }
        ```

        **403**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
          "title": "Acesso Negado",
          "status": 403,
          "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```

        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada."
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
          "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
          "title": "Serviço Indisponível",
          "status": 503,
          "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param body: No description provided.
        """
        query = {}
        headers = {}
        path_params = {}
        path_rendered = "/webhookrec".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_pix_bb(
        self,
        *,
        inicio: Optional[str] = None,
        fim: Optional[str] = None,
        txid: Optional[str] = None,
        tx_id_presente: Optional[bool] = None,
        devolucao_presente: Optional[bool] = None,
        contestacao_presente: Optional[bool] = None,
        cpf: Optional[str] = None,
        cnpj: Optional[str] = None,
        chave: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
    ):
        """
                Consulta Pix recebidos, incluindo filtro por chave e filtro por existência de contestação.
        <br><br>**Responses**<br>
        <br>
        **403**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/AcessoNegado",
            "title": "Acesso Negado",
            "status": 403,
            "detail": "Requisição de participante autenticado que viola alguma regra de autorização."
        }
        ```
        **404**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/NaoEncontrado",
            "title": "Não Encontrado",
            "status": 404,
            "detail": "Entidade não encontrada.",
            "correlationId": "API-BB-3x3mpl01-3b3f-4997-8c8b-477c368a8bc9",
            "numeroOcorrencia": 0
        }
        ```
        **503**<br>
        ```
        {
            "type": "https://api.bb.com.br/api/v2/error/ServicoIndisponivel",
            "title": "Serviço Indisponível",
            "status": 503,
            "detail": "Serviço não está disponível no momento. Serviço solicitado pode estar em manutenção ou fora da janela de funcionamento."
        }
        ```

                Args:
                    @param inicio: Data inicial utilizada na consulta. Respeita RFC 3339.
                    @param fim: Data de fim utilizada na consulta. Respeita RFC 3339.
                    @param txid: txid
                    @param tx_id_presente: txIdPresente
                    @param devolucao_presente: Filtro pela existência de devolução.
                    @param contestacao_presente: Indicador do filtro por existência de contestação.
                    @param cpf: CPF do usuário.
                    @param cnpj: CNPJ do usuário.
                    @param chave: **Chave DICT do recebedor**

        Formato do campo chave
        - Os tipos de chave podem ser: telefone, e-mail, cpf/cnpj ou EVP.
        - O formato das chaves pode ser encontrado na seção "Formatação das chaves do DICT no BR Code" do Manual de Padrões para iniciação do Pix.
                    @param paginacao_pagina_atual: paginacao.paginaAtual
                    @param paginacao_itens_por_pagina: paginacao.itensPorPagina
        """
        query = {}
        if inicio is not None:
            query["inicio"] = inicio
        if fim is not None:
            query["fim"] = fim
        if txid is not None:
            query["txid"] = txid
        if tx_id_presente is not None:
            query["txIdPresente"] = tx_id_presente
        if devolucao_presente is not None:
            query["devolucaoPresente"] = devolucao_presente
        if contestacao_presente is not None:
            query["contestacaoPresente"] = contestacao_presente
        if cpf is not None:
            query["cpf"] = cpf
        if cnpj is not None:
            query["cnpj"] = cnpj
        if chave is not None:
            query["chave"] = chave
        if paginacao_pagina_atual is not None:
            query["paginacao.paginaAtual"] = paginacao_pagina_atual
        if paginacao_itens_por_pagina is not None:
            query["paginacao.itensPorPagina"] = paginacao_itens_por_pagina
        headers = {}
        path_params = {}
        path_rendered = "/pix-bb".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
