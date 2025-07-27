"""
schema:
{
    "type": "object",
    "description": "",
    "properties": {
        "original": {
            "description": "Valor original da cobrança.",
            "type": "object",
            "properties": {
                "valor": {
                    "description": "Valor original da cobrança.",
                    "type": "string",
                    "example": "10.00"
                }
            },
            "required": [
                "valor"
            ]
        },
        "saque": {
            "$ref": "#/components/schemas/saqueCv"
        },
        "troco": {
            "$ref": "#/components/schemas/trocoCv"
        },
        "juros": {
            "description": "Juro aplicado à cobrança.",
            "type": "object",
            "properties": {
                "valor": {
                    "description": "Juro aplicado à cobrança.",
                    "type": "string",
                    "example": "10.00"
                }
            },
            "required": [
                "valor"
            ]
        },
        "multa": {
            "description": "Multa aplicada à cobrança.",
            "type": "object",
            "properties": {
                "valor": {
                    "description": "Multa aplicada à cobrança.",
                    "type": "string",
                    "example": "10.00"
                }
            },
            "required": [
                "valor"
            ]
        },
        "desconto": {
            "description": "Descontos aplicados à cobrança.",
            "type": "object",
            "properties": {
                "valor": {
                    "description": "Descontos aplicados à cobrança.",
                    "type": "string",
                    "example": "10.00"
                }
            },
            "required": [
                "valor"
            ]
        },
        "abatimento": {
            "description": "Abatimento aplicado à cobrança.",
            "type": "object",
            "properties": {
                "valor": {
                    "description": "Abatimento aplicado à cobrança.",
                    "type": "string",
                    "example": "10.00"
                }
            },
            "required": [
                "valor"
            ]
        }
    }
}
"""

from dataclasses import dataclass
from typing import Optional
from .saque import Saque
from .troco import Troco


@dataclass
class ComponentesValor:
    """
    **Descrição:** Componentes de valor que podem ser aplicados à cobrança.
    """

    original_cents: int
    """
    **Descrição:** Valor original da cobrança em centavos.
    """

    saque: Optional[Saque] = None
    """
    **Descrição:** Informações sobre o saque da cobrança, se aplicável.
    """

    troco: Optional[Troco] = None
    """
    **Descrição:** Informações sobre o troco da cobrança, se aplicável.
    """

    juros_cents: Optional[int] = None
    """
    **Descrição:** Juro aplicado à cobrança em centavos.
    """

    multa_cents: Optional[int] = None
    """
    **Descrição:** Multa aplicada à cobrança em centavos.
    """

    desconto_cents: Optional[int] = None
    """
    **Descrição:** Descontos aplicados à cobrança em centavos.
    """

    abatimento_cents: Optional[int] = None
    """
    **Descrição:** Abatimento aplicado à cobrança em centavos.
    """

    def __post_init__(self):
        if self.original_cents < 0:
            raise ValueError("O valor original não pode ser negativo.")
        if self.juros_cents is not None and self.juros_cents < 0:
            raise ValueError("O juro não pode ser negativo.")
        if self.multa_cents is not None and self.multa_cents < 0:
            raise ValueError("A multa não pode ser negativa.")
        if self.desconto_cents is not None and self.desconto_cents < 0:
            raise ValueError("O desconto não pode ser negativo.")
        if self.abatimento_cents is not None and self.abatimento_cents < 0:
            raise ValueError("O abatimento não pode ser negativo.")
        
    @classmethod
    def from_dict(cls, data: dict) -> "ComponentesValor":
        """
        Cria uma instância de ComponentesValor a partir de um dicionário.
        """
        return cls(
            original_cents=int(data.get("original", {}).get("valor", 0)) * 100,
            saque=Saque.from_dict(data.get("saque")) if data.get("saque") else None,
            troco=Troco.from_dict(data.get("troco")) if data.get("troco") else None,
            juros_cents=int(data.get("juros", {}).get("valor", 0)) * 100 if data.get("juros") else None,
            multa_cents=int(data.get("multa", {}).get("valor", 0)) * 100 if data.get("multa") else None,
            desconto_cents=int(data.get("desconto", {}).get("valor", 0)) * 100 if data.get("desconto") else None,
            abatimento_cents=int(data.get("abatimento", {}).get("valor", 0)) * 100 if data.get("abatimento") else None
        )