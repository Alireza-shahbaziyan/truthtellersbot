from pyrogram import Client, filters
from plugins.var import pv_start_result

@Client.on_message(filters.command('start'))
def start_command(c,m):
    m.reply_text(pv_start_result)
    