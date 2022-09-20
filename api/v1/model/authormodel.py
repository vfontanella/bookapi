import peewee

from api.v1.utils.db import db

class Author(peewee.Model):
    author_id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField()
    surname = peewee.CharField()
    author = peewee.
    biography = peewee.CharField(300)
    

    class Meta:
        database = db
        db_table = "authors"
        order_by = ('name',)
