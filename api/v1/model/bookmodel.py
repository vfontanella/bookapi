import peewee as pw

from api.v1.utils.db import db
from .usermodel import User
from .authormodel import Author
from .subjectmodel import Subject

class Book(pw.Model):
    book_id = pw.PrimaryKeyField(null=False)
    title = pw.CharField()
    author = pw.ForeignKeyField(Author, backref="books")
    subject = pw.ForeignKeyField(Subject, backref="books")
    is_lent = pw.BooleanField(default=False)
    cover = pw.BlobField()
    isbn = pw.CharField()
    released_at = pw.IntegerField()
    user = pw.ForeignKeyField(User, backref="books")

    class Meta:
        database = db
        db_table = "books"
        order_by = ('title')
