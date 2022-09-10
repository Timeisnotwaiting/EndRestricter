from pyrogram import Client
from pyrogram.types import Message
from db import *


async def negate_fn(_, m):
    usage = f"<i>**Usage** : /negate_name [ NAME ] <i>"
    if await is_blocked(m.from_user.id):
        return
    mem = await _.get_chat_member(m.chat.id, m.from_user.id)
    if not mem.status in ["creator", "administrator"]:
        return
    if not len(m.command) == 2:
        return await m.reply(f"<i>**Usage** : /negate_name [ NAME ] </i>")
    name = m.text.split()[1]
    if not name:
        return await m.reply(usage)
    checker = await is_name_negated(m.chat.id, name)
    if checker:
        return await m.reply(f"<i>Already exists in blocklist...!</i>")
    try:
        await negate_name(m.chat.id, name)
        return await m.reply(f"<code>{name}</code><i>added to blocklist..!</i>")
    except Exception as e:
        return await m.reply(f"<i>{e}</i>")
    
async def denegate_fn(_, m):
    usage = f"<i>**Usage** : /denegate_name [ NAME ] <i>"
    if await is_blocked(m.from_user.id):
        return
    mem = await _.get_chat_member(m.chat.id, m.from_user.id)
    if not mem.status in ["creator", "administrator"]:
        return
    if not len(m.command) == 2:
        return await m.reply(f"<i>**Usage** : /denegate_name [ NAME ] </i>")
    name = m.text.split()[1]
    if not name:
        return await m.reply(usage)
    checker = await is_name_negated(m.chat.id, name)
    if not checker:
        return await m.reply(f"<i>Doesn't exists in blocklist...!</i>")
    try:
        await denegate_name(m.chat.id, name)
        return await m.reply(f"<code>{name}</code><i>removed from blocklist..!</i>")
    except Exception as e:
        return await m.reply(f"<i>{e}</i>")

async def blocked_names(_, m):
    if await is_blocked(m.from_user.id):
        return
    mem = await _.get_chat_member(m.chat.id, m.from_user.id)
    if not mem.status in ["creator", "administrator"]:
        return
    names = await get_negated_names(m.chat.id)
    msg = ""
    for name in names:
        msg += f"{name}\n"
    return await m.reply(msg)
    
