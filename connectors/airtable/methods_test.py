from unittest import TestCase
from unittest.mock import Mock
from .methods import AirtableConnector
from requests import Response


class TestAirtableConnector(TestCase):
    def setUp(self) -> None:
        self.connector = AirtableConnector()
        self.connector.api_token = "test_token"
        self.connector.requests = Mock()
        self.connector.requests.request.return_value = Response()
        self.connector.requests.request.return_value.headers[
            "Content-Type"
        ] = "application/json"

    def test_create_records(self):
        self.connector.requests.request.return_value._content = b"""{
            "records": [
                {
                "createdTime": "2022-09-12T21:03:48.000Z",
                "fields": {
                    "Address": "333 Post St",
                    "Name": "Union Square",
                    "Visited": true
                },
                "id": "rec560UJdUtocSouk"
                },
                {
                "createdTime": "2022-09-12T21:03:48.000Z",
                "fields": {
                    "Address": "1 Ferry Building",
                    "Name": "Ferry Building"
                },
                "id": "rec3lbPRG4aVqkeOQ"
                }
            ]
        }"""
        self.connector.create_records(
            "base_id",
            "table_name",
            [
                {"Address": "333 Post St", "Name": "Union Square", "Visited": True},
                {"Address": "1 Ferry Building", "Name": "Ferry Building"},
            ],
        )
        self.connector.requests.request.assert_called_with(
            method="POST",
            url="https://api.airtable.com/v0/base_id/table_name",
            headers={
                "Authorization": "Bearer test_token",
                "Content-Type": "application/json",
            },
            json={
                "records": [
                    {
                        "fields": {
                            "Address": "333 Post St",
                            "Name": "Union Square",
                            "Visited": True,
                        }
                    },
                    {
                        "fields": {
                            "Address": "1 Ferry Building",
                            "Name": "Ferry Building",
                        }
                    },
                ]
            },
        )

    def test_create_record(self):
        self.connector.requests.request.return_value._content = b"""{
            "createdTime": "2022-09-12T21:03:48.000Z",
            "fields": {
                "Address": "333 Post St",
                "Name": "Union Square",
                "Visited": true
            },
            "id": "rec560UJdUtocSouk"
        }"""

        self.connector.create_record(
            "base_id",
            "table_name",
            {"Address": "333 Post St", "Name": "Union Square", "Visited": True},
        )
        self.connector.requests.request.assert_called_with(
            method="POST",
            url="https://api.airtable.com/v0/base_id/table_name",
            headers={
                "Authorization": "Bearer test_token",
                "Content-Type": "application/json",
            },
            json={
                "fields": {
                    "Address": "333 Post St",
                    "Name": "Union Square",
                    "Visited": True,
                }
            },
        )

    def test_list_records(self):
        self.connector.requests.request.return_value._content = b"""{
            "records": [
                {
                    "createdTime": "2022-09-12T21:03:48.000Z",
                    "fields": {
                        "Address": "333 Post St",
                        "Name": "Union Square",
                        "Visited": true
                    },
                        "id": "rec560UJdUtocSouk"
                    },
                {
                    "createdTime": "2022-09-12T21:03:48.000Z",
                    "fields": {
                        "Address": "1 Ferry Building",
                        "Name": "Ferry Building"
                    },
                    "id": "rec3lbPRG4aVqkeOQ"
                }
            ]
        }"""

        yield from self.connector.list_records("base_id", "table_name")

        self.connector.requests.request.assert_called_with(
            method="GET",
            url="https://api.airtable.com/v0/base_id/table_name",
            headers={"Authorization": "Bearer test_token"},
        )

    def test_get_record(self):
        self.connector.requests.request.return_value._content = b"""{
            "createdTime": "2022-09-12T21:03:48.000Z",
            "fields": {
                "Address": "333 Post St",
                "Name": "Union Square",
                "Visited": true
            },
            "id": "rec560UJdUtocSouk"
        }"""

        self.connector.get_record("base_id", "table_name", "rec560UJdUtocSouk")
        self.connector.requests.request.assert_called_with(
            method="GET",
            url="https://api.airtable.com/v0/base_id/table_name/rec560UJdUtocSouk",
            headers={"Authorization": "Bearer test_token"},
        )

    def test_update_records(self):
        self.connector.requests.request.return_value._content = b"""{
            "records": [
                {
                "createdTime": "2022-09-12T21:03:48.000Z",
                "fields": {
                    "Address": "501 Twin Peaks Blvd",
                    "Name": "Twin Peaks",
                    "Visited": true
                },
                "id": "rec560UJdUtocSouk"
                },
                {
                "createdTime": "2022-09-12T21:03:48.000Z",
                "fields": {
                    "Address": "1 Ferry Building",
                    "Name": "Ferry Building",
                    "Visited": true
                },
                "id": "rec3lbPRG4aVqkeOQ"
                }
            ]
        }"""

        self.connector.update_records(
            "base_id",
            "table_name",
            {
                "rec560UJdUtocSouk": {
                    "Address": "501 Twin Peaks Blvd",
                    "Name": "Twin Peaks",
                    "Visited": True,
                },
                "rec3lbPRG4aVqkeOQ": {"Visited": True},
            },
        )
        self.connector.requests.request.assert_called_with(
            method="PATCH",
            url="https://api.airtable.com/v0/base_id/table_name",
            headers={
                "Authorization": "Bearer test_token",
                "Content-Type": "application/json",
            },
            json={
                "records": [
                    {
                        "fields": {
                            "Address": "501 Twin Peaks Blvd",
                            "Name": "Twin Peaks",
                            "Visited": True,
                        },
                        "id": "rec560UJdUtocSouk",
                    },
                    {"fields": {"Visited": True}, "id": "rec3lbPRG4aVqkeOQ"},
                ]
            },
        )

    def test_update_records_upsert(self):
        self.connector.requests.request.return_value._content = b"""
            {
            "createdRecords": [
                "recsHMqsp3GEm3lEi"
            ],
            "records": [
                {
                "createdTime": "2022-09-12T21:03:48.000Z",
                "fields": {
                    "Address": "501 Twin Peaks Blvd",
                    "Name": "Twin Peaks",
                    "Visited": true
                },
                "id": "rec560UJdUtocSouk"
                },
                {
                "createdTime": "2022-11-15T01:02:04.400Z",
                "fields": {
                    "Name": "New Park",
                    "Visited": true
                },
                "id": "recsHMqsp3GEm3lEi"
                }
            ],
            "updatedRecords": [
                "rec560UJdUtocSouk"
            ]
            }
        """

        self.connector.upsert_records(
            "base_id",
            "table_name",
            "Name",
            {
                "Twin Peaks": {"Address": "501 Twin Peaks Blvd", "Visited": True},
                "New Park": {"Visited": True},
            },
        )

        self.connector.requests.request.assert_called_with(
            method="PATCH",
            url="https://api.airtable.com/v0/base_id/table_name",
            headers={
                "Authorization": "Bearer test_token",
                "Content-Type": "application/json",
            },
            json={
                "performUpsert": {"fieldsToMergeOn": ["Name"]},
                "records": [
                    {
                        "fields": {
                            "Address": "501 Twin Peaks Blvd",
                            "Name": "Twin Peaks",
                            "Visited": True,
                        }
                    },
                    {"fields": {"Name": "New Park", "Visited": True}},
                ],
            },
        )

    def test_update_record(self):
        self.connector.requests.request.return_value._content = b"""{
            "createdTime": "2022-09-12T21:03:48.000Z",
            "fields": {
                "Address": "1 Ferry Building",
                "Name": "Ferry Building",
                "Visited": true
            },
            "id": "rec3lbPRG4aVqkeOQ"
            }
        """

        self.connector.update_record(
            "base_id",
            "table_name",
            "record_id",
            {"Address": "1 Ferry Building", "Name": "Ferry Building", "Visited": True},
        )

        self.connector.requests.request.assert_called_with(
            method="PATCH",
            url="https://api.airtable.com/v0/base_id/table_name/record_id",
            headers={
                "Authorization": "Bearer test_token",
                "Content-Type": "application/json",
            },
            json={
                "fields": {
                    "Address": "1 Ferry Building",
                    "Name": "Ferry Building",
                    "Visited": True,
                }
            },
        )

    def test_delete_records(self):
        self.connector.requests.request.return_value._content = b"""{
            "records": [
                {
                "deleted": true,
                "id": "rec560UJdUtocSouk"
                },
                {
                "deleted": true,
                "id": "rec3lbPRG4aVqkeOQ"
                }
            ]
        }"""

        self.connector.delete_records(
            "base_id", "table_name", ["rec560UJdUtocSouk", "rec3lbPRG4aVqkeOQ"]
        )

        self.connector.requests.request.assert_called_with(
            method="DELETE",
            url="https://api.airtable.com/v0/base_id/table_name",
            headers={"Authorization": "Bearer test_token"},
            params={"records": ["rec560UJdUtocSouk", "rec3lbPRG4aVqkeOQ"]},
        )

    def test_delete_record(self):
        self.connector.requests.request.return_value._content = b"""{
            "deleted": true,
            "id": "rec560UJdUtocSouk"
        }"""

        self.connector.delete_record("base_id", "table_name", "record_id")

        self.connector.requests.request.assert_called_with(
            method="DELETE",
            url="https://api.airtable.com/v0/base_id/table_name/record_id",
            headers={"Authorization": "Bearer test_token"},
        )
