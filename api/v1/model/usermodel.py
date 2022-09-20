import peewee

from app.v1.utils.db import db

class User(peewee.Model):
    user_id = peewee.PrimaryKeyField(null=False)
    email = peewee.CharField(unique=True, index=True)
    name = peewee.CharField()
    surname = peewee.CharField()
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()
    is_active = peewee.BooleanField(default=True)

    class Meta:
        database = db
        db_table = "users"
        order_by = ('name',)
