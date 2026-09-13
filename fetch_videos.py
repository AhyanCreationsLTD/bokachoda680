import os
import json
from pyrogram import Client

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# CHAT_ID কে স্ট্রিং হিসেবে নেওয়া, যাতে -100 প্রিফিক্স বা ইউজারনেম দুটোই কাজ করে
chat_id_env = os.getenv("CHAT_ID", "0")
try:
    CHAT_ID = int(chat_id_env)
except ValueError:
    CHAT_ID = chat_id_env  # যদি চ্যানেলের ইউজারনেম হয় (যেমন: "@mychannel")

app = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    async with app:
        print("Connecting to channel...")
        chat = await app.get_chat(CHAT_ID)
        print(f"Successfully connected to: {chat.title}")

        videos = []
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
