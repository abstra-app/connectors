from pathlib import Path
import json
from sys import argv
from typing import List
from ..utils.string import snake_case, make_method_name, indent, pascal_case
from ..utils.json_schema import python_type_from_json_type
import functools


def resolve(file_data: dict, local_data: dict):
    if "$ref" in local_data:
        ref_path = local_data["$ref"]
        assert isinstance(ref_path, str), "$ref must be a string"
        if ref_path.startswith("#/"):
            parts = [
                part.replace("~1", "/").replace("~0", "~")
                for part in ref_path.split("/")[1:]
            ]
            result_data = file_data
            for part in parts:
                if not part:
                    continue
                if isinstance(result_data, dict):
                    result_data = result_data.get(part)
                elif isinstance(result_data, list):
                    result_data = result_data[int(part)]
            return result_data
    else:
        return local_data


def generate_openapi_client(
    open_api_path: Path, output_client_path: Path, global_params: List[str] = []
):
    api_class_name = pascal_case(open_api_path.stem)
    open_api_data = json.loads(open_api_path.read_text("utf-8"))
    global_params_code = ", ".join(
        f"{snake_case(param)}: str" for param in global_params
    )
    code_parts = [
        '"""',
        open_api_data["info"].get("title", "")
        + " v"
        + open_api_data["info"].get("version", ""),
        open_api_data["info"].get("description", ""),
        '"""',
        "import requests",
        "from typing import Optional",
        "",
        "",
        f"class {api_class_name}Client:",
        *indent(
            [
                "base_url: str",
                *[f"{snake_case(param)}: str" for param in global_params],
                "",
                f"def __init__(self, base_url: str, {global_params_code}):",
                *indent(
                    [
                        "self.base_url = base_url.rstrip('/')",
                        *[
                            f"self.{snake_case(param)} = {snake_case(param)}"
                            for param in global_params
                        ],
                    ]
                ),
            ]
        ),
    ]
    assert isinstance(open_api_data, dict), "OpenAPI data must be a dictionary"
    for path_template, path_dict in open_api_data.get("paths", {}).items():
        path_dict = resolve(open_api_data, path_dict)
        assert isinstance(path_dict, dict), f"Path {path_template} must be a dictionary"
        for method, method_dict in path_dict.items():
            if method not in ["get", "post", "put", "patch", "delete", "options"]:
                continue
            method_dict = resolve(open_api_data, method_dict)
            assert isinstance(method_dict, dict), (
                f"Method {method} in path {path_template} must be a dictionary"
            )
            method_name = make_method_name(method, path_template)
            parameters = method_dict.get("parameters", []) + path_dict.get(
                "parameters", []
            )
            assert isinstance(parameters, list), "Parameters must be a list"
            if method_dict.get("requestBody"):
                assert "content" in method_dict["requestBody"], (
                    "Request body must have content"
                )
                assert "application/json" in method_dict["requestBody"]["content"], (
                    "Request body must have application/json content"
                )
                parameters.append(
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": method_dict["requestBody"]["content"][
                            "application/json"
                        ]["schema"],
                    }
                )
            method_params = [
                f"{snake_case(parameter['name'])}: {python_type_from_json_type(resolve(open_api_data, parameter['schema']).get('type', 'string'), parameter.get('required', False))} = None"
                for parameter in map(
                    lambda p: resolve(open_api_data, p),
                    parameters,
                )
            ]
            method_params_code = ", ".join(method_params)
            function_code = "\n".join(
                indent(
                    [
                        f"def {method_name}(self, *, {method_params_code}):"
                        if method_params_code
                        else f"def {method_name}(self):",
                        *indent(
                            [
                                '"""',
                                method_dict.get(
                                    "description", "No description provided."
                                ).strip(),
                                "",
                                "Args:",
                                *indent(
                                    [
                                        f"@param {snake_case(parameter['name'])}: {parameter.get('description', 'No description provided.')}"
                                        for parameter in map(
                                            lambda p: resolve(open_api_data, p),
                                            parameters,
                                        )
                                    ]
                                ),
                                '"""',
                                *functools.reduce(
                                    lambda a, b: a + b,
                                    [
                                        [
                                            f"if {snake_case(global_param)} is None:",
                                            *indent(
                                                [
                                                    f"{snake_case(global_param)} = self.{snake_case(global_param)}"
                                                ]
                                            ),
                                        ]
                                        for global_param in global_params
                                    ],
                                    [],
                                ),
                                "query = {}",
                                *functools.reduce(
                                    lambda a, b: a + b,
                                    [
                                        [
                                            f"if {snake_case(parameter['name'])} is not None:",
                                            *indent(
                                                [
                                                    f"query[{repr(parameter['name'])}] = {snake_case(parameter['name'])}"
                                                ]
                                            ),
                                        ]
                                        for parameter in map(
                                            lambda p: resolve(open_api_data, p),
                                            parameters,
                                        )
                                        if parameter.get("in") == "query"
                                    ],
                                    [],
                                ),
                                "headers = {}",
                                *functools.reduce(
                                    lambda a, b: a + b,
                                    [
                                        [
                                            f"if {snake_case(header['name'])} is not None:",
                                            *indent(
                                                [
                                                    f"headers[{repr(header['name'])}] = {snake_case(header['name'])}"
                                                ]
                                            ),
                                        ]
                                        for header in map(
                                            lambda p: resolve(open_api_data, p),
                                            parameters,
                                        )
                                        if header.get("in") == "header"
                                    ],
                                    [],
                                ),
                                "path_params = {}",
                                *functools.reduce(
                                    lambda a, b: a + b,
                                    [
                                        [
                                            f"if {snake_case(parameter['name'])} is not None:",
                                            *indent(
                                                [
                                                    f"path_params[{repr(parameter['name'])}] = {snake_case(parameter['name'])}"
                                                ]
                                            ),
                                        ]
                                        for parameter in map(
                                            lambda p: resolve(open_api_data, p),
                                            parameters,
                                        )
                                        if parameter.get("in") == "path"
                                    ],
                                    [],
                                ),
                                f"path_rendered = {repr(path_template)}.format(**path_params)",
                                f"response = requests.{method}(",
                                *indent(
                                    [
                                        "self.base_url + path_rendered,",
                                        "params=query,",
                                        "headers=headers,",
                                        *[
                                            "json=body"
                                            for p in parameters
                                            if p.get("in") == "body"
                                        ],
                                    ]
                                ),
                                ")",
                                "response.raise_for_status()",
                                "return response.json()",
                            ]
                        ),
                    ]
                )
            )
            code_parts.append(function_code)
    output_client_path.parent.mkdir(parents=True, exist_ok=True)
    with output_client_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(code_parts))


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python openapi.py <openapi_path> <output_client_path>")
        exit(1)
    open_api_path = Path(argv[1])
    output_client_path = Path(argv[2])
    generate_openapi_client(open_api_path, output_client_path)
