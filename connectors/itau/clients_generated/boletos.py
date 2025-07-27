"""
API Boletos v0.0.1
API responsável pelo ciclo de vida de boletos. Podendo emitir novos boletos, fazer instruções em boletos existentes, consultar o detalhe do boleto, e também consultar a lista de boletos da cartira de cobrança de um beneficiário.
"""

import requests
from typing import Optional


class BoletosClient:
    base_url: str
    x_itau_apikey: str

    def __init__(self, base_url: str, x_itau_apikey: str):
        self.base_url = base_url.rstrip("/")
        self.x_itau_apikey = x_itau_apikey

    def get_boletos(
        self,
        *,
        x_itau_correlation_id: str = None,
        x_itau_apikey: str = None,
        x_itau_flowid: Optional[str] = None,
        authorization: str = None,
        content_type: Optional[str] = None,
        id_beneficiario: str = None,
        nome_pagador: Optional[str] = None,
        cpf_pagador: Optional[str] = None,
        cnpj_pagador: Optional[str] = None,
        seu_numero: Optional[str] = None,
        nosso_numero: Optional[str] = None,
        codigo_carteira: Optional[str] = None,
        codigo_barra: Optional[str] = None,
        situacao: Optional[str] = None,
        instrumento_cobranca: Optional[str] = None,
        situacao_protesto: Optional[str] = None,
        situacao_vencimento: Optional[str] = None,
        situacao_negativacao: Optional[str] = None,
        motivo_cancelamento: Optional[str] = None,
        data_entrada: Optional[str] = None,
        data_emissao: Optional[str] = None,
        data_cancelamento: Optional[str] = None,
        data_vencimento: Optional[str] = None,
        data_pagamento: Optional[str] = None,
        order_by: Optional[str] = None,
        order: Optional[str] = None,
        view: Optional[str] = None,
        indicador_descontado: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ):
        """
        Endpoint responsável por listar boletos baseado em alguns parâmetros, como data de pagamento ou emissão (entre outros) e id do beneficiário.

        Args:
            @param x_itau_correlation_id: UUID que identifica a transação.
            @param x_itau_apikey: Chave que identifica o chamador.
            @param x_itau_flowid: Chave que identifica o fluxo de negócio. Deve ser diferente do __x-itau-correlationid__.
            @param authorization: Bearer token para autorização do cliente na api
            @param content_type: Content type da aplicação (application/json)
            @param id_beneficiario: Id do beneficiário, composto de "${agencia}${conta}${dac}", sem traços ou pontos.
            @param nome_pagador: Nome do pagador do boleto.
            @param cpf_pagador: Cpf do pagador do boleto.
            @param cnpj_pagador: Cnpj do pagador do boleto.
            @param seu_numero: Seu número, identificador do boleto
            @param nosso_numero: Nosso número, identificador do boleto
            @param codigo_carteira: Codigo da carteira
            @param codigo_barra: Codigo de barras do boleto
            @param situacao: Status do boleto: aberto, emPagamento, pago ou cancelado
            @param instrumento_cobranca: Instrumento de cobrança: boleto ou bolecode
            @param situacao_protesto: Situação de protesto: emProtesto, protestado, protestoCancelado ou protestoAgendado
            @param situacao_vencimento: Status vencimento: aVencer ou vencido
            @param situacao_negativacao: Filtro por situação da negativação: emNegativacao, negativado, negativacaoCancelada ou negativacaoAgendada
            @param motivo_cancelamento: baixaSimples, baixaPorTerSidoLiquidado ou baixaPorTerSidoProtestado
            @param data_entrada: Período desejado para filtro de boletos pela data de entrada
            @param data_emissao: Período desejado para filtro de boletos pela data de emissão
            @param data_cancelamento: Período desejado para filtro de boletos pela data de cancelamento
            @param data_vencimento: Período desejado para filtro de boletos pela data de vencimento
            @param data_pagamento: Período desejado para filtro de boletos pela data de pagamento
            @param order_by: Os campos permitidos para ordenação são: nomePagador, nossoNumero, seuNumero, dataEmissao, dataVencimento, dataCancelamento, dataPagamento e valorBoleto.
            @param order: A ordem de classificação dos resultados. Os valores permitidos são: asc ou desc.
            @param view: Tipo de visão que deseja-se ter ao ler os dados
            @param indicador_descontado: Indicador de desconto (true - descontado, false - não descontado)
            @param page: Número da página que está sendo requisitada (o valor da primeira página é 0)
            @param page_size: Quantidade total de registros por páginas.
        """
        if x_itau_apikey is None:
            x_itau_apikey = self.x_itau_apikey
        query = {
            "idBeneficiario": id_beneficiario,
            "nomePagador": nome_pagador,
            "cpfPagador": cpf_pagador,
            "cnpjPagador": cnpj_pagador,
            "seuNumero": seu_numero,
            "nossoNumero": nosso_numero,
            "codigoCarteira": codigo_carteira,
            "codigoBarra": codigo_barra,
            "situacao": situacao,
            "instrumentoCobranca": instrumento_cobranca,
            "situacaoProtesto": situacao_protesto,
            "situacaoVencimento": situacao_vencimento,
            "situacaoNegativacao": situacao_negativacao,
            "motivoCancelamento": motivo_cancelamento,
            "dataEntrada": data_entrada,
            "dataEmissao": data_emissao,
            "dataCancelamento": data_cancelamento,
            "dataVencimento": data_vencimento,
            "dataPagamento": data_pagamento,
            "orderBy": order_by,
            "order": order,
            "view": view,
            "indicadorDescontado": indicador_descontado,
            "page": page,
            "pageSize": page_size,
        }
        headers = {
            "x-itau-correlationID": x_itau_correlation_id,
            "x-itau-apikey": x_itau_apikey,
            "x-itau-flowid": x_itau_flowid,
            "Authorization": authorization,
            "Content-type": content_type,
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
