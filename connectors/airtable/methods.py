import os
import requests
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict


API_TOKEN = os.getenv("CONNECTORS_AIRTABLE_TOKEN")


@dataclass
class AirtableRecord:
    id: str
    fields: dict
    created_time: datetime

    @staticmethod
    def from_dto(dto: dict):
        return AirtableRecord(
            id=dto["id"],
            fields=dto["fields"],
            created_time=datetime.fromisoformat(dto["createdTime"]),
        )


class AirtableConnector:
    def __init__(self):
        self.api_token = API_TOKEN
        self.requests = requests

    def make_request(
        self,
        *,
        base_id: str,
        table_name: str,
        method: str,
        record_id: str = None,
        data: Optional[dict] = None,
        query_params: Optional[Dict[str, List[str]]] = None,
    ) -> dict:
        url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
        if record_id:
            url += f"/{record_id}"

        base_params = dict(
            method=method,
            url=url,
        )

        if query_params is not None:
            base_params["params"] = query_params

        if data is None:
            base_params["headers"] = {
                "Authorization": f"Bearer {self.api_token}",
            }
        else:
            base_params["headers"] = {
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json",
            }
            base_params["json"] = data

        response = self.requests.request(**base_params)

        return response.json()

    def create_record(self, base_id: str, table_name: str, data) -> str:
        data = {"fields": data}
        response = self.make_request(
            base_id=base_id, table_name=table_name, method="POST", data=data
        )
        return AirtableRecord.from_dto(response)

    def create_records(self, base_id: str, table_name: str, data) -> str:
        data = {"records": [{"fields": record} for record in data]}
        response = self.make_request(
            base_id=base_id, table_name=table_name, method="POST", data=data
        )
        return [AirtableRecord.from_dto(record) for record in response["records"]]

    def update_record(
        self, base_id: str, table_name: str, record_id: str, change: dict
    ) -> None:
        data = {"fields": change}
        self.make_request(
            base_id=base_id,
            table_name=table_name,
            method="PATCH",
            record_id=record_id,
            data=data,
        )

    def update_records(self, base_id: str, table_name: str, updates: dict) -> None:
        data = {"records": [{"fields": v, "id": k} for k, v in updates.items()]}
        self.make_request(
            base_id=base_id, table_name=table_name, method="PATCH", data=data
        )

    def upsert_records(
        self, base_id: str, table_name: str, field_name: str, upserts: dict
    ):
        data = {
            "performUpsert": {"fieldsToMergeOn": [field_name]},
            "records": [{"fields": {**v, field_name: k}} for k, v in upserts.items()],
        }
        self.make_request(
            base_id=base_id,
            table_name=table_name,
            method="PATCH",
            record_id=None,
            data=data,
        )

    def delete_record(self, base_id: str, table_name: str, record_id: str) -> None:
        self.make_request(
            base_id=base_id, table_name=table_name, method="DELETE", record_id=record_id
        )

    def delete_records(self, base_id: str, table_name: str, ids: List[str]):
        self.make_request(
            base_id=base_id,
            table_name=table_name,
            method="DELETE",
            query_params={"records": ids},
        )

    def get_record(self, base_id: str, table_name: str, record_id: str) -> dict:
        return self.make_request(
            base_id=base_id, table_name=table_name, method="GET", record_id=record_id
        )

    def list_records(self, base_id: str, table_name: str):
        records = self.make_request(
            base_id=base_id, table_name=table_name, method="GET"
        )["records"]
        for record in records:
            yield AirtableRecord.from_dto(record)


default_connector = AirtableConnector()


def create_record(base_id: str, table_name: str, data) -> str:
    return default_connector.create_record(base_id, table_name, data)


def create_records(base_id: str, table_name: str, data) -> str:
    return default_connector.create_records(base_id, table_name, data)


def update_record(base_id: str, table_name: str, record_id: str, change: dict) -> None:
    return default_connector.update_record(base_id, table_name, record_id, change)


def update_records(base_id: str, table_name: str, updates: dict) -> None:
    return default_connector.update_records(base_id, table_name, updates)


def upsert_records(base_id: str, table_name: str, field_name: str, upserts: dict):
    return default_connector.upsert_records(base_id, table_name, field_name, upserts)


def delete_record(base_id: str, table_name: str, record_id: str) -> None:
    return default_connector.delete_record(base_id, table_name, record_id)


def delete_records(base_id: str, table_name: str, ids: List[str]):
    return default_connector.delete_records(base_id, table_name, ids)


def get_record(base_id: str, table_name: str, record_id: str) -> dict:
    return default_connector.get_record(base_id, table_name, record_id)


def list_records(base_id: str, table_name: str):
    return default_connector.list_records(base_id, table_name)
