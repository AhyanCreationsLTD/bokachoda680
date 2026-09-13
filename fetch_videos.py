import os
import json
from pyrogram import Client

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# সরাসরি সিক্রেট থেকে চ্যানেলের ইউজারনেম বা আইডি নেওয়া
CHAT_ID = os.getenv("CHAT_ID", "")
if CHAT_ID.startswith("-100") or CHAT_ID.isdigit():
    CHAT_ID = int(CHAT_ID)

app = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    async with app:
        videos = []
        print(f"Fetching messages from: {CHAT_ID}")
        
        async for message in app.get_chat_history(CHAT_ID, limit=50):
            if message.video:
                title = message.caption or f"ভিডিও - {message.video.file_name or message.id}"
                file_id = message.video.file_id
                videos.append({
                    "id": file_id,
                    "title": title
                })
        
        with open("videos.json", "w", encoding="utf-8") as f:
            json.dump(videos, f, ensure_ascii=False, indent=2)
        print("Successfully generated videos.json!")

app.run(main())
