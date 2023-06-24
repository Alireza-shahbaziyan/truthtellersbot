from pyrogram import Client, filters

@Client.on_message(filters.command('start'))
def start_command(c,m):
    m.reply_text("برو بچه. \nپی وی مساوی بلاک\nبدو مزاحم نشو من قصد ادامه تحصیل دارم\n امدی پی وی واسه چی")