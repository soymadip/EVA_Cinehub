from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    ChatPermissions
)
from plugins.SD_plugins.Help_Functions.admin_check import admin_check
from plugins.SD_plugins.Help_Functions.extract_user import extract_user
from plugins.SD_plugins.Help_Functions.string_handling import extract_time


@Client.on_message(filters.command("mute"))
async def mute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)
    reason = message.text.split('/mute')[1]
    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions(
            )
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "👍🏻 "
                f"{user_first_name} has been 🔇 muted."
                f"\n<b>Reason:</b> {reason} "
            )
        else:
            await message.reply_text( 
                f"<a href='tg://user?id={user_id}'>{user_first_name}</a> has been 🔇 muted."
                f"\n\n<b>Reason:</b> {reason}"
            )


@Client.on_message(filters.command("tmute"))
async def temp_mute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    if not len(message.command) > 1:
        return

    user_id, user_first_name = extract_user(message)
    reason = message.text.split('/tmute')[1]

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Invalid time type specified. "
                "Expected m, h, or d, Got it: {}"
            ).format(
                message.command[1][-1]
            )
        )
        return

    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions(
            ),
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        buttons = [[InlineKeyboardButton('🍷 Request to Unmute', url='https://t.me/anonymous7205')]]
        if str(user_id).lower().startswith("@"):
            await message.reply_text( 
                f"\<a href='tg://user?id={user_id}'>{user_first_name}</a> has been 🔇 muted for <b>{message.command[1]}</b>."
                f"\n\n<b>Reason:</b> {reason}",reply_markup=InlineKeyboardMarkup(buttons)
            )
        else:
            await message.reply_text( 
                f"\<a href='tg://user?id={user_id}'>{user_first_name}</a> has been 🔇 muted for <b>{message.command[1]}</b>."
                f"\n\n<b>Reason:</b> {reason}",reply_markup=InlineKeyboardMarkup(buttons)
            )
