from dataclasses import dataclass
from typing import Literal


@dataclass
class Loc:
    """**Descrição:** Dados da localização do payload."""

    id: int
    """**Descrição:** Identificador da URL do PIX para consulta do payload criptografado - pix link BACEN."""

    location: str
    """**Descrição:** URL do PIX para consulta do payload criptografado - pix link BACEN."""

    tipo_cob: Literal["cob", "cobv"]
    """**Descrição:** Define se o tipo do documento é imediata ou vencimento."""

    criacao: str
    """**Descrição:** Data e hora de criação da localização da cobrança."""

    def __post_init__(self):
        assert isinstance(self.id, int), f"ID deve ser um inteiro, recebeu {type(self.id)}."
        assert isinstance(self.location, str) and len(self.location) <= 77, f"Location deve ser uma string com no máximo 77 caracteres, recebeu {self.location}."
        assert self.tipo_cob in ["cob", "cobv"], f"Tipo de cobrança inválido: {self.tipo_cob}."

    @classmethod
    def from_dict(cls, data: dict):
        """
        {
            "type": "object",
            "title": "Location do Payload",
            "description": "**Descrição:** Dados da localização do payload.\n",
            "properties": {
                "id": {
                    "title": "Identificador da Localização do Payload",
                    "description": "**Descrição:** Identificador da URL do PIX para consulta do payload criptografado - pix link BACEN.\n\n**Tipo do campo:** integer($int64).\n",
                    "type": "integer",
                    "readOnly": true
                },
                "location": {
                    "title": "Localização do Payload",
                    "description": "**Descrição:** URL do PIX para consulta do payload criptografado - pix link BACEN.\n\n**Tipo do campo:** integer($uri).\n",
                    "type": "string",
                    "maxLength": 77,
                    "readOnly": true
                },
                "tipoCob": {
                    "title": "Tipo da Cobrança",
                    "description": "**Descrição:** Define se o tipo do documento é imediata ou vencimento.\n",
                    "enum": [
                        "cob",
                        "cobv"
                    ],
                    "type": "string"
                },
                "criacao": {
                    "title": "Data de Criação",
                    "description": "**Descrição:** Data e hora de criação da localização da cobrança.\n\n**Observação:** Respeita RFC 3339.\n\n**Tipo do campo:** string($date-time).\n",
                    "type": "string",
                    "readOnly": true
                }
            },
            "required": [
                "id",
                "location",
                "tipoCob",
                "criacao"
            ]
        }
        """

        return cls(
            id=data.get("id"),
            location=data.get("location"),
            tipo_cob=data.get("tipoCob"),
            criacao=data.get("criacao")
        )