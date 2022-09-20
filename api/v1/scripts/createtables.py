from api.v1.model.usermodel import User
from api.v1.model.bookmodel import Book
from api.v1.model.authormodel import Author
from api.v1.model.subjectmodel import Subject

from api.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Book, Author, Subject])
