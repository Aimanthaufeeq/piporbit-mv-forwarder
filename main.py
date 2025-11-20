from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import re

api_id = 34390587
api_hash = "734cef163cc42917b1babcafd9755412"

SOURCE_CHAT_ID = -1001239815745     # VIP Private Group
TARGET_CHAT_ID = -4990680315        # Your Group

session_string = os.getenv("TG_SESSION")

client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Keywords that define a SIGNAL
SIGNAL_KEYWORDS = [
    "buy", "sell", "xau", "gold",
    "tp", "sl", "entry", 
]

def is_signal(text):
    """Check if message qualifies as a signal"""
    text_lower = text.lower()

    # Check if any keyword is in message
    if any(keyword in text_lower for keyword in SIGNAL_KEYWORDS):
        return True

    # Also detect if message contains a price-like number
    if re.search(r"\b\d{3,5}\b", text):  # detects numbers like 1850, 2304, etc.
        return True

    return False


@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def forward_signal(event):

    text = event.message.message

    if not text:
        return

    # FILTERING: Only send if it’s a SIGNAL
    if not is_signal(text):
        print("IGNORED:", text)
        return

    # COPY + PASTE (not forward)
    print("PIPORBIT MV — SIGNAL SENT:", text)
    await client.send_message(TARGET_CHAT_ID, text)


print("🔥 PIPORBIT MV — FILTERED SIGNAL BOT RUNNING…")
client.start()
client.run_until_disconnected()
