import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from user import USER
from info import LOG_CHANNEL

@Client.on_message(filters.command(["json", 'js', 'showjson']))
async def jsonify(bot, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message
    try:
        pk = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✗ close ✗",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_text(f"{the_real_message}", reply_markup=pk, quote=True)
        await bot.USER.send_message(LOG_CHANNEL, f"hcufuvuvuvvhvuvuv")
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✗ close ✗",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            quote=True,
            reply_markup=reply_markup
        )            
        os.remove("json.text")
