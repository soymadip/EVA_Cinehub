
import asyncio
from pyrogram import Client, filters




@Client.on_message(filters.channel & (filters.document | filters.video | filters.audio ) & filters.incoming)
async def editing(bot, message):
     caption_text = message.file.file_name
     await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.message_id,
                 caption = caption_text, 
                 parse_mode = "markdown"
             ) 
              
                   
      
