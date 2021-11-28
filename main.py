from telethon import TelegramClient, events

SESSION_NAME = 'session_read'
CHAT_ID = 0
GROUP_ID = ""
API_ID = 0
API_HASH = ''

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


@client.on(events.NewMessage(chats=GROUP_ID))
async def handler(event):
    await client.send_message(CHAT_ID, event.raw_text)


client.start()
client.run_until_disconnected()
