import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \
    make_inactive
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.handlers import CallbackQueryHandler
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results



@Client.on_message(filters.text & filters.private & filters.incoming) #PM guide module
async def filter(client, message):
    if message.text.startswith("/"):
        return 
    if 2 < len(message.text) < 10:
        btn = [
        [
            InlineKeyboardButton('⚡️ ℂ𝕀ℕ𝔼𝕄𝔸 ℍ𝕌𝔹 ⚡️', url=f'https://t.me/cinemaforyou07')
        ]
        ]
        await client.send_message(chat_id=message.from_user.id, text='🔰𝗡𝗢𝗧𝗜𝗖𝗘🔰\n\nDo not request here😡\nThis chat is only for <u>movie delevery</u>.\n\n<b>Request in CINEMA HUB group👇🏻</b>', reply_markup=InlineKeyboardMarkup(btn))
