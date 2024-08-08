from peewee import SqliteDatabase, Model, IntegerField, CharField, TextField
from flask_login import UserMixin
db = SqliteDatabase("db.sqlite")


class User(Model, UserMixin):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True)
    email = CharField(unique=True)
    password = TextField()

    class Meta():
        database = db
        table_name = "user"


db.create_tables([User])
