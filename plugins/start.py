from pyrogram import Client, filters
import config
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(config.message.START.format(message.from_user.mention),
    	reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Noticias", switch_inline_query='')]]))
