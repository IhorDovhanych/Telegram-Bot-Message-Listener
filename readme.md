# Telegram Bot Message Sender and Listener

This script interacts with a Telegram bot, sending a specified message and monitoring the bot's responses until it finds an expected piece of text. Upon finding the expected text, the script stops execution.

## Setup

1. **Telegram API Credentials**: Obtain `api_id`, `api_hash`, and `phone` from [my.telegram.org](https://my.telegram.org/auth).

2. **Environment Variables**: Create a `.env` file with the following variables:

```
API_ID=01234567
API_HASH=859325ga4ca28345u123d906f4358
PHONE=+1401234567
BOT_USERNAME=@example_username
MESSAGE_TO_FIND=expected_response_text
MESSAGE_TO_SEND=message_to_send_to_bot
```

3. **Dependencies**: 
    3.1 First create venv:
    ```
    python -m venv venv
    ```
    Than activate it
    ```
    .\venv\Scripts\activate
    ```
    3.2 Install necessary dependencies using `pip`:
    ```
    pip install telethon
    pip install python-dotenv
    ```
    or
    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Script**: Execute the script to start interacting with the Telegram bot.

2. **Expected Behavior**:

- The script sends `MESSAGE_TO_SEND` to `BOT_USERNAME`.
- It listens for responses from the bot.
- If `MESSAGE_TO_FIND` is found in a response, the script stops and notifies with a sound.
- If the bot sends the same message consecutively, the script terminates to prevent looping.

## Example

Suppose you want to send a message "Hello!" to `@example_bot` and wait for the response "Goodbye!". Set up your `.env` file as follows:
