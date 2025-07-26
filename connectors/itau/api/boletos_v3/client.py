
from ...utils.auth import Credentials
from typing import Optional, List, Any
from dataclasses import dataclass
import requests
import uuid
from datetime import date, datetime
from ...utils.currency import str_to_cents


# --- Data classes geradas a partir dos schemas OpenAPI ---

@dataclass
class SituacaoGeralBoleto:
    codigo: str
    descricao: str

@dataclass
class StatusBoletoCanal:
    codigo: str
    descricao: str

@dataclass
class StatusVencimento:
    codigo: str
    descricao: str

@dataclass
class Boleto:
    nome_pagador: Optional[str] = None
    numero_cpf_cnpj_pagador: Optional[str] = None
    tipo_boleto: Optional[str] = None
    numero_nosso_numero: Optional[str] = None
    dac_titulo: Optional[str] = None
    seu_numero: Optional[str] = None
    data_emissao: Optional[date] = None
    data_inclusao_boleto: Optional[date] = None
    data_vencimento: Optional[date] = None
    data_inclusao_pagamento: Optional[date] = None
    valor_titulo_cents: Optional[int] = None
    valor_pago_total_cents: Optional[int] = None
    situacao_geral_boleto: Optional[SituacaoGeralBoleto] = None
    status_vencimento: Optional[StatusVencimento] = None
    emitir_segunda_via: Optional[bool] = None
    codigo_carteira: Optional[str] = None
    status_boleto_canal: Optional[StatusBoletoCanal] = None

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de Boleto a partir de um dicionário.
        """
        return cls(
            nome_pagador=data.get("nome_pagador"),
            numero_cpf_cnpj_pagador=data.get("numero_cpf_cnpj_pagador"),
            tipo_boleto=data.get("tipo_boleto"),
            numero_nosso_numero=data.get("numero_nosso_numero"),
            dac_titulo=data.get("dac_titulo"),
            seu_numero=data.get("seu_numero"),
            data_emissao=date.fromisoformat(data["data_emissao"]) if data.get("data_emissao") else None,
            data_inclusao_boleto=date.fromisoformat(data["data_inclusao_boleto"]) if data.get("data_inclusao_boleto") else None,
            data_vencimento=date.fromisoformat(data["data_vencimento"]) if data.get("data_vencimento") else None,
            data_inclusao_pagamento=date.fromisoformat(data["data_inclusao_pagamento"]) if data.get("data_inclusao_pagamento") else None,
            valor_titulo_cents=str_to_cents(data["valor_titulo"]) if data.get("valor_titulo") else None,
            valor_pago_total_cents=str_to_cents(data["valor_pago_total"]) if data.get("valor_pago_total") else None,
            situacao_geral_boleto=SituacaoGeralBoleto(**data["situacao_geral_boleto"]) if data.get("situacao_geral_boleto") else None,
            status_vencimento=StatusVencimento(**data["status_vencimento"]) if data.get("status_vencimento") else None,
            emitir_segunda_via=data.get("emitir_segunda_via"),
            codigo_carteira=data.get("codigo_carteira"),
            status_boleto_canal=StatusBoletoCanal(**data["status_boleto_canal"]) if data.get("status_boleto_canal") else None,
        )

@dataclass
class NotificacaoBoleto:
    webhook_url: Optional[str] = None
    webhook_oauth_url: Optional[str] = None
    webhook_oauth_scope: Optional[str] = None
    valor_minimo_cents: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de NotificacaoBoleto a partir de um dicionário.
        """
        return cls(
            webhook_url=data.get("webhook_url"),
            webhook_oauth_url=data.get("webhook_oauth_url"),
            webhook_oauth_scope=data.get("webhook_oauth_scope"),
            valor_minimo_cents=str_to_cents(data["valor_minimo"]) if data.get("valor_minimo") else None,
        )

@dataclass
class NotificacaoBoletoPost:
    id_beneficiario: Optional[str] = None
    webhook_client_id: Optional[str] = None
    webhook_client_secret: Optional[str] = None
    tipos_notificacoes: Optional[List[str]] = None

