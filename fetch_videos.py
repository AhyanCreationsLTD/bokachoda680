import os
import json
from pyrogram import Client

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

chat_id_env = os.getenv("CHAT_ID", "0")
try:
    # যদি -100 সহ সংখ্যা আইডি হয়
    CHAT_ID = int(chat_id_env)
except ValueError:
    # যদি চ্যানেলের ইউজারনেম হয় (যেমন: @mychannel)
    CHAT_ID = chat_id_env

app = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    async with app:
        videos = []
        print(f"Fetching messages from chat: {CHAT_ID}")
        
        # সরাসরি চ্যানেল থেকে মেসেজ ফেচ করা (বটের জন্য এটি সম্পূর্ণ বৈধ)
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
