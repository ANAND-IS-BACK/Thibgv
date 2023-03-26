import requests
from FallenRobot import pbot
from pyrogram import filters



url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"
@pbot.on_message(filters.command('/ask'))
async def anu_pii(bot, m):
    text = m.text.split(' ', 1)[1]
    payload = {
    "enable_google_results": "true",
    "enable_memory": False,
    "input_text": text
    }
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "7384fc5d-3a89-44b6-b8c0-3f98c689d87f"
    }
    response = requests.post(url, json=payload, headers=headers)
    await m.reply(response.text, quote=True)
