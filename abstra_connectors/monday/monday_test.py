import unittest
import os

from abstra_connectors.monday import Item, MondayConnector

SUBDOMAIN = "abstra-cast"
API_KEY = os.environ.get("MONDAY_API_KEY", "")
BOARD_ID = "6255133301"
COLUMNS = [
    {
        "title": "Dropdown",
        "type": "dropdown",
        "options": ["Option 1", "Option 2", "Option 3"],
    },
    {
        "title": "Status",
        "type": "status",
        "options": ["Done", "Working on it", "Stuck", "Not Started"],
    },
    {
        "title": "Date",
        "type": "date",
    },
    {
        "type": "person",
        "title": "Person",
        "options": ["dev@abstra.app"],
    },
]


class TestMondayConnector(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.monday = MondayConnector(API_KEY)

    def test_fetch_all_items(self):
        items = self.monday.get_all_items(BOARD_ID)

        self.assertIsInstance(items, list)
        self.assertGreater(len(items), 0)

    def test_fetch_item(self):
        items = self.monday.get_all_items(BOARD_ID)
        item = self.monday.fetch_item(items[0].id)

        self.assertIsInstance(item, Item)

    def test_fetch_item_from_url(self):
        items = self.monday.get_all_items(BOARD_ID)
        url = f"https://{SUBDOMAIN}.monday.com{items[0].relative_link}"

        item = self.monday.fetch_item_from_url(url)
        self.assertIsInstance(item, Item)

    def test_get_column_value(self):
        items = self.monday.get_all_items(BOARD_ID)
        item = self.monday.fetch_item(items[0].id)

        assert item

        item.get_column_value(column_title="Dropdown")
        item.get_column_value(column_title="Status")
        item.get_column_value(column_title="Date")
        item.get_column_value(column_title="Person")

        expected = {
            "Dropdown": item.column_values[0].text,
            "Status": item.column_values[1].text,
            "Date": item.column_values[2].text,
            "Person": item.column_values[3].text,
        }

        self.assertEqual(
            item.get_column_value(column_title="Dropdown"), expected["Dropdown"]
        )
        self.assertEqual(
            item.get_column_value(column_title="Status"), expected["Status"]
        )
        self.assertEqual(item.get_column_value(column_title="Date"), expected["Date"])
        self.assertEqual(
            item.get_column_value(column_title="Person"), expected["Person"]
        )

    def test_set_column_value_dropdown(self):
        items = self.monday.get_all_items(BOARD_ID)
        item = self.monday.fetch_item(items[0].id)

        assert item

        item.set_column_value(column_title="Dropdown", value="")
        self.assertEqual(item.get_column_value(column_title="Dropdown"), None)

        item.set_column_value(column_title="Dropdown", value=COLUMNS[0]["options"][0])
        self.assertEqual(
            item.get_column_value(column_title="Dropdown"), COLUMNS[0]["options"][0]
        )

    def test_set_column_value_status(self):
        items = self.monday.get_all_items(BOARD_ID)
        item = self.monday.fetch_item(items[0].id)

        assert item

        item.set_column_value(column_title="Status", value=COLUMNS[1]["options"][0])
        self.assertEqual(
            item.get_column_value(column_title="Status"), COLUMNS[1]["options"][0]
        )

        item.set_column_value(column_title="Status", value=COLUMNS[1]["options"][1])
        self.assertEqual(
            item.get_column_value(column_title="Status"), COLUMNS[1]["options"][1]
        )

    def test_set_column_value_date(self):
        items = self.monday.get_all_items(BOARD_ID)
        item = self.monday.fetch_item(items[0].id)

        assert item

        item.set_column_value(column_title="Date", value="")
        self.assertEqual(item.get_column_value(column_title="Date"), "")

        item.set_column_value(column_title="Date", value="2022-12-12")
        self.assertEqual(item.get_column_value(column_title="Date"), "2022-12-12")

    def test_set_column_value_person(self):
        items = self.monday.get_all_items(BOARD_ID)
        item = self.monday.fetch_item(items[0].id)

        assert item

        item.set_column_value(column_title="Person", value="")
        self.assertEqual(item.get_column_value(column_title="Person"), "")

        item.set_column_value(column_title="Person", value=COLUMNS[3]["options"][0])
        self.assertEqual(
            item.get_column_value(column_title="Person"), COLUMNS[3]["options"][0]
        )
