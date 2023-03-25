import requests
import pbot as Client
from pyrogram import Client, filters



url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"
@Client.on_message(filters.command('/ask'))
async def anu_pii(bot, m):
    text = m.text[len('/ask ') :]
    payload = {
    "enable_google_results": "true",
    "enable_memory": False,
    "input_text": f"{text}"
    }
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "7384fc5d-3a89-44b6-b8c0-3f98c689d87f"
    }
    response = requests.post(url, json=payload, headers=headers)
    await m.reply(response.text)
