from dataclasses import dataclass
import json
from os import PathLike
import requests
from pathlib import Path


@dataclass
class Credentials:
    client_id: str
    client_secret: str

    @classmethod
    def from_json_file(cls, file_path: PathLike = ".env"):
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Credentials file not found: {file_path}")
        with open(file_path, "r") as file:
            data = json.load(file)
            return cls(
                client_id=data["client_id"],
                client_secret=data["client_secret"],
            )

    def get_token(
        self, token_url: str = "https://sandbox.devportal.itau.com.br/api/oauth/jwt"
    ):
        response = requests.post(
            token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        )

        response.raise_for_status()

        token_data = response.json()

        @dataclass
        class TokenResponse:
            access_token: str
            token_type: str
            expires_in: int
            active: bool
            scope: str

        return TokenResponse(**token_data)