@dataclass
class NotificacaoBoletoPatch:
    webhook_client_id: Optional[str] = None
    webhook_client_secret: Optional[str] = None
    webhook_url: Optional[str] = None
    webhook_oauth_url: Optional[str] = None
    webhook_oauth_scope: Optional[str] = None
    valor_minimo_cents: Optional[int] = None

@dataclass
class NotificacaoBoletoGet:
    id_beneficiario: Optional[str] = None

@dataclass
class Baixas:
    valor_cents: int
    quantidade: float

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de Baixas a partir de um dicionário.
        """
        return cls(
            valor_cents=str_to_cents(data["valor"]),
            quantidade=data["quantidade"]
        )

@dataclass
class Vencidos:
    data_inicial: Optional[date] = None
    data_final: date = date.today()
    valor_cents: int = 0
    quantidade: float = 0

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de Vencidos a partir de um dicionário.
        """
        return cls(
            data_inicial=date.fromisoformat(data["data_inicial"]) if data.get("data_inicial") else None,
            data_final=date.fromisoformat(data["data_final"]) if data.get("data_final") else date.today(),
            valor_cents=str_to_cents(data["valor"]) if data.get("valor") else 0,
            quantidade=data.get("quantidade", 0)
        )

@dataclass
class Posicao:
    data_posicao: date
    posicao_anterior: Optional[Baixas] = None
    entradas: Optional[Baixas] = None
    baixas: Optional[Baixas] = None
    baixas_desconto: Optional[Baixas] = None
    baixas_cobranca: Optional[Baixas] = None
    liquidacoes: Optional[Baixas] = None
    posicao_atual: Optional[Baixas] = None
    consolidado_vencer: Optional[List[Any]] = None  # array de datas/valores
    vencidos: Optional[Vencidos] = None

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de Posicao a partir de um dicionário.
        """
        return cls(
            data_posicao=date.fromisoformat(data["data_posicao"]),
            posicao_anterior=Baixas.from_dict(data["posicao_anterior"]) if data.get("posicao_anterior") else None,
            entradas=Baixas.from_dict(data["entradas"]) if data.get("entradas") else None,
            baixas=Baixas.from_dict(data["baixas"]) if data.get("baixas") else None,
            baixas_desconto=Baixas.from_dict(data["baixas_desconto"]) if data.get("baixas_desconto") else None,
            baixas_cobranca=Baixas.from_dict(data["baixas_cobranca"]) if data.get("baixas_cobranca") else None,
            liquidacoes=Baixas.from_dict(data["liquidacoes"]) if data.get("liquidacoes") else None,
            posicao_atual=Baixas.from_dict(data["posicao_atual"]) if data.get("posicao_atual") else None,
            consolidado_vencer=data.get("consolidado_vencer"),
            vencidos=Vencidos.from_dict(data["vencidos"]) if data.get("vencidos") else None,
        )

@dataclass
class MovimentacaoFinanceira:
    principal_liquidacoes_cents: int
    descontos_abatimentos_cents: int
    juros_multas_cents: int
    total_cents: int

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de MovimentacaoFinanceira a partir de um dicionário.
        """
        return cls(
            principal_liquidacoes_cents=str_to_cents(data["principal_liquidacoes"]),
            descontos_abatimentos_cents=str_to_cents(data["descontos_abatimentos"]),
            juros_multas_cents=str_to_cents(data["juros_multas"]),
            total_cents=str_to_cents(data["total"])
        )

@dataclass
class FrancesaResumidaMovimentacaoContaDeducao:
    descricao: str
    valor_cents: int

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de FrancesaResumidaMovimentacaoContaDeducao a partir de um dicionário.
        """
        return cls(
            descricao=data["descricao"],
            valor_cents=str_to_cents(data["valor"])
        )

@dataclass
class PeriodoConsolidado:
    data_inicial: date
    data_final: date

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de PeriodoConsolidado a partir de um dicionário.
        """
        return cls(
            data_inicial=date.fromisoformat(data["data_inicial"]),
            data_final=date.fromisoformat(data["data_final"])
        )

