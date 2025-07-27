from pathlib import Path
from shutil import rmtree
from typing import List
from connectors.generators.openapi import generate_openapi_client


def generate_client(schema_name: str, global_params: List[str] = []):
    openapi_json_path = Path(__file__).parent.joinpath("schemas", schema_name)
    assert openapi_json_path.suffix == ".json", (
        f"Unexpected file: {openapi_json_path.name}"
    )
    assert openapi_json_path.is_file(), f"Expected a file: {openapi_json_path.name}"
    assert openapi_json_path.stat().st_size > 0, (
        f"File is empty: {openapi_json_path.name}"
    )

    generate_openapi_client(
        open_api_path=openapi_json_path,
        output_client_path=clients_generated_path.joinpath(
            openapi_json_path.stem
        ).with_suffix(".py"),
        global_params=global_params,
    )


if __name__ == "__main__":
    clients_generated_path = Path(__file__).parent.joinpath("clients_generated")
    if clients_generated_path.exists():
        rmtree(clients_generated_path)

    generate_client("arrecadacao_integrada_ao_pix.json", [])
    generate_client("autorizacao_debito_automatico.json", [])
    generate_client("bb_pay_v1.json", [])
    generate_client("bb_pay_v2.json", [])
    generate_client("cobrancas.json", [])
    generate_client("debitos_veiculantes.json", [])
    generate_client("extratos.json", [])
    generate_client("fundos_de_investimento.json", [])
    generate_client("login_bb.json", [])
    generate_client("pag_bb.json", [])
    generate_client("pagamentos_em_lote.json", [])
    generate_client("pix.json", [])
    generate_client("seguro_credito_protegido.json", [])
    generate_client("seguro_de_itens_pessoais.json", [])
    generate_client("seguro_empresarial.json", [])
    generate_client("seguro_protecao_pessoal.json", [])
    generate_client("seguro_residencial.json", [])
    generate_client("servicos_de_arrecadacao.json", [])
    generate_client("simulacao_de_pagar_boleto.json", [])
    generate_client("validacao_de_contas.json", [])
