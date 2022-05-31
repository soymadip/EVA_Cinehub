import logging
from info import NM_CHAT, NM_TIME, TIMEZONE
from pyrogram import Client, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions


NM_START = NM_TIME.split('-')[0]

NM_END = NM_TIME.split('-')[1]


async def group_close():
    try:
        await Bot.send_message(
                NM_CHAT,
                "Group is Closing!"
                )
        await Bot.set_chat_permissions(
                NM_CHAT,
                ChatPermissions()
                )
    except BaseException as e:
        await Bot.send_message(
                NM_CHAT,
                f"**Error while closing group:**"
                )

async def group_open():
    try:
        await bBt.send_message(
                NM_CHAT,
                "Opened group"
                )
        await Bot.set_chat_permissions(
                NM_CHAT,
                ChatPermissions(
                    can_send_messages=True
                    )
                )
    except BaseException as e:
        await bot.send_message(
                NM_CHAT,
                f"**Error while opening group:**"
                )


scheduler = AsyncIOScheduler(timezone=TIMEZONE)
scheduler.add_job(group_close, trigger="cron", hour=23, minute=10)
scheduler.add_job(group_open, trigger="cron", hour=8, minute=1)
scheduler.start()
