from typing import Optional, List
import requests
import os
from dataclasses import dataclass


@dataclass
class SlackPostMessageResponse:
    ok: bool
    channel: str
    ts: str
    message: dict

    @staticmethod
    def from_json(json: dict):
        return SlackPostMessageResponse(
            ok=json["ok"],
            channel=json["channel"],
            ts=json["ts"],
            message=json["message"],
        )

    def reply(self, msg: str) -> "SlackPostMessageResponse":
        return send_message(msg, self.channel, self.ts)


def _is_email(channel: str) -> bool:
    return "@" in channel


def _get_user_id_from_email(email: str) -> str:
    token = os.getenv("SLACK_BOT_TOKEN")
    if token is None:
        raise Exception("SLACK_BOT_TOKEN env var is not set")

    response = requests.get(
        "https://slack.com/api/users.lookupByEmail",
        params={"email": email},
        headers={"Authorization": "Bearer " + token},
    )

    return response.json()["user"]["id"]


def user_link(user_id: str) -> str:
    if _is_email(user_id):
        user_id = _get_user_id_from_email(user_id)
    return f"<@{user_id}>"


def send_message(
    msg: str, channel: Optional[str] = None, thread_ts: Optional[str] = None
) -> SlackPostMessageResponse:
    if channel is None:
        channel = os.getenv("SLACK_CHANNEL")

    if channel is None:
        raise Exception("channel not set")

    if _is_email(channel):
        channel = _get_user_id_from_email(channel)

    token = os.getenv("SLACK_BOT_TOKEN")
    if token is None:
        raise Exception("SLACK_BOT_TOKEN env var is not set")

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        json={
            "channel": channel,
            "text": msg,
            **({"thread_ts": thread_ts} if thread_ts else {}),
        },
        headers={
            "Authorization": "Bearer " + token,
            "Content-type": "application/json; charset=utf-8",
        },
    )

    response.raise_for_status()
    return SlackPostMessageResponse.from_json(response.json())


@dataclass
class SlackMessage:
    user: str
    text: str
    thread_ts: str
    reply_count: int
    subscribed: bool
    last_read: str
    unread_count: int
    ts: str

    @staticmethod
    def from_dict(json: dict):
        return SlackMessage(
            user=json["user"],
            text=json["text"],
            thread_ts=json["thread_ts"],
            reply_count=json["reply_count"],
            subscribed=json["subscribed"],
            last_read=json["last_read"],
            unread_count=json["unread_count"],
            ts=json["ts"],
        )


@dataclass
class SlackReply:
    user: str
    text: str
    thread_ts: str
    parent_user_id: str
    ts: str

    @staticmethod
    def from_dict(json: dict):
        return SlackReply(
            user=json["user"],
            text=json["text"],
            thread_ts=json["thread_ts"],
            parent_user_id=json["parent_user_id"],
            ts=json["ts"],
        )


@dataclass
class SlackGetMessageResponse:
    messages: List[SlackMessage]
    has_more: bool
    ok: bool
    response_metadata: dict

    @staticmethod
    def from_dict(json: dict):
        return SlackGetMessageResponse(
            messages=[SlackMessage.from_dict(msg) for msg in json["messages"]],
            has_more=json["has_more"],
            ok=json["ok"],
            response_metadata=json["response_metadata"],
        )


def get_messages(
    *,
    channel: Optional[str] = None,
    ts: str,
    cursor: Optional[str] = None,
    include_all_metadata: Optional[bool] = None,
    inclusive: Optional[bool] = None,
    latest: Optional[str] = None,
    limit: Optional[int] = None,
    oldest: Optional[str] = None,
) -> List[dict]:
    if channel is None:
        channel = os.getenv("SLACK_CHANNEL")
    if channel is None:
        raise Exception("channel not set")
    token = os.getenv("SLACK_BOT_TOKEN")
    if token is None:
        raise Exception("SLACK_BOT_TOKEN env var is not set")

    response = requests.get(
        "https://slack.com/api/conversations.replies",
        params={
            "channel": channel,
            "ts": ts,
            **({"cursor": cursor} if cursor else {}),
            **(
                {"include_all_metadata": include_all_metadata}
                if include_all_metadata
                else {}
            ),
            **({"inclusive": inclusive} if inclusive else {}),
            **({"latest": latest} if latest else {}),
            **({"limit": limit} if limit else {}),
            **({"oldest": oldest} if oldest else {}),
        },
        headers={"Authorization": "Bearer " + token},
    )
    response.raise_for_status()

    if not response.json()["ok"]:
        raise Exception(response.json()["error"])

    return response.json()["messages"]


