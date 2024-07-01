import os
import dotenv

'''
Here we extracting data from .env
'''

dotenv.load_dotenv(".env")
dict = {
    "api_id": os.environ.get("API_ID"),
    "api_hash": os.environ.get("API_HASH"),
    "phone": os.environ.get("PHONE"),
    "bot_username": os.environ.get("BOT_USERNAME"),
    "expected_message_piece": os.environ.get("EXPECTED_MESSAGE_PIECE "),
    "message_to_send": os.environ.get("MESSAGE_TO_SEND")
}
