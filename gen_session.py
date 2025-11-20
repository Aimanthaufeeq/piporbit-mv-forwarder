from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 34390587
api_hash = "734cef163cc42917b1babcafd9755412"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\n🔥 Your PIPORBIT MV Session String:")
    print(client.session.save())
    print("\n⚠️ Copy this and paste into Render environment variable TG_SESSION")