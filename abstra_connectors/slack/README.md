# Documentation

## Overview

The `abstra_connectors.slack` package provides methods to interact with Slack's API, including sending messages to channels or users and retrieving user IDs from email addresses.

## Modules

### `abstra_connectors.slack.methods`

This module contains functions to interact with Slack's API.

#### Functions

##### `is_email(channel: str) -> bool`

Checks if the given channel string is an email address.

- **Parameters:**
  - `channel` (str): The channel string to check.

- **Returns:**
  - `bool`: `True` if the channel is an email address, `False` otherwise.

##### `get_user_id_from_email(email: str) -> str`

Retrieves a Slack user ID from an email address.

- **Parameters:**
  - `email` (str): The email address to look up.

- **Returns:**
  - `str`: The Slack user ID associated with the email address.

- **Raises:**
  - `Exception`: If the `SLACK_BOT_TOKEN` environment variable is not set.

##### `send_message(msg: str, channel: Optional[str] = None)`

Sends a message to a Slack channel or user.

- **Parameters:**
  - `msg` (str): The message to send.
  - `channel` (Optional[str]): The Slack channel or user to send the message to. If not provided, it defaults to the `SLACK_CHANNEL` environment variable.

- **Raises:**
  - `Exception`: If the `SLACK_BOT_TOKEN` environment variable is not set.
  - `Exception`: If the channel is not set.

- **Behavior:**
  - If the channel is an email address, it converts the email to a Slack user ID before sending the message.

## Environment Variables

- `SLACK_BOT_TOKEN`: The token used to authenticate with Slack's API.
- `SLACK_CHANNEL`: The default Slack channel to send messages to if no channel is provided.

## Example Usage

```python
from abstra_connectors.slack.methods import send_message

# Send a message to a specific channel
send_message("Hello, Slack!", "#general")

# Send a message to a

 user

 via email
send_message("Hello, User!", "user@example.com")
```

For more details, refer to the source code in `abstra_connectors/slack/methods.py`.