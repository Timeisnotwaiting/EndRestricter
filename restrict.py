from pyrogram import Client, filters
import os

API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)
BOT_TOKEN = os.getenv("BOT_TOKEN", None)

app = Client(":environment:", API_ID, API_HASH, BOT_TOKEN)

@app.on_message(filters.command(["negate_name", "denegate_name"]))
async def appendix(_, m):
    if m.text.split()[0][1].lower() == "d":
        return await denegate_fn(_, m)
    return await negate_fn(_, m)
    
@app.on_message(filters.command("
