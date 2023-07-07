from pyrogram import Client, filters

@Client.on_message(filters.command('start') & filters.private)
def start(client, message):
    message.reply_text("Hello")
