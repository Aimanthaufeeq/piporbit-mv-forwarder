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


# -----------------------------------------------------------------------------------
# SIGNAL FILTER — detects when a message is actually a forex signal
# -----------------------------------------------------------------------------------

SIGNAL_KEYWORDS = [
    "buy", "sell",
    "tp", "sl",
    "xauusd", "gold",
    "signal",
]

def is_signal(text):
    text = text.lower()
    return any(keyword in text for keyword in SIGNAL_KEYWORDS)


# -----------------------------------------------------------------------------------
# MAIN EVENT — When the bot receives a message in the SOURCE group
# -----------------------------------------------------------------------------------

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):
    text = event.raw_text.strip()

    # Ignore empty
    if not text:
        return

    # FILTERING
    if not is_signal(text):
        print("IGNORED:", text)
        return

    # COPY + PASTE SIGNAL
    print("PIPORBIT MV — SIGNAL SENT:", text)
    await client.send_message(TARGET_CHAT_ID, text)


# -----------------------------------------------------------------------------------
# START BOT
# -----------------------------------------------------------------------------------

print("🔥 PIPORBIT MV — FILTERED SIGNAL BOT RUNNING…")
client.start()
client.run_until_disconnected()
