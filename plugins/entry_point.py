from pyrogram import Client, filters

from db import do



@Client.on_message(filters.all, group=-10)
def gate(_, message):
    if do.get_user(message.from_user.id) is None:
        do.add_user(message.from_user.id)


@Client.on_message(filters.command('start') & filters.private)
def start(_, message):
    message.reply_text("جوابتو نمیدم کنفت بشی")

@Client.on_message(filters.reply & filters.regex("truth"))
def truth(_,message):
    target_id = message.reply_to_message.from_user.id
    do.add_hagh(target_id)
    target = do.get_user(target_id)
    # message.reply_text( f"یک حق به حقهای کاربر اضاف شد \n تعداد حق های کاربر:{target.haghs}")
    with open("video/hagh.mp4", "rb") as f:
        message.reply_video(video=f,caption=f"یک حق به حقهای کاربر اضاف شد \n تعداد حق های کاربر:{target.haghs}")
    
