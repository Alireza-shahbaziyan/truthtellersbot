from pony import orm

from datetime import datetime

db = orm.Database()
db.bind(provider='sqlite', filename='../db.sqlite3', create_db=True)


class User(db.Entity):
    id        = orm.PrimaryKey(str) # user_id, ex: 956473054
    score     = orm.Required(int)
    supporters = orm.Required(orm.StrArray)
    joined_at = orm.Required(datetime)


db.generate_mapping(create_tables=True)