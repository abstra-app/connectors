"""
Seguro Crédito Protegido API v1.0.0

"""

import requests


class SeguroCreditoProtegidoClient:
    base_url: str

    def __init__(
        self,
        base_url: str,
    ):
        self.base_url = base_url.rstrip("/")

    def post_acessos_token(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization: str = None,
        body: dict = None,
    ):
        """
                Realiza a geração do token de acesso da BB corretora, para garantir o devido
        acesso aos serviços do portal do desenvolvedor.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization is not None:
            headers["Authorization"] = authorization
        path_params = {}
        path_rendered = "/acessos/token".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_cotacoes_emissao(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
        <br/> <b>BRASIL_SEG -> /emissao/cotacao/v1</b> <br/> <br/> Para iniciar o fluxo de contratação da cotação é necessário informar obrigatóriamente o canal, meio canal, ponto de venda e o grupo de produto, e caso já possua os dados do proponente e ou número da oferta já pode informar nos repectivos campos, conforme exemplo. <br/> <br/> <i>Caso o número da oferta for informado nessa etapa, a etapa de selecionar a oferta não é necessária.</i> <br/>

        Args:
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
            @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
            @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
            @param coligada: No description provided.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/emissao".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_cotacoes_oferta(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
        <br/> <b>BRASIL_SEG -> /emissao/cotacao/v0/oferta</b> <br/> <br/> Registra qual foi a oferta selecionada para a cotação. <br/>

        Args:
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
            @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
            @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
            @param coligada: No description provided.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/oferta".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_cotacoes_proponente(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/v0/proponente</b>
        <br/>
        <br/>
         Grava o proponente na cotação.
         <br/>
        <br/>
        <b> Para testar a inclusão é necessário alterar os dados do proponente na requisição de exemplo.</b>

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/proponente".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def put_cotacoes_proponente(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/v0/proponente</b>
        <br/>
        <br/>
         Atualiza o proponente na cotação.
        <br />

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/proponente".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def delete_cotacoes_proponente(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
        <br/> <b>BRASIL_SEG -> /emissao/cotacao/v0/proponente</b> <br/> <br/> Realiza a Exclusão do proponente da cotação.

        Args:
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
            @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
            @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
            @param coligada: No description provided.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/proponente".format(**path_params)
        response = requests.delete(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_cotacoes_objeto_segurado(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/v0/objetosegurado</b>
        <br/>
        <br/>
         Grava um objeto segurado de acordo com as resposta do questionário.
        <br/>
        <br/>
        <i>Para obter o questionário que deve ser respondido, é necessário buscar no response do último serviço executado, seguindo as etapas abaixo:
        <br />
        <i> 1 - Localizar na lista de oferta a oferta selecionada.
        <br />
        <i> 2 - A partir da estrutura json da oferta selecionada, é necessário localizar a lista de chassi e varrer cada item da lista
        <br />
        <i> 3 - A partir da estrutura json do item da lista de chassi, é só localizar a lista de questionário
        <br />
        <br />
        <i> Para obter o identificador do chassi<b>(nmIdentificadorChassi)</b> é só recuperar da raiz do item da lista de chassi<b>(lsChassi)</b>.
        <br />
        <br />
        <i> Para obter número do tipo do objeto segurado<b>(nrTipoObjetoSegurado)</b> é só recuperar da raiz do item da lista de questionário que vai ser respondido.
        <br />
        <br />
        <i> Para preencher a propriedade <b>objeto</b> do response é necessário identificar a propriedade <b>nmPropriedade</b> de cada pergunta do questionário e adicionar a chave de resposta, conforme exemplo da requisição abaixo.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/objeto-segurado".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def put_cotacoes_objeto_segurado(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: str = None,
    ):
        """
        <br/> <b>BRASIL_SEG -> /emissao/cotacao/v0/objetosegurado</b> <br/> <br/> Altera um objeto segurado de acordo com as resposta do questionário. <br/> <br/> <i>Para obter o questionário que deve ser respondido, é necessário buscar no response do último serviço executado, seguindo as etapas abaixo: <br /> <i> 1 - Localizar na lista de oferta a oferta selecionada. <br /> <i> 2 - A partir da estrutura json da oferta selecionada, é necessário localizar a lista de chassi e varrer cada item da lista <br /> <i> 3 - A partir da estrutura json do item da lista de chassi, é só localizar a lista de questionário <br /> <br /> <i> Para obter o <b>identificador do chassi(nmIdentificadorchassi)</b> é só recuperar da raiz do item da lista de chassi(lsChassi). <br /> <br /> <i> Para obter o <b>identificador do objeto segurado(nmIdentificadorObjetoSegurado)</b> é necessário localizar na lista de objeto segurado(lsObjetoSegurado). <br /> <br /> <i> Para obter <b>número do tipo do objeto segurado(nrTipoObjetoSegurado)</b> é só recuperar da raiz do item da lista de questionário que vai ser respondido. <br /> <br /> <i> Para preencher a propriedade <b>objeto</b> do response é necessário identificar a propriedade <b>nmPropriedade</b> de cada pergunta do questionário e adicionar a chave de resposta, conforme exemplo da requisição abaixo.</i> <br /> <br /> <b> É necessário enviar todas as propriedades geradas para o campo 'objeto' novamente, alterando somente os valores de respostas necessários

        Args:
            @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
            @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
            @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
            @param coligada: No description provided.
            @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/objeto-segurado".format(**path_params)
        response = requests.put(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_cotacoes_plano(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/v1/plano</b>
        <br/>
        <br/>
        Registra qual foi o plano selecionado para cada tipo de objeto segurado.
        <br/>
        <b> *O plano deve ser selecionado de acordo com o objeto segurado que foi cotado<b/>
        <br/>
        <br/>
        <i> Para obter número do tipo do objeto segurado<b>(nrTipoObjetoSegurado)</b> é só recuperar da raiz do item da lista de questionário que vai ser respondido.
        <br />
        <br />
        <i>Para o campo identificador do plano<b>(nmIdentificadorPlano)</b>, busque a oferta selecionada na lista de oferta<b>(lsOferta)</b> da cotação, depois busque na raiz do item da oferta selecionado a lista de plano<b>(lsPlano)</b>.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/plano".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_cotacoes_periodicidade(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/v1/periodicidade</b>
        <br/>
        <br/>
        Serviço para registrar qual é a periodicidade de contratação do seguro, ou seja, por quanto tempo aquele seguro estará vigente para o segurado.
        <br />
        <br />
        <i>Para o campo quantidade da periodicidade<b>(qtPeriodicidade)</b> será aceito somente valores que estiver configurado no chassi<b>(lsChassi)</b> da oferta<b>(lsOferta)</b> selecionado.
        <br />
        <br />
        <i>Para o campo identificador da periodicidade<b>(nmIdentificadorPeriodicidade)</b>, busque a oferta selecionada na lista de oferta<b>(lsOferta)</b> da cotação, depois busque na raiz do item da oferta selecionado a lista de chassi<b>(lsChassi)</b> pegue o item do index zero, na raiz do item do chassi busque pela chave <b>periodicidadeContratacao</b>.
        <br />
        <br />
        <i> Para obter o identificador do chassi<b>(nmIdentificadorChassi)</b> é só recuperar da raiz do item da lista de chassi<b>(lsChassi)</b>.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/cotacoes/periodicidade".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_contratacoes_plano_pagamento(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/v0/planopagamento</b>
        <br/>
        <br/>
        Registra qual foi o plano de pagamento selecionado para a cotação.
        <br />
        <br />
        <i>Para o campo identificador do plano de pagamento<b>(nmIdentificadorPlanoPagamento)</b>, busque a oferta selecionada na lista de oferta<b>(lsOferta)</b> da cotação, depois busque na raiz do item da oferta selecionado a lista de plano de pagamento<b>(lsPlanoPagamento)</b>

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/contratacoes/plano-pagamento".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_contratacoes_plano_pagamento_parcelamento(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/planopagamento/parcelamento</b>
        <br/>
        <br/>
        Seleciona um parcelamento disponível para o plano de pagamento escolhido.
        <br />
        <br />
        <i>Para o campo identificador da parcela<b>(nmIdentificadorParcela)</b>, busque a oferta selecionada na lista de oferta<b>(lsOferta)</b> da cotação, depois busque na raiz do item da oferta selecionado a lista de plano de pagamento<b>(lsPlanoPagamento)</b> e busque pelo plano de pagamento selecionado, com item do plano de pagamento selecionado busque na raiz a lista de parcelas<b>(lsParcela)</b>.
        <br />
        <br />
        <i> A lista de parcelas<b>(lsParcela)</b> só é gerada após a seleção do plano de pagamento

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/contratacoes/plano-pagamento/parcelamento".format(
            **path_params
        )
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def post_contratacoes_de_acordo(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/v0/deacordo</b>
        <br/>
        <br/>
        Registra na cotação o 'de acordo' do cliente titular.

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/contratacoes/de-acordo".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_contratacoes_bandeira_cartao(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /financeiro/dadobasico/bandeiraCartao</b>
        <br/>
        <br/>
        Lista as bandeirdas de cartões com seus respectivos códigos.
        <br />

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/contratacoes/bandeira-cartao".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def post_contratacoes_contrato_cobranca(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        body: dict = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/v0/contrato-cobranca</b>
        <br/>
        <br/>
        Efetiva a cobrança da cotação.
        <br />
        <br />
        <i> A chave <b>dadoCartaoCredito</b> deve ser preenchida de acordo com o plano de pagamento escolhido.
        <br/>
        <b> *A opção de débito em conta não está habilitada</b>

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param body: No description provided.
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        path_rendered = "/contratacoes/contrato-cobranca".format(**path_params)
        response = requests.post(
            self.base_url + path_rendered, params=query, headers=headers, json=body
        )
        response.raise_for_status()
        return response.json()

    def get_consultas_pdf_proposta(
        self,
        *,
        gw_dev_app_key: str = None,
        authorization_seg: str = None,
        authorization: str = None,
        coligada: str = None,
        nm_identificador_pdf: str = None,
    ):
        """
                <br/>
        <b>BRASIL_SEG -> /emissao/cotacao/pdf/{nmIdentificadorPdf}</b>
        <br/>
        <br/>
        Lista as bandeirdas de cartões com seus respectivos códigos.
        <br />

                Args:
                    @param gw_dev_app_key: É a chave de acesso do aplicativo do desenvolvedor obtida no Portal do Desenvolvedor, Essa chave será usada para identificação do aplicativo.
                    @param authorization_seg:  Token" de acesso fornecido pelo bbs-credentials. Ex: Bearer [ACCESS_TOKEN]
                    @param authorization: Token" de acesso fornecido pelo OAuth 2.0. Ex: Bearer [ACCESS_TOKEN]
                    @param coligada: No description provided.
                    @param nm_identificador_pdf: Identificador da proposta informado no serviço de cobrar e contratar
        """
        query = {}
        if gw_dev_app_key is not None:
            query["gw-dev-app-key"] = gw_dev_app_key
        headers = {}
        if authorization_seg is not None:
            headers["Authorization_seg"] = authorization_seg
        if authorization is not None:
            headers["Authorization"] = authorization
        if coligada is not None:
            headers["coligada"] = coligada
        path_params = {}
        if nm_identificador_pdf is not None:
            path_params["nmIdentificadorPdf"] = nm_identificador_pdf
        path_rendered = "/consultas/pdf-proposta".format(**path_params)
        response = requests.get(
            self.base_url + path_rendered,
            params=query,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
