import os
import json
from pyrogram import Client

# গিটহাব সিক্রেটস থেকে ক্রেডেনশিয়াল ফেচ করা
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHAT_ID = int(os.getenv("CHAT_ID", "0"))

app = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    async with app:
        videos = []
        # চ্যানেল থেকে সর্বশেষ ৫০টি মেসেজ চেক করা হচ্ছে
        async for message in app.get_chat_history(CHAT_ID, limit=50):
            if message.video:
                title = message.caption or f"ভিডিও - {message.video.file_name or message.id}"
                file_id = message.video.file_id
                videos.append({
                    "id": file_id,
                    "title": title
                })
        
        # videos.json ফাইল সেভ করা
        with open("videos.json", "w", encoding="utf-8") as f:
            json.dump(videos, f, ensure_ascii=False, indent=2)
        print("Successfully generated videos.json!")

app.run(main())
