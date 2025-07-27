from dataclasses import dataclass
from typing import Optional


@dataclass
class Devedor:
    """
    **Descrição:** Campo que organiza a identificação do devedor, ou seja, a pessoa ou instituição a quem a cobrança está endereçada. Não identifica, necessariamente, quem irá efetivamente realizar o pagamento.
    
    **Observação:** Não é permitido que o campo `devedor.cpf` e campo `devedor.cnpj` estejam preenchidos ao mesmo tempo. Se o campo `devedor.cnpj` está preenchido, então o campo `devedor.cpf` não pode estar preenchido, e vice-versa. Se o campo devedor.nome está preenchido, então deve existir ou um `devedor.cpf` ou um campo `devedor.cnpj` preenchido.
    """

    nome: str
    """
    **Descrição:** Nome do pagador da cobrança. 
    
    **Observação:** Necessário preencher o campo CNPJ ou o campo CPF.
    """

    email: Optional[str] = None
    """
    **Descrição:** E-mail do devedor.
    """

    logradouro: Optional[str] = None
    """
    **Descrição:** Logradouro do devedor.
    """

    cidade: Optional[str] = None
    """
    **Descrição:** Cidade do devedor.
    """

    uf: Optional[str] = None
    """
    **Descrição:** UF do devedor.
    """

    cep: Optional[str] = None
    """
    **Descrição:** CEP do devedor.
    """

    cpf: Optional[str] = None
    """
    **Descrição:** Número do Documento Cadastro de Pessoa Física.

    **Observação:** Se preenchido, não enviar CNPJ.
    """

    cnpj: Optional[str] = None
    """
    **Descrição:** Número do Cadastro Nacional da Pessoa Jurídica.
    
    **Observação:** Se preenchido, não enviar CPF.
    """


    def __post_init__(self):
        assert len(self.nome) <= 200, "Nome deve ter no máximo 200 caracteres."
        assert self.logradouro is None or len(self.logradouro) <= 200, "Logradouro deve ter no máximo 200 caracteres."
        assert self.cidade is None or len(self.cidade) <= 200, "Cidade deve ter no máximo 200 caracteres."
        assert self.uf is None or len(self.uf) == 2, "UF deve ter exatamente 2 caracteres."
        assert self.cep is None or len(self.cep) == 8, "CEP deve ter exatamente 8 caracteres."
        assert self.cpf is None or (len(self.cpf) == 11 and self.cpf.isdigit()), "CPF deve ser exatamente uma sequência de 11 dígitos numéricos."
        assert self.cnpj is None or (len(self.cnpj) == 14 and self.cnpj.isdigit()), "CNPJ deve ser exatamente uma sequência de 14 dígitos numéricos."

    @classmethod
    def from_dict(cls, data: dict):
        """
        {
            "type": "object",
            "title": "Devedor",
            "description": "**Descrição:** Campo que organiza a identificação do devedor, ou seja, a pessoa ou instituição a quem a cobrança está endereçada. Não identifica, necessariamente, quem irá efetivamente realizar o pagamento.\n\n**Observação:** Não é permitido que o campo `devedor.cpf` e campo `devedor.cnpj` estejam preenchidos ao mesmo tempo. Se o campo `devedor.cnpj` está preenchido, então o campo `devedor.cpf` não pode estar preenchido, e vice-versa. Se o campo devedor.nome está preenchido, então deve existir ou um `devedor.cpf` ou um campo `devedor.cnpj` preenchido.\n",
            "properties": {
                "email": {
                    "title": "Email",
                    "description": "**Descrição:** E-mail do devedor.\n",
                    "type": "string"
                },
                "logradouro": {
                    "title": "Logradouro",
                    "description": "**Descrição:** Logradouro do devedor.\n",
                    "type": "string",
                    "maxLength": 200
                },
                "cidade": {
                    "title": "Cidade",
                    "description": "**Descrição:** Cidade do devedor.\n",
                    "type": "string",
                    "maxLength": 200
                },
                "uf": {
                    "title": "UF",
                    "description": "**Descrição:** UF do devedor.\n",
                    "type": "string",
                    "maxLength": 2
                },
                "cep": {
                    "title": "CEP",
                    "description": "**Descrição:** CEP do devedor.\n",
                    "type": "string",
                    "maxLength": 8
                },
                "cpf": {
                    "description": "**Descrição:** Número do Documento Cadastro de Pessoa Física.\n\n**Observação:** Se preenchido, não enviar CNPJ.\n",
                    "type": "string",
                    "title": "CPF",
                    "pattern": "/^\\d{11}$/"
                },
                "cnpj": {
                    "description": "**Descrição:** Número do Cadastro Nacional da Pessoa Jurídica.\n\n**Observação:** Se preenchido, não enviar CPF.\n",
                    "type": "string",
                    "title": "CNPJ",
                    "pattern": "/^\\d{14}$/"
                },
                "nome": {
                    "description": "**Descrição:** Nome do pagador da cobrança. \n\n**Observação:** Necessário preencher o campo CNPJ ou o campo CPF.\n",
                    "type": "string",
                    "title": "Nome",
                    "maxLength": 200
                }
            },
            "required": [
                "cpf",
                "cnpj",
                "nome"
            ]
        }
        """
        return cls(
            nome=data.get("nome"),
            email=data.get("email"),
            logradouro=data.get("logradouro"),
            cidade=data.get("cidade"),
            uf=data.get("uf"),
            cep=data.get("cep"),
            cpf=data.get("cpf"),
            cnpj=data.get("cnpj")
        )