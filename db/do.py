from .models import *
from pony.orm import db_session

from datetime import datetime


@db_session
def get_user(user_id):
    return User.get(id=str(user_id))

@db_session
def add_user(user_id):
    return User(id=str(user_id), haghs=0, timestamp=datetime.now())

@db_session
def add_hagh(user_id):
    user = get_user(user_id)
    if user is None: return False
    user.haghs += 1
    return True