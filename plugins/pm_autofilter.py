import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, PM_FILTER, AUTH_GROUPS, P_TTI_SHOW_OFF, PROTECT_CONTENT, IMDB, \
    SINGLE_BUTTON, SPELL_CHECK_REPLY, MAINTENANCE_MODE, IMDB_TEMPLATE, LOG_CHANNEL, SUPPORT_CHAT
from plugins.pm_filter import advantage_spell_chok
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


@Client.on_message(filters.private & filters.text & ~filters.edited & filters.incoming)
async def auto_filter(client, msg, spoll=False):
    if not spoll:
        message = msg
        settings = await get_settings(message.chat.id)
        if message.text.startswith("/"): return  # ignore commands
        if message.text.startswith("#"): return  # ignore wrong formats
        if message.text.startswith("."): return # ignore userbot commands
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
            return
        if 1 < len(message.text) < 100:
            search = message.text
            files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)
            if not files:
                if SPELL_CHECK_REPLY:
                    return await advantage_spell_chok(msg)
                else:
                    return
        else:
            return
    else:
        settings = await get_settings(msg.message.chat.id)
        message = msg.message.reply_to_message  # msg will be callback query
        search, files, offset, total_results = spoll
    pre = 'file'
    if SINGLE_BUTTON:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}", callback_data=f'{pre}#{file.file_id}'
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}",
                    callback_data=f'{pre}#{file.file_id}',
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'{pre}_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if offset != "":
        key = f"{message.chat.id}-{message.message_id}"
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append(
                [InlineKeyboardButton(text="⭕️ ℂℍ𝔼ℂ𝕂 ℙ𝕄 ⭕️", url=f"https://telegram.dog/{temp.U_NAME}")]
            )
        btn.append(
            [InlineKeyboardButton(text=f"🗓 1/{round(int(total_results) / 10)}", callback_data="pages"),
             InlineKeyboardButton(text="𝗡𝗘𝗫𝗧 ⏩", callback_data=f"next_{req}_{key}_{offset}")]
        )
    else:
        btn.append(
                [InlineKeyboardButton(text="⭕️ ℂℍ𝔼ℂ𝕂 ℙ𝕄 ⭕️", url=f"https://telegram.dog/{temp.U_NAME}")]
            )
        btn.append(
            [InlineKeyboardButton(text="🗓 1/1", callback_data="pages")]
        )
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    imdb = await get_poster(search, file=(files[0]).file_name) if IMDB else None
    TEMPLATE = IMDB_TEMPLATE
    if imdb:
        cap = TEMPLATE.format(
            query=search,
            title=imdb['title'],
            votes=imdb['votes'],
            aka=imdb["aka"],
            seasons=imdb["seasons"],
            box_office=imdb['box_office'],
            localized_title=imdb['localized_title'],
            kind=imdb['kind'],
            imdb_id=imdb["imdb_id"],
            cast=imdb["cast"],
            runtime=imdb["runtime"],
            countries=imdb["countries"],
            certificates=imdb["certificates"],
            languages=imdb["languages"],
            director=imdb["director"],
            writer=imdb["writer"],
            producer=imdb["producer"],
            composer=imdb["composer"],
            cinematographer=imdb["cinematographer"],
            music_team=imdb["music_team"],
            distributors=imdb["distributors"],
            release_date=imdb['release_date'],
            year=imdb['year'],
            genres=imdb['genres'],
            poster=imdb['poster'],
            plot=imdb['plot'],
            rating=imdb['rating'],
            url=imdb['url'],
            **locals()
        )
    else:
        cap = f"\n<b>️📽️ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕄𝕠𝕧𝕚𝕖 </b> : {search}\n<b>👤ℝ𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕓𝕪 </b> : {message.from_user.mention}\n\n⚙️<b>𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝟮 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.</b>"
    if imdb and imdb.get('poster'):
        try:
            hehe = await message.reply_photo(photo=imdb.get('poster'), caption=cap[:1024], reply_to_message_id=reply_id, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(150)
            await hehe.delete()
            await message.delete()
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            hmm = await message.reply_photo(photo=poster, caption=cap[:1024], reply_to_message_id=reply_id, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(150)
            await hmm.delete()
            await message.delete()
        except Exception as e:
            logger.exception(e)
            fek = await message.reply_photo(photo="https://telegra.ph/file/4e7e0a76a54d16ce2b80c.jpg", caption=cap, reply_to_message_id=reply_id, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(150)
            await fek.delete()
            await msg.delete()
    else:
        fuk = await message.reply_photo(photo="https://telegra.ph/file/4e7e0a76a54d16ce2b80c.jpg", caption=cap, reply_to_message_id=reply_id, reply_markup=InlineKeyboardMarkup(btn))
        await asyncio.sleep(150)
        await fuk.edit(f"\n \n⚙️ {message.from_user.mention}'s Result For **{search}**  Closed ️")
