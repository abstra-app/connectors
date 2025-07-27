from dataclasses import dataclass
from typing import Optional, Literal

@dataclass
class Troco:
    """**Descrição:** Informações relacionadas ao troco."""

    valor: str
    """**Descrição:** Valor do troco efetuado."""

    modalidade_alteracao: Optional[int] = 0
    """**Descrição:** Modalidade de alteração do troco. Indica se o valor final do documento pode ser alterado pelo pagador."""

    modalidade_agente: Literal["AGTEC", "AGTOT"]
    """**Descrição:** Modalidade do agente responsável pelo troco."""

    prestador_do_servico_de_saque: str
    """**Descrição:** ISPB do facilitador de serviço de saque."""

    def __post_init__(self):
        assert isinstance(self.valor, str) and len(self.valor) <= 10, f"Valor deve ser uma string com no máximo 10 caracteres, recebeu {self.valor}."
        assert self.modalidade_agente in ["AGTEC", "AGTOT"], f"Modalidade do agente inválida: {self.modalidade_agente}."
        assert isinstance(self.prestador_do_servico_de_saque, str) and len(self.prestador_do_servico_de_saque) == 8, f"ISPB do facilitador de serviço de saque deve ter exatamente 8 caracteres, recebeu {self.prestador_do_servico_de_saque}."
        assert self.modalidade_alteracao in [0, 1], f"Modalidade de alteração deve ser 0 ou 1, recebeu {self.modalidade_alteracao}."

    @classmethod
    def from_dict(cls, data: dict):
        """
        {
            "type": "object",
            "title": "Troco",
            "description": "**Descrição:** Informações relacionadas ao troco.\n",
            "properties": {
                "valor": {
                    "description": "**Descrição:** Valor do troco efetuado. \n\n**Observação:** Valor mínimo do troco 10.00 e valor máximo do troco 500.00.\n",
                    "type": "string",
                    "title": "Valor do Troco",
                    "pattern": "\\d{1,10}\\.\\d{2}"
                },
                "modalidadeAlteracao": {
                    "title": "Modalidade de Alteração do Troco",
                    "description": "**Descrição:** Modalidade de alteração de valor do troco. Trata-se de um campo que determina se o valor final do documento pode ser alterado pelo pagador.\n\n**Observação:** Quando não preenchido o valor assumido é o 0 (zero).\n\nNa ausência desse campo, assume-se que não se pode alterar o valor do troco, ou seja, assume-se o valor 0.\n\nSe o campo estiver presente e com valor 1, então está determinado que o valor final do troco pode ser alterado pelo pagador.\n\n**Tipo do campo:** integer($int32).\n",
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 1
                },
                "modalidadeAgente": {
                    "title": "Modalidade do Agente",
                    "description": "**Descrição:** Modalidade do Agente.\n| SIGLA | Descrição                               |\n| ----- | --------------------------------------- |\n| AGTEC | Agente Estabelecimento Comercial        |\n| AGTOT | Agente Outra Espécie de Pessoa Jurídica |\n",
                    "type": "string",
                    "enum": [
                        "AGTEC",
                        "AGTOT"
                    ]
                },
                "prestadorDoServicoDeSaque": {
                    "title": "Facilitador de Serviço de Saque",
                    "description": "**Descrição:** ISPB do Facilitador de Serviço de Saque.\n",
                    "type": "string",
                    "pattern": "\\d{8}"
                }
            },
            "required": [
                "valor",
                "modalidadeAgente",
                "prestadorDoServicoDeSaque"
            ]
        }
        """
        return cls(
            valor=data.get("valor"),
            modalidade_alteracao=data.get("modalidadeAlteracao"),
            modalidade_agente=data.get("modalidadeAgente"),
            prestador_do_servico_de_saque=data.get("prestadorDoServicoDeSaque")
        )