"""
{
    "type": "object",
    "title": "Valor da Cobrança com Vencimento",
    "description": "**Descrição:** Campo que organiza os valores monetários referentes à cobrança.\n",
    "properties": {
        "original": {
            "title": "Valor",
            "description": "**Descrição:** Valor nominal/original da cobrança.\n\n**Observação:** O valor deve ser maior do que zero. Todos os campos que indicam valores monetários obedecem ao formato do ID 54 da especificação EMV/BR Code para QR Codes. O separador decimal é o caractere ponto. Não é aplicável utilizar separador de milhar. Exemplos de valores aderentes ao padrão: “0.00”, “1.00”, “123.99”, “123456789.23”.\n",
            "type": "string",
            "pattern": "\\d{1,10}\\.\\d{2}"
        },
        "multa": {
            "title": "Multa Aplicada",
            "description": "**Descrição:** Multa aplicada à cobrança.\n",
            "type": "object",
            "properties": {
                "modalidade": {
                    "title": "Modalidade da Multa",
                    "description": "**Descrição:** Modalidade da multa, conforme tabela de domínios.\n| Descrição  | Domínio |\n| ---------- | ------- |\n| Valor Fixo | 1       |\n| Percentual | 2       |\n\n**Tipo do campo:** integer($int32).\n",
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 2
                },
                "valorPerc": {
                    "title": "Valor da Multa Absoluta",
                    "description": "**Descrição:** Multa do documento em valor absoluto ou percentual, conforme `valor.multa.modalidade`.\n",
                    "type": "string",
                    "pattern": "\\d{1,10}\\.\\d{2}"
                }
            },
            "required": [
                "modalidade",
                "valorPerc"
            ]
        },
        "juros": {
            "title": "Juro Aplicado",
            "description": "**Descrição:** Juros aplicado à cobrança.\n",
            "type": "object",
            "properties": {
                "modalidade": {
                    "title": "Modalidade de Juros",
                    "description": "**Descrição:** Modalidade de juros, conforme tabela de domínios.\n\n| Descrição                         | Domínio |\n| --------------------------------- | ------- |\n| Valor (dias corridos)             | 1       |\n| Percentual ao dia (dias corridos) | 2       |\n| Percentual ao mês (dias corridos) | 3       |\n| Percentual ao ano (dias corridos) | 4       |\n| Valor (dias úteis)                | 5       |\n| Percentual ao dia (dias úteis)    | 6       |\n| Percentual ao mês (dias úteis)    | 7       |\n| Percentual ao ano (dias úteis)    | 8       |\n\n**Tipo do campo:** integer($int32).\n",
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 8
                },
                "valorPerc": {
                    "title": "Valor",
                    "description": "**Descrição:** Juros do documento em valor absoluto ou percentual.\n",
                    "type": "string",
                    "pattern": "\\d{1,10}\\.\\d{2}"
                }
            },
            "required": [
                "modalidade",
                "valorPerc"
            ]
        },
        "abatimento": {
            "title": "Abatimento Aplicado",
            "description": "**Descrição:** Abatimento aplicado à cobrança.\n",
            "type": "object",
            "properties": {
                "modalidade": {
                    "title": "Modalidade de Abatimentos",
                    "description": "**Descrição:** Modalidade de abatimentos, conforme tabela de domínios.\n| Descrição  | Domínio |\n| ---------- | ------- |\n| Valor Fixo | 1       |\n| Percentual | 2       |\n\n**Tipo do campo:** integer($int32).\n",
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 2
                },
                "valorPerc": {
                    "title": "Abatimentos",
                    "description": "**Descrição:** Abatimentos ou outras deduções aplicadas ao documento, em valor absoluto ou percentual do valor original do documento.\n",
                    "type": "string",
                    "pattern": "\\d{1,10}\\.\\d{2}"
                }
            },
            "required": [
                "modalidade",
                "valorPerc"
            ]
        },
        "desconto": {
            "title": "Descontos Aplicados",
            "description": "**Descrição:** Descontos aplicados à cobranca.\n",
            "type": "object",
            "properties": {
                "modalidade": {
                    "title": "Modalidade de Descontos",
                    "description": "**Descrição:** Modalidade de desconto, conforme tabela de domínios.\n| Descrição                                | Domínio |\n| ---------------------------------------- | ------- |\n| Valor Fixo até a[s] data[s] informada[s] | 1       |\n| Percentual até a data informada          | 2       |\n| Valor por antecipação dia corrido        | 3       |\n| Valor por antecipação dia útil           | 4       |\n| Percentual por antecipação dia corrido   | 5       |\n| Percentual por antecipação dia útil      | 6       |\n\n**Tipo do campo:** integer($int32).\n",
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 6
                },
                "valorPerc": {
                    "title": "Abatimentos",
                    "description": "**Descrição:** Abatimentos ou outras deduções aplicadas ao documento, em valor absoluto ou percentual do valor original do documento.\n\n**Observação:** Não deve ser enviado `valorPerc` e `descontoDataFixa` juntos.\n",
                    "type": "string",
                    "pattern": "\\d{1,10}\\.\\d{2}"
                },
                "descontoDataFixa": {
                    "title": "Lista de Descontos",
                    "description": "**Descrição:** Data limite para o desconto absoluto da cobrança.\n\n**Observação:** A data de desconto obrigatoriamente deverá ser menor que a data de vencimento da cobrança.\n",
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 3,
                    "uniqueItems": true,
                    "items": {
                        "type": "object",
                        "description": "",
                        "properties": {
                            "data": {
                                "title": "Data Limite",
                                "description": "**Descrição:** Data limite para o desconto absoluto da cobrança.\n\n**Observação:** Descontos por pagamento antecipado, com data fixa. Matriz com até três elementos, sendo que cada elemento é composto por um par `data` e `valorPerc`, para estabelecer descontos percentuais ou absolutos, até aquela data de pagamento. Trata-se de uma data, no formato `YYYY-MM-DD`, segundo ISO 8601. A data de desconto obrigatoriamente deverá ser menor ou igual à data de vencimento da cobrança.\n\n**Tipo do campo:** string($date).\n",
                                "type": "string"
                            },
                            "valorPerc": {
                                "title": "Valor do Desconto Absoluto",
                                "description": "**Descrição:** Desconto em valor absoluto ou percentual por dia, útil ou corrido, conforme `valor.desconto.modalidade`.\n",
                                "type": "string",
                                "pattern": "\\d{1,10}\\.\\d{2}"
                            }
                        },
                        "required": [
                            "data",
                            "valorPerc"
                        ]
                    }
                }
            },
            "required": [
                "modalidade",
                "valorPerc"
            ]
        }
    },
    "required": [
        "original"
    ]
}
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from enum import Enum

class ValorMultaModalidade(Enum):
    FIXO = 1
    PERCENTUAL = 2

@dataclass
class ValorParte:
    """
    Modalidade de multa aplicada à cobrança.
    """

    modalidade: ValorMultaModalidade
    """
    Modalidade da multa, conforme tabela de domínios.
    1: Valor Fixo
    2: Percentual
    """

    valor_perc: Decimal
    """
    Valor da multa, em valor absoluto ou percentual.
    Deve seguir o formato `\\d{1,10}\\.\\d{2}`
    Exemplo: "123.45"
    """

    @classmethod
    def from_dict(cls, data: dict):
        modalidade = ValorMultaModalidade(data['modalidade'])
        valor_perc = Decimal(data['valorPerc'])
        return cls(modalidade=modalidade, valor_perc=valor_perc)

class ValorJurosModalidade(Enum):
    DIAS_CORRIDOS_VALOR = 1
    DIAS_CORRIDOS_PERC_DIA = 2
    DIAS_CORRIDOS_PERC_MES = 3
    DIAS_CORRIDOS_PERC_ANO = 4
    DIAS_UTEIS_VALOR = 5
    DIAS_UTEIS_PERC_DIA = 6
    DIAS_UTEIS_PERC_MES = 7
    DIAS_UTEIS_PERC_ANO = 8

@dataclass
class ValorJuros:
    """
    Modalidade de juros aplicada à cobrança.
    """

    modalidade: ValorJurosModalidade
    """
    Modalidade de juros, conforme tabela de domínios.
    1: Valor (dias corridos)
    2: Percentual ao dia (dias corridos)
    3: Percentual ao mês (dias corridos)
    4: Percentual ao ano (dias corridos)
    5: Valor (dias úteis)
    6: Percentual ao dia (dias úteis)
    7: Percentual ao mês (dias úteis)
    8: Percentual ao ano (dias úteis)
    """

    valor_perc: Decimal
    """
    Valor dos juros, em valor absoluto ou percentual.
    Deve seguir o formato `\\d{1,10}\\.\\d{2}`
    Exemplo: "123.45"
    """

    @classmethod
    def from_dict(cls, data: dict):
        modalidade = ValorJurosModalidade(data['modalidade'])
        valor_perc = Decimal(data['valorPerc'])
        return cls(modalidade=modalidade, valor_perc=valor_perc)

@dataclass
class Valor:
    """
    Valor da cobrança com vencimento.
    """

    original_cents: int
    """
    Valor nominal/original da cobrança, em centavos.
    """

    multa: Optional[ValorParte] = None
    """
    Multa aplicada à cobrança.
    Deve ser uma instância de `ValorParte`.
    """

    juros: Optional[ValorJuros] = None
    """
    Juros aplicados à cobrança.
    Deve ser uma instância de `ValorJuros`.
    """

    abatimento: Optional[ValorParte] = None
    """
    Abatimento aplicado à cobrança.
    Deve ser uma instância de `ValorParte`.
    """

    desconto: Optional[ValorParte] = None
    """
    Descontos aplicados à cobrança.
    Deve ser uma instância de `ValorParte`.
    """

    def __post_init__(self):
        if not isinstance(self.original_cents, int) or self.original_cents <= 0:
            raise ValueError("original_cents must be a positive integer")
        if self.multa is not None and not isinstance(self.multa, ValorParte):
            raise TypeError("multa must be an instance of ValorParte")
        if self.juros is not None and not isinstance(self.juros, ValorJuros):
            raise TypeError("juros must be an instance of ValorJuros")
        if self.abatimento is not None and not isinstance(self.abatimento, ValorParte):
            raise TypeError("abatimento must be an instance of ValorParte")
        if self.desconto is not None and not isinstance(self.desconto, ValorParte):
            raise TypeError("desconto must be an instance of ValorParte")
    
    @classmethod
    def from_dict(cls, data: dict):
        original_cents = int(data['original'] * 100)
        multa = ValorParte.from_dict(data['multa']) if 'multa' in data else None
        juros = ValorJuros.from_dict(data['juros']) if 'juros' in data else None
        abatimento = ValorParte.from_dict(data['abatimento']) if 'abatimento' in data else None
        desconto = ValorParte.from_dict(data['desconto']) if 'desconto' in data else None
        return cls(original_cents=original_cents, multa=multa, juros=juros, abatimento=abatimento, desconto=desconto)