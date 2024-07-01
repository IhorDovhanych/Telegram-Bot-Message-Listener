import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv(".env")

# Create dictionary using environment variables
config = {
    "api_id": os.getenv("API_ID"),
    "api_hash": os.getenv("API_HASH"),
    "phone": os.getenv("PHONE"),
    "bot_username": os.getenv("BOT_USERNAME"),
    "expected_message_piece": os.getenv("EXPECTED_MESSAGE_PIECE"),
    "message_to_send": os.getenv("MESSAGE_TO_SEND"),
    "telegram_path": os.getenv("TELEGRAM_PATH")
}
