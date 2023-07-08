from .models import *
from pony.orm import db_session

from datetime import datetime


@db_session
def get_user(user_id):
    return User.get(id=str(user_id))


@db_session
def add_user(user_id):
    return User(id=str(user_id), score=0, supporters=[], joined_at=datetime.now())


@db_session
def add_hagh(receiver, giver):
    user = get_user(receiver)
    
    # if user befor give a gagh :/
    if str(giver) in user.supporters: return False

    user.score += 1
    user.supporters += [str(giver)]
    return True

