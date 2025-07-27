def python_type_from_json_type(json_type: str, required: bool) -> str:
    """Convert a JSON schema type to a Python type."""
    type_mapping = {
        "string": "str",
        "number": "float",
        "integer": "int",
        "boolean": "bool",
        "array": "list",
        "object": "dict",
    }
    type_code = type_mapping.get(json_type, json_type)
    if required:
        return type_code
    else:
        return f"Optional[{type_code}]"
