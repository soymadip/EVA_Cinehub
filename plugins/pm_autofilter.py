import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \
    make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, PM_FILTER, AUTH_GROUPS, P_TTI_SHOW_OFF, PROTECT_CONTENT, IMDB, \
    SINGLE_BUTTON, SPELL_CHECK_REPLY, MAINTENANCE_MODE, IMDB_TEMPLATE, LOG_CHANNEL, SUPPORT_CHAT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.handlers import CallbackQueryHandler
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import (
    del_all,
    find_filter,
    get_filters,
)







@Client.on_message(filters.text & filters.private & filters.incoming & filters.chat(AUTH_GROUPS) if AUTH_GROUPS else filters.text & filters.group & filters.incoming)
async def pm_autofilter(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 1 < len(message.text) < 50:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"{get_size(file.file_size)} {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", callback_data=f"pmfile#{file_id}")]
                )
        else:
            await message.reply_photo(
                photo="https://telegra.ph/file/4e7e0a76a54d16ce2b80c.jpg",
                caption=f"\n<b>️📽️ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕄𝕠𝕧𝕚𝕖 </b> : {search}\n<b>👤ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕓𝕪 </b> : {message.from_user.mention}\n\n⚙️<b>𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝟮 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.</b>",
                reply_markup=InlineKeyboardMarkup([[
                   InlineKeyboardButton("🔘 REQUEST HERE 🔘", url=f"https://t.me/cinemaforyou07")
                   ]]
                )
            )
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages"),
                 InlineKeyboardButton("Close 🗑️", callback_data="close")]
            )


            imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=f"\n<b>️📽️ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕄𝕠𝕧𝕚𝕖 </b> : {search}\n<b>👤ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕓𝕪 </b> : {message.from_user.mention}\n\n⚙️<b>𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝟮 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.</b>", reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
            elif imdb:
                dell=await message.reply_photo(photo="https://telegra.ph/file/4e7e0a76a54d16ce2b80c.jpg", caption=f"\n<b>️📽️ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕄𝕠𝕧𝕚𝕖 </b> : {search}\n<b>👤ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕓𝕪 </b> : {message.from_user.mention}\n\n⚙️<b>𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝟮 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.</b>", reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
            else:
                dell=await message.reply_photo(photo="https://telegra.ph/file/4e7e0a76a54d16ce2b80c.jpg", caption=f"\n<b>️📽️ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕄𝕠𝕧𝕚𝕖 </b> : {search}\n<b>👤ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕓𝕪 </b> : {message.from_user.mention}\n\n⚙️<b>𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝟮 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.</b>", reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")

            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Next Page ➡",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("Close 🗑️", callback_data="close")]
        )

        imdb=await get_poster(search)
        if imdb and imdb.get('poster'):
            dell=await message.reply_photo(photo=imdb.get('poster'), caption=f"\n<b>️📽️ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕄𝕠𝕧𝕚𝕖 </b> : {search}\n<b>👤ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕓𝕪 </b> : {message.from_user.mention}\n\n⚙️<b>𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝟮 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.</b>", reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")         
        elif imdb:
            dell=await message.reply_photo(photo="https://telegra.ph/file/4e7e0a76a54d16ce2b80c.jpg", caption=f"\n<b>️📽️ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕄𝕠𝕧𝕚𝕖 </b> : {search}\n<b>👤ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕓𝕪 </b> : {message.from_user.mention}\n\n⚙️<b>𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝟮 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.</b>", reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
        else:
            dell=await message.reply_photo(photo="https://telegra.ph/file/4e7e0a76a54d16ce2b80c.jpg", caption=f"\n<b>️📽️ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕄𝕠𝕧𝕚𝕖 </b> : {search}\n<b>👤ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕓𝕪 </b> : {message.from_user.mention}\n\n⚙️<b>𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝟮 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.</b>", reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")