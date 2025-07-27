"""
schema:
{
    "type": "object",
    "description": "",
    "properties": {
        "nome": {
            "description": "**Descrição:** Nome do campo de informação adicional.\n",
            "type": "string",
            "title": "Nome",
            "maxLength": 50
        },
        "valor": {
            "description": "**Descrição:** Dados a serem apresentados na informação adicional.\n",
            "type": "string",
            "title": "Valor",
            "maxLength": 200
        }
    },
    "required": [
        "nome",
        "valor"
    ]
}
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class InformacaoAdicional:
    """
    **Descrição:** Informações adicionais que podem ser apresentadas na cobrança.
    """

    nome: str
    """
    **Descrição:** Nome do campo de informação adicional.
    """

    valor: str
    """
    **Descrição:** Dados a serem apresentados na informação adicional.
    """

    def __post_init__(self):
        if len(self.nome) > 50:
            raise ValueError("O campo 'nome' deve ter no máximo 50 caracteres.")
        if len(self.valor) > 200:
            raise ValueError("O campo 'valor' deve ter no máximo 200 caracteres.")
    
    @classmethod
    def from_dict(cls, data: dict) -> "InformacaoAdicional":
        """
        Cria uma instância de InformacaoAdicional a partir de um dicionário.
        """
        return cls(
            nome=data.get("nome"),
            valor=data.get("valor")
        )