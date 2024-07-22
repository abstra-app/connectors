import os
import pathlib
import re

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

# The list of requirements
REQUIREMENTS = (HERE / "requirements.txt").read_text(encoding="utf-8").split("\n")

# Version
VERSION_FILE = HERE / "VERSION"
if VERSION_FILE.exists():
    VERSION = VERSION_FILE.read_text(encoding="utf-8").strip()
else:
    regex = r"^v(\d+\.\d+\.\d+)$"
    TAG = os.getenv("TAG", "v0.0.0")
    if not TAG or not re.search(regex, TAG):
        raise ValueError("TAG environment variable must be in the format v1.2.3")

    match = re.search(regex, TAG)
    VERSION = match.group(1) if match else "0.0.0"

setup(
    name="abstra-connectors",
    license="MIT",
    version=VERSION,
    description="Abstra Connectors",
    python_requires=">=3.8, <4",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abstra-app/abstra-connectors",
    packages=find_packages(exclude=["tests"]),
    install_requires=REQUIREMENTS,
)