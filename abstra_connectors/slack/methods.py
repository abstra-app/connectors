from typing import Optional
import requests
import os


def is_email(channel: str) -> bool:
    return "@" in channel


def get_user_id_from_email(email: str) -> str:
    token = os.getenv("SLACK_BOT_TOKEN")
    if token is None:
        raise Exception("SLACK_BOT_TOKEN env var is not set")
    response = requests.get(
        "https://slack.com/api/users.lookupByEmail",
        params={"email": email},
        headers={"Authorization": "Bearer " + token},
    )
    return response.json()["user"]["id"]


def send_message(msg: str, channel: Optional[str] = None):
    if channel is None:
        channel = os.getenv("SLACK_CHANNEL")
    if channel is None:
        raise Exception("channel not set")

    if is_email(channel):
        channel = get_user_id_from_email(channel)
    token = os.getenv("SLACK_BOT_TOKEN")
    if token is None:
        raise Exception("SLACK_BOT_TOKEN env var is not set")
    requests.post(
        "https://slack.com/api/chat.postMessage",
        json={
            "channel": channel,
            "text": msg,
        },
        headers={
            "Authorization": "Bearer " + token,
            "Content-type": "application/json; charset=utf-8",
        },
    )
