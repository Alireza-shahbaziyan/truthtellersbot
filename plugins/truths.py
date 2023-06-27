from pyrogram import Client,filters
from plugins.db_manger import *
from plugins.var import *

@Client.on_message(filters.reply & filters.regex("حق"))
def add_score(client,message):
    user = message.reply_to_message.from_user
    try:
        create_user(user_id=user.id,name=user.first_name)
    except:
        message.reply_text(error_create_user)
    try:
        update_user(user_id=user.id,score=1)
        message.reply_text("OK")
    except:
        message.reply_text(error_add_score)

@Client.on_message(filters.reply & filters.regex("status"))
def chenck_score(client,message):
    user = get_user(user_id=message.reply_to_message.from_user.id)
    chat_id = message.chat.id
    client.send_message(chat_id,User.Score)

