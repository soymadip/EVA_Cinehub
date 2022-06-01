import logging
from info import NM_CHAT, NM_TIME, TIMEZONE
from pyrogram import filters , Client as nmbot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions


NM_START = NM_TIME.split('-')[0]

NM_END = NM_TIME.split('-')[1]


async def group_close():
        await nmbot.set_chat_permissions(
                NM_CHAT,
                ChatPermissions()
                )



async def group_open():
        await nmbot.set_chat_permissions(
                NM_CHAT,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_stickers=True,
                    can_send_animations=True
                    )
                )




scheduler = AsyncIOScheduler(timezone=TIMEZONE)
scheduler.add_job(group_close, trigger="cron", hour=6, minute=59)
scheduler.add_job(group_open, trigger="cron", hour=8, minute=1)
scheduler.start()
