# Documentation

## Overview

The `connectors.slack` package provides methods to interact with Slack's API, including sending messages to channels or users and retrieving user IDs from email addresses.

## Modules

### `connectors.slack`

This module contains functions to interact with Slack's API.

#### Functions

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
from connectors.slack import send_message

# Send a message to a specific channel
send_message("Hello, Slack!", "#general")

# Send a message to a

 user

 via email
send_message("Hello, User!", "user@example.com")
```

For more details, refer to the source code in `connectors/slack/methods.py`.