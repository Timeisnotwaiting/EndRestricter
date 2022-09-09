from pyrogram import Client, filters
import os

API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)
BOT_TOKEN = os.getenv("BOT_TOKEN", None)

app = Client(":environment:", API_ID, API_HASH, BOT_TOKEN)
