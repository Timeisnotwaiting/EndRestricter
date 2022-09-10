from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

_BLOCK_MARKUP = InlineKeyboardMarkup([
            [InlineKeyboardButton("Names", callback_data="names"),
            InlineKeyboardButton("Usernames", callback_data="usernames")
            ]
            ]
