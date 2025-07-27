"""
API Pixautomatico v1.40.0
A API Pix Automático padroniza serviços oferecidos pelo PSP recebedor no contexto do arranjo Pix Automático, direcionando:
- o gerenciamentos de cobranças com recorrências, em lotes ou não;
- as consultas.
"""

import requests
from typing import Optional


class PixautomaticoV1Client:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def post_locrec(self, *, content_type: str = None, x_itau_apikey: str = None):
        """
        Criar location do payload

        Args:
            @param content_type: Tipo de conteúdo
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Content-Type": content_type,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/locrec".format(**path_params)
        response = requests.post(
            path_rendered,
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
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
        Endpoint para consultar locations cadastradas

        Args:
            @param inicio: No description provided.
            @param fim: No description provided.
            @param id_rec_presente: No description provided.
            @param convenio: No description provided.
            @param paginacao_pagina_atual: No description provided.
            @param paginacao_itens_por_pagina: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "inicio": inicio,
            "fim": fim,
            "idRecPresente": id_rec_presente,
            "convenio": convenio,
            "paginacao.paginaAtual": paginacao_pagina_atual,
            "paginacao.itensPorPagina": paginacao_itens_por_pagina,
        }
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/locrec".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_locrec_by_id(
        self,
        *,
        id: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
        Recupera a location do payload

        Args:
            @param id: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "id": id,
        }
        path_rendered = "/locrec/{id}".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_locrec_by_id_id_rec(self, *, id: str = None, x_itau_apikey: str = None):
        """
        Endpoint utilizado para desvincular uma recorrência de uma location.

        Args:
            @param id: No description provided.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "id": id,
        }
        path_rendered = "/locrec/{id}/idRec".format(**path_params)
        response = requests.delete(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_token_rec_by_rec_url_access_token(
        self,
        *,
        rec_url_access_token: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
                ## Endpoint (location) que serve um payload que representa uma recorrência.

        No momento em que o usuário pagador efetua a leitura de um QR Code composto gerado pelo recebedor, esta URL será acessada e seu conteúdo consiste em uma estrutura JWS.
        As informações sobre a segurança no acesso às urls encontram-se no Manual de Segurança do Pix disponível nesse __[link](https://www.bcb.gov.br/estabilidadefinanceira/comunicacaodados)__.

                Args:
                    @param rec_url_access_token: No description provided.
                    @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
                    @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
                    @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "rec_url_access_token": rec_url_access_token,
        }
        path_rendered = "/token/rec/{recUrlAccessToken}".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_webhookrec(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
                Endpoint opcional para configuração do serviço de notificações acerca de recorrências. Somente recorrências associadas ao usuário recebedor serão notificadas
        Para que o usuário recebedor possa receber notificações acerca do status de uma cobrança, é necessário que o usuário recebedor crie e proveja sua própria API de recebimento de notificações, de acordo com as especificações do Bacen e conforme a aba "Callback" abaixo, para acionamento.
        Este endpoint, PUT /webhookcobr, deve ser chamado para cadastrar a URL completa da API do usuário recebedor nos nossos sistemas. O cadastro pode ser feito em qualquer momento após o onboarding, mas o usuário recebedor só passa a receber as notificações das cobranças correntes após o cadastro com este endpoint.

        Pré-requisitos:
        É necessário que o usuário recebedor tenha feito o processo de onboarding e ativado o produto Pix Automático.

        Quanto ao disparo de notificações:
        Os sistemas do Itaú se comunicam com a API cadastrada neste endpoint pelo usuário recebedor, na ocorrência de notificação, via mTLS. O Itaú faz o papel do cliente, enquanto a API parceira faz o papel de servidor nessa conexão.
        C.A do Servidor Cliente (Itaú): Para fluxo mTLS, o Itaú utiliza sua própria Chave Pública (CA). Portanto, para que o servidor do parceiro valide a autenticidade da chamada recebida pelo Itaú em sua URL de webhook, é necessário realizar o trust da CA do Itaú. Mais informações e a CA do Itaú para download podem ser encontradas neste link (https://devportal.itau.com.br/autenticacao-documentacao), em "Fluxos de autenticação Webhook".
        C.A do Servidor do Webhook (API do parceiro): Para que o Itaú consiga estabelecer comunicação TLS/SSL na chamada do webhook, é necessário que o parceiro verifique se a CA usada pelo servidor de domínios consta na seguinte relação:
        - Amazon
        - DigiCert
        - GlobalSign
        - Comodo
        - Entrust
        - GeoTrust
        - Thawte
        - VeriSign
        - GoDaddy
        Caso a CA não esteja na relação acima, o parceiro deve entrar em contato com o time de implantação técnica do Itaú para habilitação da CA na plataforma.

                Args:
                    @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
                    @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
                    @param x_itau_apikey: UUID que identifica a o clientID da chamada
                    @param content_type: Tipo de conteúdo
                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {}
        path_rendered = "/webhookrec".format(**path_params)
        response = requests.put(path_rendered, params=query, headers=headers, json=body)
        response.raise_for_status()
        return response.json()

    def get_webhookrec(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
                Endpoint para cancelamento do webhook.
        Caso o parceiro queira parar de receber notificações sobre recorrência, pode utilizar este endpoint. O parceiro pode reativar o recebimento de notificações a qualquer momento por meio do enpoint PUT.

                Args:
                    @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
                    @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
                    @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/webhookrec".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_webhookrec(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
                Endpoint para cancelamento do webhook.
        Caso o parceiro queira parar de receber notificações sobre recorrência, pode utilizar este endpoint. O parceiro pode reativar o recebimento de notificações a qualquer momento por meio do enpoint PUT.

                Args:
                    @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
                    @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
                    @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/webhookrec".format(**path_params)
        response = requests.delete(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def put_webhookcobr(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
                Endpoint opcional para configuração do serviço de notificações acerca de recorrências. Somente recorrências associadas ao usuário recebedor serão notificadas
        Para que o usuário recebedor possa receber notificações acerca do status de uma cobrança, é necessário que o usuário recebedor crie e proveja sua própria API de recebimento de notificações, de acordo com as especificações do Bacen e conforme a aba "Callback" abaixo, para acionamento.
        Este endpoint, PUT /webhookcobr, deve ser chamado para cadastrar a URL completa da API do usuário recebedor nos nossos sistemas. O cadastro pode ser feito em qualquer momento após o onboarding, mas o usuário recebedor só passa a receber as notificações das cobranças correntes após o cadastro com este endpoint.

        Pré-requisitos:
        É necessário que o usuário recebedor tenha feito o processo de onboarding e ativado o produto Pix Automático.

        Quanto ao disparo de notificações:
        Os sistemas do Itaú se comunicam com a API cadastrada neste endpoint pelo usuário recebedor, na ocorrência de notificação, via mTLS. O Itaú faz o papel do cliente, enquanto a API parceira faz o papel de servidor nessa conexão.
        C.A do Servidor Cliente (Itaú): Para fluxo mTLS, o Itaú utiliza sua própria Chave Pública (CA). Portanto, para que o servidor do parceiro valide a autenticidade da chamada recebida pelo Itaú em sua URL de webhook, é necessário realizar o trust da CA do Itaú. Mais informações e a CA do Itaú para download podem ser encontradas neste link (https://devportal.itau.com.br/autenticacao-documentacao), em "Fluxos de autenticação Webhook".
        C.A do Servidor do Webhook (API do parceiro): Para que o Itaú consiga estabelecer comunicação TLS/SSL na chamada do webhook, é necessário que o parceiro verifique se a CA usada pelo servidor de domínios consta na seguinte relação:
        - Amazon
        - DigiCert
        - GlobalSign
        - Comodo
        - Entrust
        - GeoTrust
        - Thawte
        - VeriSign
        - GoDaddy
        Caso a CA não esteja na relação acima, o parceiro deve entrar em contato com o time de implantação técnica do Itaú para habilitação da CA na plataforma.

                Args:
                    @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
                    @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
                    @param x_itau_apikey: UUID que identifica a o clientID da chamada
                    @param content_type: Tipo de conteúdo
                    @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {}
        path_rendered = "/webhookcobr".format(**path_params)
        response = requests.put(path_rendered, params=query, headers=headers, json=body)
        response.raise_for_status()
        return response.json()

    def get_webhookcobr(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
                Endpoint para recuperação de informações sobre o Webhook.
        Neste endpoint, obtenha informações sobre qual URL foi cadastrada pelo parceiro para recebimento de notificações e data de criação.

                Args:
                    @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
                    @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
                    @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/webhookcobr".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def delete_webhookcobr(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
        Endpoint para cancelamento do webhook. Não é a única forma pela qual um webhook pode ser removido.

        Args:
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/webhookcobr".format(**path_params)
        response = requests.delete(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get_rec_by_id_rec(
        self,
        *,
        id_rec: str = None,
        txid: Optional[str] = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
        Consultar recorrência.

        Args:
            @param id_rec: No description provided.
            @param txid: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "txid": txid,
        }
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "id_rec": id_rec,
        }
        path_rendered = "/rec/{idRec}".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_rec_by_id_rec(
        self,
        *,
        id_rec: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
        Revisar recorrência.

        Args:
            @param id_rec: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
            @param content_type: Tipo de conteúdo
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {
            "id_rec": id_rec,
        }
        path_rendered = "/rec/{idRec}".format(**path_params)
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
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
        convenio: Optional[str] = None,
        location_presente: Optional[bool] = None,
        status: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
        Consultar lista de recorrências.

        Args:
            @param inicio: No description provided.
            @param fim: No description provided.
            @param cpf: No description provided.
            @param cnpj: No description provided.
            @param convenio: No description provided.
            @param location_presente: No description provided.
            @param status: No description provided.
            @param paginacao_pagina_atual: No description provided.
            @param paginacao_itens_por_pagina: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "inicio": inicio,
            "fim": fim,
            "cpf": cpf,
            "cnpj": cnpj,
            "convenio": convenio,
            "locationPresente": location_presente,
            "status": status,
            "paginacao.paginaAtual": paginacao_pagina_atual,
            "paginacao.itensPorPagina": paginacao_itens_por_pagina,
        }
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/rec".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_rec(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
        Criar recorrência

        Args:
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
            @param content_type: Tipo de conteúdo
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {}
        path_rendered = "/rec".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_solicrec(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
        Criar solicitação de confirmação de recorrência.

        Args:
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
            @param content_type: Tipo de conteúdo
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {}
        path_rendered = "/solicrec".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_solicrec_by_id_solic_rec(
        self,
        *,
        id_solic_rec: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
        Consultar solicitação.

        Args:
            @param id_solic_rec: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "id_solic_rec": id_solic_rec,
        }
        path_rendered = "/solicrec/{idSolicRec}".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def patch_solicrec_by_id_solic_rec(
        self,
        *,
        id_solic_rec: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
        Revisar solicitação de confirmação de recorrência.

        Args:
            @param id_solic_rec: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
            @param content_type: Tipo de conteúdo
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {
            "id_solic_rec": id_solic_rec,
        }
        path_rendered = "/solicrec/{idSolicRec}".format(**path_params)
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def put_cobr_by_txid(
        self,
        *,
        txid: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
        Endpoint para criar uma cobrança recorrente.

        Args:
            @param txid: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
            @param content_type: Tipo de conteúdo
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {
            "txid": txid,
        }
        path_rendered = "/cobr/{txid}".format(**path_params)
        response = requests.put(path_rendered, params=query, headers=headers, json=body)
        response.raise_for_status()
        return response.json()

    def patch_cobr_by_txid(
        self,
        *,
        txid: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
        Endpoint para revisar uma cobrança recorrente.

        Args:
            @param txid: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
            @param content_type: Tipo de conteúdo
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {
            "txid": txid,
        }
        path_rendered = "/cobr/{txid}".format(**path_params)
        response = requests.patch(
            path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_cobr_by_txid(
        self,
        *,
        txid: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
        Endpoint para consultar uma cobrança recorrente através de um determinado txid.

        Args:
            @param txid: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {
            "txid": txid,
        }
        path_rendered = "/cobr/{txid}".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_cobr(
        self,
        *,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
        body: dict = None,
    ):
        """
        Endpoint para criar uma cobrança recorrente, neste caso, o txid deve ser definido pelo PSP.

        Args:
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
            @param content_type: Tipo de conteúdo
            @param body: No description provided.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {}
        path_rendered = "/cobr".format(**path_params)
        response = requests.post(
            path_rendered, params=query, headers=headers, json=body
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
        convenio: Optional[str] = None,
        paginacao_pagina_atual: Optional[int] = None,
        paginacao_itens_por_pagina: Optional[int] = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
    ):
        """
        Endpoint para consultar cobranças recorrentes através de parâmetros como início, fim, idRec, cpf, cnpj, status e convênio.

        Args:
            @param inicio: No description provided.
            @param fim: No description provided.
            @param id_rec: No description provided.
            @param cpf: No description provided.
            @param cnpj: No description provided.
            @param convenio: No description provided.
            @param paginacao_pagina_atual: No description provided.
            @param paginacao_itens_por_pagina: No description provided.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "inicio": inicio,
            "fim": fim,
            "idRec": id_rec,
            "cpf": cpf,
            "cnpj": cnpj,
            "convenio": convenio,
            "paginacao.paginaAtual": paginacao_pagina_atual,
            "paginacao.itensPorPagina": paginacao_itens_por_pagina,
        }
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
        }
        path_params = {}
        path_rendered = "/cobr".format(**path_params)
        response = requests.get(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_cobr_by_txid_retentativa_by_data(
        self,
        *,
        txid: str = None,
        data: str = None,
        authorization: str = None,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        content_type: str = None,
    ):
        """
        Endpoint para solicitar retentativa de uma cobrança recorrente.

        Args:
            @param txid: No description provided.
            @param data: Data prevista para liquidação da ordem de pagamento correspondente. Trata-se de uma data, no formato `YYYY-MM-DD`, segundo ISO 8601.
            @param authorization: Token de acesso a API. Obtido através do endpoint de autorização.
            @param x_itau_correlation_id: UUID que identifica a requisição, para propósitos de rastreamento.
            @param x_itau_apikey: UUID que identifica a o clientID da chamada
            @param content_type: Tipo de conteúdo
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {}
        headers = {
            "Authorization": authorization,
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "Content-Type": content_type,
        }
        path_params = {
            "txid": txid,
            "data": data,
        }
        path_rendered = "/cobr/{txid}/retentativa/{data}".format(**path_params)
        response = requests.post(
            path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