@dataclass
class TarifacaoMensalTarifas:
    descricao: str
    quantidade: int
    valor_cents: int

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de TarifacaoMensalTarifas a partir de um dicionário.
        """
        return cls(
            descricao=data["descricao"],
            quantidade=data["quantidade"],
            valor_cents=str_to_cents(data["valor"])
        )

@dataclass
class TotalTarifas:
    quantidade: float
    valor_cents: int

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de TotalTarifas a partir de um dicionário.
        """
        return cls(
            quantidade=data["quantidade"],
            valor_cents=str_to_cents(data["valor"])
        )

@dataclass
class TarifacaoMensal:
    data_debito: date
    periodo_consolidado: PeriodoConsolidado
    tarifas: List[TarifacaoMensalTarifas]
    total_tarifas: TotalTarifas

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de TarifacaoMensal a partir de um dicionário.
        """
        return cls(
            data_debito=date.fromisoformat(data["data_debito"]),
            periodo_consolidado=PeriodoConsolidado.from_dict(data["periodo_consolidado"]),
            tarifas=[TarifacaoMensalTarifas.from_dict(tarifa) for tarifa in data["tarifas"]],
            total_tarifas=TotalTarifas.from_dict(data["total_tarifas"])
        )

@dataclass
class MovimentacaoConta:
    valores_disponiveis_cents: int
    valores_a_compensar_cents: int
    valores_nao_liberados_cents: int
    valor_total_deducoes_cents: int
    deducoes: List[FrancesaResumidaMovimentacaoContaDeducao]
    tarifacao_mensal: Optional[TarifacaoMensal] = None

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de MovimentacaoConta a partir de um dicionário.
        """
        return cls(
            valores_disponiveis_cents=str_to_cents(data["valores_disponiveis"]),
            valores_a_compensar_cents=str_to_cents(data["valores_a_compensar"]),
            valores_nao_liberados_cents=str_to_cents(data["valores_nao_liberados"]),
            valor_total_deducoes_cents=str_to_cents(data["valor_total_deducoes"]),
            deducoes=[FrancesaResumidaMovimentacaoContaDeducao.from_dict(deducao) for deducao in data["deducoes"]],
            tarifacao_mensal=TarifacaoMensal.from_dict(data["tarifacao_mensal"]) if data.get("tarifacao_mensal") else None
        )