@dataclass
class SlackUser:
    id: str
    team_id: str
    name: str
    deleted: bool
    color: str
    real_name: str
    tz: str
    tz_label: str
    tz_offset: int
    profile_avatar_hash: str
    profile_status_text: str
    profile_status_emoji: str
    profile_real_name: str
    profile_display_name: str
    profile_real_name_normalized: str
    profile_display_name_normalized: str
    profile_email: str
    profile_image_original: str
    profile_image_24: str
    profile_image_32: str
    profile_image_48: str
    profile_image_72: str
    profile_image_192: str
    profile_image_512: str
    is_admin: bool
    is_owner: bool
    is_primary_owner: bool
    is_restricted: bool
    is_ultra_restricted: bool
    is_bot: bool
    updated: int
    is_app_user: bool
    has_2fa: bool

    @staticmethod
    def from_dict(json: dict):
        return SlackUser(
            id=json["id"],
            team_id=json["team_id"],
            name=json["name"],
            deleted=json["deleted"],
            color=json["color"],
            real_name=json["real_name"],
            tz=json["tz"],
            tz_label=json["tz_label"],
            tz_offset=json["tz_offset"],
            profile_avatar_hash=json["profile"].get("avatar_hash", ""),
            profile_status_text=json["profile"].get("status_text", ""),
            profile_status_emoji=json["profile"].get("status_emoji", ""),
            profile_real_name=json["profile"].get("real_name", ""),
            profile_display_name=json["profile"].get("display_name", ""),
            profile_real_name_normalized=json["profile"].get(
                "real_name_normalized", ""
            ),
            profile_display_name_normalized=json["profile"].get(
                "display_name_normalized", ""
            ),
            profile_email=json["profile"].get("email", ""),
            profile_image_original=json["profile"].get("image_original", ""),
            profile_image_24=json["profile"].get("image_24", ""),
            profile_image_32=json["profile"].get("image_32", ""),
            profile_image_48=json["profile"].get("image_48", ""),
            profile_image_72=json["profile"].get("image_72", ""),
            profile_image_192=json["profile"].get("image_192", ""),
            profile_image_512=json["profile"].get("image_512", ""),
            is_admin=json["is_admin"],
            is_owner=json["is_owner"],
            is_primary_owner=json["is_primary_owner"],
            is_restricted=json["is_restricted"],
            is_ultra_restricted=json["is_ultra_restricted"],
            is_bot=json["is_bot"],
            updated=json["updated"],
            is_app_user=json["is_app_user"],
            has_2fa=json.get("has_2fa"),
        )


def get_user(user_id: str) -> SlackUser:
    token = os.getenv("SLACK_BOT_TOKEN")
    if token is None:
        raise Exception("SLACK_BOT_TOKEN env var is not set")

    response = requests.get(
        "https://slack.com/api/users.info",
        params={"user": user_id},
        headers={"Authorization": "Bearer " + token},
    )
    response.raise_for_status()

    if not response.json()["ok"]:
        raise Exception(response.json()["error"])

    return SlackUser.from_dict(response.json()["user"])


@dataclass
class SlackMe:
    id: str
    name: str
    team_id: str
    team_name: str

    @staticmethod
    def from_dict(json: dict):
        return SlackMe(
            id=json["user_id"],
            name=json["user"],
            team_id=json["team_id"],
            team_name=json["team"],
        )


def get_me():
    token = os.getenv("SLACK_BOT_TOKEN")
    if token is None:
        raise Exception("SLACK_BOT_TOKEN env var is not set")

    response = requests.get(
        "https://slack.com/api/auth.test",
        headers={"Authorization": "Bearer " + token},
    )
    response.raise_for_status()

    if not response.json()["ok"]:
        raise Exception(response.json()["error"])

    return SlackMe.from_dict(response.json())
