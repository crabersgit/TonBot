

from pyrogram import Client

TG_API_ID=""
TG_API_HASH=""
app = Client("my_account",TG_API_ID,TG_API_HASH)

chat_id = -1001758611100
messages = []

async def main():
    async with app:
        async for message in app.get_chat_history(chat_id):
            if message.text is not None:
                print(message.text)
                print(message.date)
                # print(message.web_page)
                # messages.append(message.text)

app.run(main())