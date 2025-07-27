from typing import List


def snake_case(name: str) -> str:
    """Convert a string to snake_case."""
    import re

    if not name:
        return name
    # Remove leading/trailing whitespace
    name = name.strip()
    # Replace hyphens, spaces, slashes, and dots with underscores
    name = re.sub(r"[-\s/\.]+", "_", name)
    # Handle acronym and camelCase transitions: HTTPResponse -> http_response, HelloWorld -> hello_world
    name = re.sub(
        r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name
    )  # Split acronym from next word
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)  # Split lower/number from upper
    # Lowercase and collapse multiple underscores
    name = re.sub(r"_+", "_", name).lower()
    # Remove leading/trailing underscores
    name = name.strip("_")
    return name


def pascal_case(name: str) -> str:
    """Convert a string to PascalCase."""
    import re

    if not name:
        return name
    # Remove leading/trailing whitespace
    name = name.strip()
    # Replace hyphens, spaces, slashes, and dots with underscores
    name = re.sub(r"[-\s/\.]+", "_", name)
    # Split by underscores and capitalize each part
    parts = name.split("_")
    return "".join(part.capitalize() for part in parts)


def make_method_name(method: str, path_template: str) -> str:
    """Create a method name from the HTTP method and path template."""
    import re

    path_parts = path_template.strip("/").split("/")
    processed_parts = []
    for part in path_parts:
        # Replace all occurrences of {param} with by_param
        def replacer(match):
            return f"by_{match.group(1)}"

        new_part = re.sub(r"\{([^}]+)\}", replacer, part)
        processed_parts.append(new_part)
    method_name = snake_case(f"{method}_{'_'.join(processed_parts)}")
    return method_name


def indent(lines: List[str]) -> List[str]:
    """Indent each line in the list by four spaces."""
    return [f"    {line}" for line in lines]
