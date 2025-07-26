from dataclasses import dataclass
import json
from os import PathLike

@dataclass
class Credentials:
    client_id: str
    client_secret: str
    token: str

    @classmethod
    def from_json_file(cls, file_path: PathLike = ".env"):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return cls(
                client_id=data["client_id"],
                client_secret=data["client_secret"],
                token=data["token"]
            )