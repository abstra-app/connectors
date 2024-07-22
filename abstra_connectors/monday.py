from typing import Any, List, Optional

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from pydantic.dataclasses import dataclass

MONDAY_URL = "https://api.monday.com/v2"
API_VERSION = "2023-10"

ITEM_FRAGMENT = """
    fragment itemFragment on Item {
        id
        name
        board {
            id
        }
        relative_link
        group {
            title
        }
        column_values {
            value
            text
            column {
                id
                title
                type
            }
        }
    }
"""


class AbstraMondayException(Exception):
    def __init__(self, message: str, original_exception: Optional[Exception] = None):
        self.message = f"Monday Connector Error: {message}.\n{original_exception}\nPlease contact Abstra support."


@dataclass
class SubscriptableDataclass:
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


@dataclass
class ItemsPageDTO(SubscriptableDataclass):
    items: List["ItemDTO"]
    cursor: Optional[str]


@dataclass
class ColumnDTO(SubscriptableDataclass):
    id: str
    title: str
    type: str


@dataclass
class ColumnValueDTO(SubscriptableDataclass):
    value: Optional[str]
    text: Optional[str]
    column: ColumnDTO


@dataclass
class GroupDTO(SubscriptableDataclass):
    title: str


@dataclass
class BoardDTO(SubscriptableDataclass):
    id: str


@dataclass
class ItemDTO(SubscriptableDataclass):
    id: str
    name: str
    relative_link: str
    group: GroupDTO
    column_values: List[ColumnValueDTO]
    board: BoardDTO


class Item:
    id: str
    name: str
    board: BoardDTO
    relative_link: str
    group: GroupDTO
    column_values: List[ColumnValueDTO]
    api: "MondayConnector"

    def __init__(
        self,
        dto: ItemDTO,
        api: "MondayConnector",
    ):
        self.api = api
        self.__dict__.update(dto.__dict__)

    def __str__(self) -> str:
        return str(self.__dict__)

    @property
    def item_id(self):
        return self.id

    def set_column_value(
        self,
        column_title: Optional[str] = None,
        column_id: Optional[str] = None,
        value: Any = None,
    ) -> None:
        if not column_id and not column_title:
            raise AbstraMondayException(
                "Either column_title or column_id args must be provided"
            )

        if column_title:
            for column_value in self.column_values:
                if column_value.column.title == column_title:
                    column_id = column_value.column.id
                    break

        if not column_id:
            raise AbstraMondayException(
                f"Column with title '{column_title}' not found in item '{self.id}'\nColumns found: {[column.column.title for column in self.column_values]}"
            )

        self.api.update_item_column_value(
            item_id=str(self.id),
            column_id=column_id,
            board_id=str(self.board.id),
            value=value,
        )

        self.refetch()

    def get_column_value(self, column_title=None, column_id=None) -> Optional[str]:
        if column_id:
            for column_value in self.column_values:
                if column_value.column.id == column_id:
                    return column_value.text
            raise AbstraMondayException(
                f"Column with id '{column_id}' not found in item '{self.id}'\nColumns found: {[column.column.id for column in self.column_values]}"
            )

        if column_title:
            for column_value in self.column_values:
                if column_value.column.title == column_title:
                    return column_value.text
            raise AbstraMondayException(
                f"Column with title '{column_title}' not found in item '{self.id}'\nColumns found: {[column.column.title for column in self.column_values]}"
            )

        raise AbstraMondayException(
            "Either column_title or column_id args must be provided"
        )

    def refetch(self):
        item = self.api.fetch_item(self.id)
        self.__dict__.update(item.__dict__)


class MondayConnector:
    def __init__(self, api_key: str):
        self.api_key = api_key
        transport = AIOHTTPTransport(
            url=MONDAY_URL,
            headers={"Authorization": api_key, "API-Version": API_VERSION},
        )
        self.client = Client(transport=transport, fetch_schema_from_transport=True)

    def fetch_item_from_url(self, url: str) -> Optional["Item"]:
        def get_item_id_from_url(url: str):
            fragments = url.split("/")

            if fragments[-2] != "pulses":
                return None

            return fragments[-1]

        item_id = get_item_id_from_url(url)

        if not item_id:
            return None

        return self.fetch_item(int(item_id))

    def fetch_item(self, item_id) -> Optional["Item"]:
        query = gql(
            """
            query getItem($itemId: ID!) {
                items(ids: [$itemId]) {
                    ...itemFragment
                }
            }
        """
            + ITEM_FRAGMENT
        )

        params = {"itemId": item_id}

        response = self.client.execute(query, variable_values=params)

        if not response.get("items") and len(response["items"]) == 0:
            return None

        item_dto = response["items"][0]

        try:
            return Item(
                api=self,
                dto=ItemDTO(
                    id=item_dto["id"],
                    name=item_dto["name"],
                    relative_link=item_dto["relative_link"],
                    group=item_dto["group"],
                    column_values=item_dto["column_values"],
                    board=item_dto["board"],
                ),
            )
        except Exception as e:
            raise AbstraMondayException(
                f"Error while validating dto for item '{item_id}'",
                e,
            )

    def get_all_items(self, board_id: str) -> List["Item"]:
        items = []
        cursor = None
        while True:
            items_page = self._get_items_page_dto(board_id, cursor=cursor)
            cursor = items_page.cursor
            items.extend(
                [Item(api=self, dto=item_dto) for item_dto in items_page.items]
            )
            if cursor is None:
                break

        return items

    def _get_items_page_dto(
        self, board_id: str, cursor: Optional[str], limit=250
    ) -> ItemsPageDTO:
        query = gql(
            """
            query getItems($boardId: ID!, $limit: Int!, $cursor: String) {
                boards(ids: [$boardId]) {
                    items_page(limit: $limit, cursor: $cursor) {
                        cursor
                        items {
                            ...itemFragment
                        }
                    }
                }
            }
        """
            + ITEM_FRAGMENT
        )

        params = {"boardId": board_id, "limit": limit, "cursor": cursor}

        response = self.client.execute(query, variable_values=params)

        if not response.get("boards") and len(response["boards"]) == 0:
            raise AbstraMondayException(
                f"Error while fetching items for board '{board_id}'"
            )

        item_dtos = response["boards"][0]["items_page"]["items"]

        items = []

        for item_dto in item_dtos:
            try:
                items.append(
                    ItemDTO(
                        id=item_dto["id"],
                        name=item_dto["name"],
                        relative_link=item_dto["relative_link"],
                        group=item_dto["group"],
                        column_values=item_dto["column_values"],
                        board=item_dto["board"],
                    ),
                )
            except Exception as e:
                raise AbstraMondayException(
                    f"Error while validating dto for item '{item_dto['id']}'", e
                )

        return ItemsPageDTO(
            items=items, cursor=response["boards"][0]["items_page"]["cursor"]
        )

    def update_item_column_value(
        self, board_id: str, column_id: str, item_id: str, value: str
    ):
        query = gql(
            """
            mutation changeColumnValue(
                $boardId: ID!
                $itemId: ID, 
                $columnId: String!, 
                $value: String, 
            ) {
                change_simple_column_value(
                    item_id: $itemId, 
                    column_id: $columnId, 
                    board_id: $boardId,
                    value: $value, 
                ) {
                    id
                }
            }
        """
        )

        params = {
            "itemId": item_id,
            "columnId": column_id,
            "value": value,
            "boardId": board_id,
        }

        return self.client.execute(query, variable_values=params)
