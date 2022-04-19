from pyrogram import Client, filters
import re
import ast
import asyncio

from plugins.pm_filter import auto_filter


@Client.on_message(filters.private & filters.text & filters.incoming)
async def private_give_filter(client, message):
        await auto_filter(client, message)

