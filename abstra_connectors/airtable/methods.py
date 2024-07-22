import os
import requests

API_TOKEN = os.getenv("CONNECTORS_AIRTABLE_TOKEN")

def airtable_insert(base_id: str, table_name: str, data: dict) -> str:
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
    }

    response = requests.post(url, headers=headers, data=data)

    return response.json()
