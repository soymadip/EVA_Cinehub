import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
try:
    apiid = config("API_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    datgbot = TelegramClient('bot', apiid, apihash)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()



@datgbot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            if event.poll:
                print("skipped poll.")
            if event.sticker:
                return
            if event.photo:
                print("skipped pic.")
            elif event.media:
                try:
                    if event.media.webpage:
                        print("skipped links.")
                except:
                    media = event.media.document
                    await asyncio.sleep(1)
                    await datgbot.send_file(tochnl, media, caption = event.text, link_preview = False)
                    return
            else:
                print("skipped text.")
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")

