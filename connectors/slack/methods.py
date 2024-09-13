from typing import Optional
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
