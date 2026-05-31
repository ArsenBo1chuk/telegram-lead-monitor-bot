from telethon import TelegramClient, events
import config
from datetime import datetime
import os
import logging
from logging.handlers import RotatingFileHandler
import re

log_handler = RotatingFileHandler(
    config.LOG_FILE, maxBytes=5*1024*1024, backupCount=2, encoding='utf-8'
)
logging.basicConfig(
    handlers=[log_handler],
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def write_log(chat_name, keyword):
    logging.info(f"Chat: {chat_name} | Keyword: {keyword}")

def load_list(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def load_sent_messages():
    if not os.path.exists(config.SENT_FILE):
        return set()
    with open(config.SENT_FILE, "r") as f:
        return set(line.strip() for line in f)

def save_sent_message(message_id):
    with open(config.SENT_FILE, "a") as f:
        f.write(str(message_id) + "\n")
    
    with open(config.SENT_FILE, "r") as f:
        lines = f.readlines()
    if len(lines) > 5000:
        with open(config.SENT_FILE, "w") as f:
            f.writelines(lines[-2000:]) 


keywords = [k.lower() for k in load_list(config.KEYWORDS_FILE)]
chats = load_list(config.CHATS_FILE)
sent_messages = load_sent_messages()

client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)

@client.on(events.NewMessage(chats=chats))
async def handler(event):
    global sent_messages
    
    text = (event.raw_text or "").lower()
    unique_id = f"{event.chat_id}_{event.id}"

    if unique_id in sent_messages:
        return

    for keyword in keywords:
     if re.search(rf'\b{re.escape(keyword)}\b', text):
            chat = await event.get_chat()
            chat_name = getattr(chat, 'title', 'Приватний чат/Unknown')
            
            message_link = "Посилання відсутнє (приватний чат)"
            if getattr(chat, 'username', None):
                message_link = f"https://t.me/{chat.username}/{event.id}"
            else:
                peer_id = str(event.chat_id).replace("-100", "")
                message_link = f"https://t.me/c/{peer_id}/{event.id}"

            report_text = (
                f"**Новий потенційний клієнт**\n\n"
                f"**Чат:** {chat_name}\n"
                f"**Ключове слово:** `{keyword}`\n\n"
                f"**Текст:**\n{event.raw_text}\n\n"
                f"**Посилання:** {message_link}"
            )

            try:
                await client.send_message(config.MY_ID, report_text)
                
                write_log(chat_name, keyword)
                save_sent_message(unique_id)
                sent_messages.add(unique_id)
            except Exception as e:
                print(f"Помилка при відправці: {e}")
            
            break

async def main():
    phone_number = input("Введіть ваш номер телефону (наприклад, +380...): ")
    
    await client.start(phone=phone_number)
    print("Бот запущений і моніторить чати...")
    
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