@dataclass
class MovimentacaoDetalheOperacao:
    codigo: str
    descricao: str
    valor_cents: int

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de MovimentacaoDetalheOperacao a partir de um dicionário.
        """
        return cls(
            codigo=data["codigo"],
            descricao=data["descricao"],
            valor_cents=str_to_cents(data["valor"])
        )

@dataclass
class Movimentacao:
    agencia: float
    conta: float
    data_movimentacao: date
    numero_carteira: float
    codigo_status: str
    tipo_movimentacao: str
    tipo_cobranca: str
    nosso_numero: str
    seu_numero: str
    dac_titulo: float
    sequencia_titulo: float
    pagador: str
    agencia_recebedora: float
    data_movimentacao_titulo_carteira: date
    data_inclusao: date
    data_vencimento: date
    valor_titulo_cents: int
    valor_liquido_lancado_cents: int
    valor_acrescimo_cents: int
    valor_decrescimo_cents: int
    indicador_pagamento_reserva_administrativa: str
    indicador_rateio_credito: bool
    dac_agencia_conta_beneficiario: float
    operacoes_cobranca: List[MovimentacaoDetalheOperacao]
    operacoes_desconto: Optional[List[MovimentacaoDetalheOperacao]] = None

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de Movimentacao a partir de um dicionário.
        """
        return cls(
            agencia=data["agencia"],
            conta=data["conta"],
            data_movimentacao=date.fromisoformat(data["data_movimentacao"]),
            numero_carteira=data["numero_carteira"],
            codigo_status=data["codigo_status"],
            tipo_movimentacao=data["tipo_movimentacao"],
            tipo_cobranca=data["tipo_cobranca"],
            nosso_numero=data["nosso_numero"],
            seu_numero=data["seu_numero"],
            dac_titulo=data["dac_titulo"],
            sequencia_titulo=data["sequencia_titulo"],
            pagador=data["pagador"],
            agencia_recebedora=data["agencia_recebedora"],
            data_movimentacao_titulo_carteira=date.fromisoformat(data["data_movimentacao_titulo_carteira"]),
            data_inclusao=date.fromisoformat(data["data_inclusao"]),
            data_vencimento=date.fromisoformat(data["data_vencimento"]),
            valor_titulo_cents=str_to_cents(data["valor_titulo"]),
            valor_liquido_lancado_cents=str_to_cents(data["valor_liquido_lancado"]),
            valor_acrescimo_cents=str_to_cents(data["valor_acrescimo"]),
            valor_decrescimo_cents=str_to_cents(data["valor_decrescimo"]),
            indicador_pagamento_reserva_administrativa=data["indicador_pagamento_reserva_administrativa"],
            indicador_rateio_credito=data["indicador_rateio_credito"],
            dac_agencia_conta_beneficiario=data["dac_agencia_conta_beneficiario"],
            operacoes_cobranca=[MovimentacaoDetalheOperacao.from_dict(op) for op in data["operacoes_cobranca"]],
            operacoes_desconto=[MovimentacaoDetalheOperacao.from_dict(op) for op in data["operacoes_desconto"]] if data.get("operacoes_desconto") else None
        )

@dataclass
class ResumoLiquidacaoDesconto:
    liquidacao_desconto_cents: int
    credito_conta_corrente_cents: int
    debito_conta_corrente_cents: int
    juros_moratorio_cents: int

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de ResumoLiquidacaoDesconto a partir de um dicionário.
        """
        return cls(
            liquidacao_desconto_cents=str_to_cents(data["liquidacao_desconto"]),
            credito_conta_corrente_cents=str_to_cents(data["credito_conta_corrente"]),
            debito_conta_corrente_cents=str_to_cents(data["debito_conta_corrente"]),
            juros_moratorio_cents=str_to_cents(data["juros_moratorio"])
        )

@dataclass
class ResumoEntradaDesconto:
    valor_creditado_conta_corrente_apos_deducoes_cents: int
    deducoes: List[FrancesaResumidaMovimentacaoContaDeducao]

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de ResumoEntradaDesconto a partir de um dicionário.
        """
        return cls(
            valor_creditado_conta_corrente_apos_deducoes_cents=str_to_cents(data["valor_creditado_conta_corrente_apos_deducoes"]),
            deducoes=[FrancesaResumidaMovimentacaoContaDeducao.from_dict(deducao) for deducao in data["deducoes"]]
        )

@dataclass
class ResumidaDescontado:
    posicao: Optional[Posicao] = None
    resumo_liquidacao_desconto: Optional[ResumoLiquidacaoDesconto] = None
    resumo_entrada_desconto: Optional[ResumoEntradaDesconto] = None

@dataclass
class ResumidaCobranca:
    posicao: Posicao
    movimentacao_financeira: MovimentacaoFinanceira
    movimentacao_conta: MovimentacaoConta

@dataclass
class MovimentacaoResumida:
    resumida_cobranca: ResumidaCobranca
    resumida_descontado: Optional[ResumidaDescontado] = None

@dataclass
class Francesa:
    posicao: Optional[Posicao] = None
    movimentacao_financeira: Optional[MovimentacaoFinanceira] = None
    movimentacao_conta: Optional[MovimentacaoConta] = None

