from pyrogram import Client, filters
from db import do

@Client.on_message(filters.reply & filters.regex("حق"))
async def truth(_,message):
    target_id = message.reply_to_message.from_user.id # Getting the target personal ID

    message_target_id = message.reply_to_message.id # geetting the target message ID

    add_hagh = do.add_hagh(target_id,message_target_id) # call add_hagh function and add a score

    if add_hagh == False : 
        await message.reply_text("یکبار تایید کردم کافیه")
    else:
        target = do.get_user(target_id)
        with open("video/hagh.mp4", "rb") as f:
            await message.reply_video(video=f,caption=f"یک حق به حقهای کاربر اضاف شد \n تعداد حق های کاربر: **{target.score}**")