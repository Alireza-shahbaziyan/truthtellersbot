from plugins.models import User
import datetime

def get_user(user_id):
    return User().select().where(User.user_id == user_id)

def create_user(user_id, name):
    if get_user(user_id) != None: return False
    user = User.create(user_id=user_id, name=name, joined_at=datetime.now(),)
    return True

def update_user(user_id,score):
    user = get_user(user_id)
    if user == None: return False
    if user != None:
        user.name = name
        user.Score += score
        user.last_activity = datetime.now()
        user.save()
        return True