@dataclass
class Error:
    """
    Error model
    """
    status: int
    """
    Error code
    """
    message: str
    """
    Error message
    """

    @property
    def exception(self):
        """
        Returns a formatted exception message.
        """
        return f"Error {self.status}: {self.message}"

    @classmethod
    def from_dict(cls, data: dict):
        """
        {
            "description": "Error model",
            "type": "object",
            "properties": {
                "status": {
                    "type": "number",
                    "description": "Error code"
                },
                "message": {
                    "type": "string",
                    "description": "Error message"
                }
            }
        }
        """
        assert "status" in data and "message" in data, f"Invalid error data: {data}"
        return cls(status=data["status"], message=data["message"])

class BoletosV3Client:
    """
    Cliente para a API Boletos v3 do Itaú.
    """
    def __init__(self, creds: Credentials, base_url: str = None):
        self.creds = creds
        self.base_url = base_url or "https://sandbox.devportal.itau.com.br/itau-ep9-gtw-boletos-boletos-v3-ext-aws/v1"

    def _get_headers(self, correlation_id=None):
        return {
            "Authorization": f"Bearer {self.creds.get_token().access_token}",
            "x-itau-correlationid": correlation_id or str(uuid.uuid4()),
            "User-Agent": "Collection-by-itaú-for-developers",
            "Accept": "application/json",
        }

    def get_francesas(
        self, 
        agencia: str, 
        conta: str, 
        dac: str, 
        correlation_id: Optional[uuid.UUID] = None,
        mes_referencia: Optional[str] = None,
        data: Optional[str] = None
    ):
        """
        Recupera a lista de francesas cadastradas.
        Corresponde ao endpoint GET /francesas.

        @param agencia: str - 4 dígitos da agência.
        @param conta: str - 7 dígitos da conta corrente.
        @param dac: str - 1 dígito do dac.
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        @param mes_referencia: Optional[str] - Mês de referência para consulta de datas disponíveis para visualização da francesa (formato mmyyyy).
        @param data: Optional[str] - Data para consulta de datas disponíveis para visualização da francesa.
        """
        url = f"{self.base_url}/francesas"
        params = {
            "agencia": agencia,
            "conta": conta,
            "dac": dac
        }
        
        if mes_referencia:
            params["mes_referencia"] = mes_referencia
        if data:
            params["data"] = data
            
        headers = self._get_headers(correlation_id)
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            response.raise_for_status()

    def get_francesa_movimentacoes(
        self, 
        id_francesa: str, 
        correlation_id: Optional[uuid.UUID] = None
    ):
        """
        Recupera as movimentações de uma francesa específica.
        Corresponde ao endpoint GET /francesas/{id_francesa}/movimentacoes.

        @param id_francesa: str - Identificador da francesa.
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        """
        url = f"{self.base_url}/francesas/{id_francesa}/movimentacoes"
        headers = self._get_headers(correlation_id)
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            response.raise_for_status()

    def get_francesa_movimentacoes_resumidas(
        self, 
        id_francesa: str, 
        correlation_id: Optional[uuid.UUID] = None
    ):
        """
        Recupera as movimentações resumidas de uma francesa específica.
        Corresponde ao endpoint GET /francesas/{id_francesa}/movimentacoes_resumidas.

        @param id_francesa: str - Identificador da francesa.
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        """
        url = f"{self.base_url}/francesas/{id_francesa}/movimentacoes_resumidas"
        headers = self._get_headers(correlation_id)
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            response.raise_for_status()

    def get_boletos(
        self, 
        data_inicial: str,
        data_final: str,
        id_beneficiario: str,
        correlation_id: Optional[uuid.UUID] = None,
        codigo_carteira: Optional[str] = None,
        nome_pagador: Optional[str] = None,
        numero_cpf_cnpj_pagador: Optional[int] = None,
        numero_nosso_numero: Optional[int] = None,
        seu_numero: Optional[str] = None,
        tipo_boleto: Optional[str] = None,
        situacao_geral_boleto: Optional[str] = None,
        status_vencimento: Optional[str] = None,
        status_boleto_canal: Optional[str] = None,
        data_vencimento_inicial: Optional[str] = None,
        data_vencimento_final: Optional[str] = None,
        valor_titulo_inicial: Optional[float] = None,
        valor_titulo_final: Optional[float] = None,
        valor_pago_total_inicial: Optional[float] = None,
        valor_pago_total_final: Optional[float] = None,
        data_inclusao_boleto_inicial: Optional[str] = None,
        data_inclusao_boleto_final: Optional[str] = None,
        data_inclusao_pagamento_inicial: Optional[str] = None,
        data_inclusao_pagamento_final: Optional[str] = None,
        emitir_segunda_via: Optional[bool] = None
    ):
        """
        Recupera a lista de boletos.
        Corresponde ao endpoint GET /boletos.

        @param data_inicial: str - Data inicial da pesquisa (formato: 2021-01-23T00:00:00.000Z).
        @param data_final: str - Data final da pesquisa (formato: 2021-01-23T00:00:00.000Z).
        @param id_beneficiario: str - (4 dígitos agência)(5 dígitos c/c)+(1 dígito DAC).
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        @param codigo_carteira: Optional[str] - Número da carteira utilizada na emissão do boleto.
        @param nome_pagador: Optional[str] - Nome do destinatário do boleto.
        @param numero_cpf_cnpj_pagador: Optional[int] - Número do CPF ou CNPJ do destinatário do boleto.
        @param numero_nosso_numero: Optional[int] - Nosso número informado na emissão do boleto.
        @param seu_numero: Optional[str] - Seu número, informado pelo beneficiário de cobrança.
        @param tipo_boleto: Optional[str] - Tipo do boleto.
        @param situacao_geral_boleto: Optional[str] - Situação geral do boleto.
        @param status_vencimento: Optional[str] - Status do vencimento.
        @param status_boleto_canal: Optional[str] - Status do boleto no canal.
        @param data_vencimento_inicial: Optional[str] - Data de vencimento inicial.
        @param data_vencimento_final: Optional[str] - Data de vencimento final.
        @param valor_titulo_inicial: Optional[float] - Valor do título inicial.
        @param valor_titulo_final: Optional[float] - Valor do título final.
        @param valor_pago_total_inicial: Optional[float] - Valor pago total inicial.
        @param valor_pago_total_final: Optional[float] - Valor pago total final.
        @param data_inclusao_boleto_inicial: Optional[str] - Data de inclusão do boleto inicial.
        @param data_inclusao_boleto_final: Optional[str] - Data de inclusão do boleto final.
        @param data_inclusao_pagamento_inicial: Optional[str] - Data de inclusão do pagamento inicial.
        @param data_inclusao_pagamento_final: Optional[str] - Data de inclusão do pagamento final.
        @param emitir_segunda_via: Optional[bool] - Indicador para emitir segunda via.
        """
        url = f"{self.base_url}/boletos"
        params = {
            "data_inicial": data_inicial,
            "data_final": data_final,
            "id_beneficiario": id_beneficiario
        }
        
        # Adiciona parâmetros opcionais
        optional_params = {
            "codigo_carteira": codigo_carteira,
            "nome_pagador": nome_pagador,
            "numero_cpf_cnpj_pagador": numero_cpf_cnpj_pagador,
            "numero_nosso_numero": numero_nosso_numero,
            "seu_numero": seu_numero,
            "tipo_boleto": tipo_boleto,
            "situacao_geral_boleto": situacao_geral_boleto,
            "status_vencimento": status_vencimento,
            "status_boleto_canal": status_boleto_canal,
            "data_vencimento_inicial": data_vencimento_inicial,
            "data_vencimento_final": data_vencimento_final,
            "valor_titulo_inicial": valor_titulo_inicial,
            "valor_titulo_final": valor_titulo_final,
            "valor_pago_total_inicial": valor_pago_total_inicial,
            "valor_pago_total_final": valor_pago_total_final,
            "data_inclusao_boleto_inicial": data_inclusao_boleto_inicial,
            "data_inclusao_boleto_final": data_inclusao_boleto_final,
            "data_inclusao_pagamento_inicial": data_inclusao_pagamento_inicial,
            "data_inclusao_pagamento_final": data_inclusao_pagamento_final,
            "emitir_segunda_via": emitir_segunda_via
        }
        
        # Adiciona apenas os parâmetros que não são None
        for key, value in optional_params.items():
            if value is not None:
                params[key] = value
                
        headers = self._get_headers(correlation_id)
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            response.raise_for_status()

    def post_notificacao_boletos(
        self, 
        data: dict, 
        correlation_id: Optional[uuid.UUID] = None
    ):
        """
        Cria uma nova notificação de boleto.
        Corresponde ao endpoint POST /notificacoes_boletos.

        @param data: dict - Dados da notificação a ser criada.
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        """
        url = f"{self.base_url}/notificacoes_boletos"
        headers = self._get_headers(correlation_id)
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code in (200, 201):
            return response.json()
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            response.raise_for_status()

    def get_notificacoes_boleto(
        self, 
        correlation_id: Optional[uuid.UUID] = None
    ):
        """
        Recupera a lista de notificações de boletos.
        Corresponde ao endpoint GET /notificacoes_boletos.

        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        """
        url = f"{self.base_url}/notificacoes_boletos"
        headers = self._get_headers(correlation_id)
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            response.raise_for_status()

    def delete_notificacao_boleto(
        self, 
        id_notificacao_boleto: str, 
        correlation_id: Optional[uuid.UUID] = None
    ):
        """
        Remove uma notificação de boleto específica.
        Corresponde ao endpoint DELETE /notificacoes_boletos/{id_notificacao_boleto}.

        @param id_notificacao_boleto: str - Identificador da notificação de boleto.
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        """
        url = f"{self.base_url}/notificacoes_boletos/{id_notificacao_boleto}"
        headers = self._get_headers(correlation_id)
        response = requests.delete(url, headers=headers)
        
        if response.status_code in (200, 204):
            return True
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            response.raise_for_status()

    def patch_notificacao_boleto(
        self, 
        id_notificacao_boleto: str, 
        data: dict, 
        correlation_id: Optional[uuid.UUID] = None
    ):
        """
        Atualiza parcialmente uma notificação de boleto específica.
        Corresponde ao endpoint PATCH /notificacoes_boletos/{id_notificacao_boleto}.

        @param id_notificacao_boleto: str - Identificador da notificação de boleto.
        @param data: dict - Dados a serem atualizados na notificação.
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        """
        url = f"{self.base_url}/notificacoes_boletos/{id_notificacao_boleto}"
        headers = self._get_headers(correlation_id)
        response = requests.patch(url, headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code in [400, 401, 403, 404, 422, 500, 503]:
            error_data = response.json()
            raise Error.from_dict(error_data).exception
        else:
            response.raise_for_status()

    # --- Métodos auxiliares para facilitar o uso da API ---

    def create_notificacao_boleto(
        self,
        id_beneficiario: str,
        webhook_url: str,
        webhook_client_id: str,
        webhook_client_secret: str,
        tipos_notificacoes: List[str],
        correlation_id: Optional[uuid.UUID] = None,
        webhook_oauth_url: Optional[str] = None,
        webhook_oauth_scope: Optional[str] = None,
        valor_minimo_cents: Optional[int] = None
    ):
        """
        Método auxiliar para criar uma notificação de boleto usando parâmetros nomeados.
        
        @param id_beneficiario: str - ID do beneficiário (formato: agência + conta + DAC).
        @param webhook_url: str - URL do webhook para receber notificações.
        @param webhook_client_id: str - Client ID para autenticação OAuth.
        @param webhook_client_secret: str - Client Secret para autenticação OAuth.
        @param tipos_notificacoes: List[str] - Lista de tipos de notificação (ex: ["BAIXA_EFETIVA", "BAIXA_OPERACIONAL"]).
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        @param webhook_oauth_url: Optional[str] - URL para autenticação OAuth.
        @param webhook_oauth_scope: Optional[str] - Escopo OAuth.
        @param valor_minimo_cents: Optional[int] - Valor mínimo para notificação em centavos.
        """
        data = {
            "data": {
                "id_beneficiario": id_beneficiario,
                "webhook_url": webhook_url,
                "webhook_client_id": webhook_client_id,
                "webhook_client_secret": webhook_client_secret,
                "tipos_notificacoes": tipos_notificacoes
            }
        }
        
        if webhook_oauth_url:
            data["data"]["webhook_oauth_url"] = webhook_oauth_url
        if webhook_oauth_scope:
            data["data"]["webhook_oauth_scope"] = webhook_oauth_scope
        if valor_minimo_cents is not None:
            data["data"]["valor_minimo"] = valor_minimo_cents / 100.0  # Converte centavos para reais
            
        return self.post_notificacao_boletos(data, correlation_id)

    def update_notificacao_boleto(
        self,
        id_notificacao_boleto: str,
        correlation_id: Optional[uuid.UUID] = None,
        webhook_client_id: Optional[str] = None,
        webhook_client_secret: Optional[str] = None,
        webhook_url: Optional[str] = None,
        webhook_oauth_url: Optional[str] = None,
        webhook_oauth_scope: Optional[str] = None,
        valor_minimo_cents: Optional[int] = None
    ):
        """
        Método auxiliar para atualizar uma notificação de boleto usando parâmetros nomeados.
        
        @param id_notificacao_boleto: str - Identificador da notificação de boleto.
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        @param webhook_client_id: Optional[str] - Client ID para autenticação OAuth.
        @param webhook_client_secret: Optional[str] - Client Secret para autenticação OAuth.
        @param webhook_url: Optional[str] - URL do webhook para receber notificações.
        @param webhook_oauth_url: Optional[str] - URL para autenticação OAuth.
        @param webhook_oauth_scope: Optional[str] - Escopo OAuth.
        @param valor_minimo_cents: Optional[int] - Valor mínimo para notificação em centavos.
        """
        data = {}
        
        if webhook_client_id is not None:
            data["webhook_client_id"] = webhook_client_id
        if webhook_client_secret is not None:
            data["webhook_client_secret"] = webhook_client_secret
        if webhook_url is not None:
            data["webhook_url"] = webhook_url
        if webhook_oauth_url is not None:
            data["webhook_oauth_url"] = webhook_oauth_url
        if webhook_oauth_scope is not None:
            data["webhook_oauth_scope"] = webhook_oauth_scope
        if valor_minimo_cents is not None:
            data["valor_minimo"] = valor_minimo_cents / 100.0  # Converte centavos para reais
            
        return self.patch_notificacao_boleto(id_notificacao_boleto, data, correlation_id)

    def get_boletos_by_date_range(
        self,
        data_inicial: date,
        data_final: date,
        id_beneficiario: str,
        correlation_id: Optional[uuid.UUID] = None,
        **kwargs
    ):
        """
        Método auxiliar para consultar boletos usando objetos date.
        
        @param data_inicial: date - Data inicial da pesquisa.
        @param data_final: date - Data final da pesquisa.
        @param id_beneficiario: str - ID do beneficiário.
        @param correlation_id: Optional[uuid.UUID] - Identificador único para rastreamento da requisição.
        @param **kwargs: Parâmetros opcionais adicionais para filtrar boletos.
        """
        # Converte as datas para o formato ISO com timezone
        data_inicial_str = data_inicial.strftime("%Y-%m-%dT00:00:00.000Z")
        data_final_str = data_final.strftime("%Y-%m-%dT23:59:59.999Z")
        
        return self.get_boletos(
            data_inicial=data_inicial_str,
            data_final=data_final_str,
            id_beneficiario=id_beneficiario,
            correlation_id=correlation_id,
            **kwargs
        )
