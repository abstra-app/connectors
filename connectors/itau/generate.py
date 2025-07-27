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

    generate_client("account_statement.json", ["Authorization"])
    generate_client("boletos_consulta.json", ["x_itau_apikey"])
    generate_client("boletos_emissao.json", ["x_itau_apikey"])
    generate_client("boletos_v3.json", ["x_itau_apikey"])
    generate_client("boletos.json", ["x_itau_apikey"])
    generate_client("pix_recebimentos_conciliacoes_v2.json", ["x_itau_apikey"])
    generate_client("pix_recebimentos.json", ["x_itau_apikey"])
    generate_client("pixautomatico_v1.json", ["x_itau_apikey"])
    generate_client("qrcode_pix_automatico_v1.json", ["x_itau_apikey"])
    generate_client("sispag.json", ["x_itau_apikey"])
