from telethon import TelegramClient, events
import asyncio
import winsound
from core.config import dict

api_id = dict["api_id"]
api_hash = dict["api_hash"]
phone = dict["phone"]
"""
To get api_id and api_hash you need to
create telegram application on my.telegram.org
Fields like Title, Short name and URL are required
(else you will have errors due creating application)
to create application, these parameters could be random.
----------------------------------------------------
Than create .env file like this
API_ID=01234567
API_HASH=859325ga4ca28345u123d906f4358
PHONE=+1401234567
BOT_USERNAME=@example_username
"""

bot_username = dict["bot_username"]  # use telegram tags: @example_username

message_to_find = dict["message_to_find"]  # a message you expect in response
previous_message = (
    ""  # a variable which need to avoid loop if you getting same response after message
)

message_to_send = dict["message_to_send"]  # a message which you send to the chat

client = TelegramClient("session_name", api_id, api_hash)


@client.on(events.NewMessage(from_users=[bot_username]))
async def handler(event):
    global previous_message, message_to_find, message_to_send
    if (
        event.message.message
    ):  # this variable could return null sometimes and it's make bot working incorrect, so we check is it exists
        print("🤖----------------Response----------------🤖")
        default_print(message_to_send, event.message.message)

        if message_to_find in event.message.message:  # found message condition
            print("✅-----------------FOUND-----------------✅")
            default_print(message_to_send, event.message.message)
            print("---------------------END--------------------")
            winsound.MessageBeep()
            await client.disconnect()

        elif (
            event.message.message == previous_message
        ):  # stuck with similar messages condition
            print("❌-----------------STUCK------------------❌")
            default_print(message_to_send, event.message.message)
            print("💥-------------------END------------------💥")
            winsound.MessageBeep()
            await client.disconnect()

        previous_message = event.message.message

        await asyncio.sleep(
            0.1
        )  # some delay to avoid bugs, haven't try bot without this delay, you can delete this on your own risk
        await client.send_message(bot_username, message_to_send)


def default_print(message, response):
    print("Message:")
    print(f'"{message}"\n')
    print("Bot response:")
    print(response)


async def main():
    await client.start(phone)
    await client.send_message(bot_username, message_to_send)
    await client.run_until_disconnected()


client.loop.run_until_complete(main())
