# API Boletos v3 - Itaú

Este módulo implementa o cliente para a API Boletos v3 do Itaú, que permite gerenciar boletos, francesas e notificações de boletos.

## Características

- **Datas**: Todas as datas são armazenadas como `datetime.date`
- **Valores monetários**: Todos os valores monetários são armazenados como `int` com sufixo `_cents` (centavos)
- **Parsing automático**: Conversão automática de strings para tipos apropriados
- **Tratamento de erros**: Tratamento consistente de erros da API

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `sandbox.json` com suas credenciais:

```json
{
    "client_id": "seu-client-id",
    "client_secret": "seu-client-secret"
}
```

## Uso Básico

```python
from connectors.itau.api.boletos_v3.client import BoletosV3Client
from connectors.itau.utils.auth import Credentials
from datetime import date

# Configurar credenciais
creds = Credentials.from_json_file('sandbox.json')
client = BoletosV3Client(creds=creds)

# Consultar francesas
francesas = client.get_francesas(
    agencia="1500",
    conta="0001560",
    dac="1"
)

# Consultar boletos
boletos = client.get_boletos_by_date_range(
    data_inicial=date(2024, 1, 1),
    data_final=date(2024, 12, 31),
    id_beneficiario="15000015601"
)

# Criar notificação de boleto
notificacao = client.create_notificacao_boleto(
    id_beneficiario="15000015601",
    webhook_url="https://seu-webhook.com",
    webhook_client_id="client-id",
    webhook_client_secret="client-secret",
    tipos_notificacoes=["BAIXA_EFETIVA", "BAIXA_OPERACIONAL"],
    valor_minimo_cents=10000  # 100 reais em centavos
)
```

## Endpoints Disponíveis

### Francesas

- `get_francesas()` - Lista francesas disponíveis
- `get_francesa_movimentacoes()` - Movimentações de uma francesa
- `get_francesa_movimentacoes_resumidas()` - Movimentações resumidas

### Boletos

- `get_boletos()` - Consulta boletos com filtros
- `get_boletos_by_date_range()` - Consulta boletos por período (método auxiliar)

### Notificações

- `post_notificacao_boletos()` - Cria notificação
- `get_notificacoes_boleto()` - Lista notificações
- `patch_notificacao_boleto()` - Atualiza notificação
- `delete_notificacao_boleto()` - Remove notificação
- `create_notificacao_boleto()` - Método auxiliar para criar notificação
- `update_notificacao_boleto()` - Método auxiliar para atualizar notificação

## Estruturas de Dados

### Boleto

```python
@dataclass
class Boleto:
    nome_pagador: Optional[str]
    numero_cpf_cnpj_pagador: Optional[str]
    data_emissao: Optional[date]
    data_vencimento: Optional[date]
    valor_titulo_cents: Optional[int]  # Valor em centavos
    valor_pago_total_cents: Optional[int]  # Valor em centavos
    # ... outros campos
```

### Posicao

```python
@dataclass
class Posicao:
    data_posicao: date
    posicao_anterior: Optional[Baixas]
    entradas: Optional[Baixas]
    baixas: Optional[Baixas]
    # ... outros campos
```

### Baixas

```python
@dataclass
class Baixas:
    valor_cents: int  # Valor em centavos
    quantidade: float
```

## Tratamento de Erros

A API retorna exceções específicas para diferentes códigos de erro:

```python
try:
    response = client.get_boletos(...)
except Exception as e:
    print(f"Erro: {e}")
```

## Testes

Execute os testes com:

```bash
python -m pytest connectors/itau/api/boletos_v3/sandbox_test.py -v
```

## Exemplos de Uso

### Consulta de Boletos com Filtros

```python
boletos = client.get_boletos(
    data_inicial="2024-01-01T00:00:00.000Z",
    data_final="2024-12-31T23:59:59.999Z",
    id_beneficiario="15000015601",
    nome_pagador="João Silva",
    valor_titulo_inicial=100.0,
    valor_titulo_final=1000.0
)
```

### Criação de Notificação com OAuth

```python
notificacao = client.create_notificacao_boleto(
    id_beneficiario="15000015601",
    webhook_url="https://api.exemplo.com/webhook",
    webhook_client_id="oauth-client-id",
    webhook_client_secret="oauth-client-secret",
    webhook_oauth_url="https://auth.exemplo.com/oauth",
    webhook_oauth_scope="boletos-notificacao",
    tipos_notificacoes=["BAIXA_EFETIVA"],
    valor_minimo_cents=5000  # 50 reais em centavos
)
```

### Atualização de Notificação

```python
client.update_notificacao_boleto(
    id_notificacao_boleto="12345",
    webhook_url="https://novo-webhook.com",
    valor_minimo_cents=7500  # 75 reais em centavos
)
``` 