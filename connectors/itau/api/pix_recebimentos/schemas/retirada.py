from dataclasses import dataclass
from typing import Optional
from .saque import Saque
from .troco import Troco


"""
{
    "type": "object",
    "title": "Informações de Retirada",
    "description": "**Descrição:** Estrutura opcional relacionada ao Saque/Troco Pix.\n",
    "properties": {
        "saque": {
            "$ref": "#/components/schemas/saque"
        },
        "troco": {
            "$ref": "#/components/schemas/troco"
        }
    }
}
"""

@dataclass
class Retirada:
    saque: Optional[Saque] = None
    troco: Optional[Troco] = None

    def __post_init__(self):
        if self.saque is not None and not isinstance(self.saque, Saque):
            raise TypeError("saque must be an instance of Saque")
        if self.troco is not None and not isinstance(self.troco, Troco):
            raise TypeError("troco must be an instance of Troco")
    
    @classmethod
    def from_dict(cls, data: dict):
        saque = Saque.from_dict(data['saque']) if 'saque' in data else None
        troco = Troco.from_dict(data['troco']) if 'troco' in data else None
        return cls(saque=saque, troco=troco)