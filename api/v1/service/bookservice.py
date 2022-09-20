from fastapi import HTTPException, status

from api.v1.model.bookmodel import Book as BookModel
from api.v1.schema import bookschema
from api.v1.schema import userschema

def add_book(book: bookschema.AddBook, user: userschema.User):
    db_book = BookModel(
        title=book.title,
        user_id=user.id
    )

    db_book.save()

    return bookschema.Book(
        id = db_book.id,
        title = db_book.title,
        is_lent = db_book.is_lent,
        created_at = db_book.created_at
    )

def get_book(user: userschema.User, is_lent: bool = None):
    if(is_lent is None):
        book_by_user = BookModel.filter(BookModel.user_id == user.id).order_by(BookModel.created_at.desc())
    else:
        book_by_user = BookModel.filter((BookModel.user_id == user.id) & (BookModel.is_lent == is_lent)).order_by(BookModel.created_at.desc())

    list_books = []
    for book in book_by_user:
        list_books.append(
            bookschema.Book(
                id = book.id,
                title = book.title,
                author = book.author,
                subject = book.subject,
                is_lent = book.is_lent,
                released_at = book.released_at
            )
        )

    return list_books

def get_book(book_id: int, user: userschema.User):
    book = BookModel.filter((BookModel.id == book_id) & (BookModel.user_id == user.id)).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not in database..."
        )

    return bookschema.Book(
        id = book.id,
        title = book.title,
        author = book.author,
        subject = book.subject,
        is_lent = book.is_lent,
        released_at = book.released_at
    )

    def update_book_status(is_lent: bool, book_id: int, user: userschema.User):
        book = BookModel.filter((BookModel.id == book_id) & (BookModel.user_id == user.id)).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not in database..."
            )

        book.is_lent = is_lent
        book.save()

        return bookschema.Book(
            id = book.id,
            title = book.title,
            author = book.author,
            subject = book.subject,
            is_lent = book.is_lent,
            released_at = book.released_at
        )

def delete_book(book_id: int, user: user_schema.User):
    book = BookModel.filter((BookModel.id == book_id) & (BookModel.user_id == user.id)).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found..."
        )

    book.delete_instance()