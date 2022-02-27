
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
