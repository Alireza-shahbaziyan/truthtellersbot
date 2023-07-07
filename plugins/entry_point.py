from pyrogram import Client, filters

from db import do



@Client.on_message(filters.all, group=-10)
def gate(_, message):
    if do.get_user(message.from_user.id) is None:
        do.add_user(message.from_user.id)


@Client.on_message(filters.command('start') & filters.private)
def start(_, message):
    message.reply_text("Hello")
