from tinydb import TinyDB, Query
from pyrogram import Client , filters

db = TinyDB('../db.json')

def add_user(user_id):
    Fruit = Query()
    if db.search(Fruit.userName == 'apple') == None :
        db.insert({'user_id': user_id, 'Score':0,truth:[]})

