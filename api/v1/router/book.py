from fastapi import APIRouter, Depends, Body
from fastapi import Query
from fastapi import Path
from fastapi import status

from api.v1.schema import bookschema
from api.v1.service import bookservice
from api.v1.utils.db import get_db
from api.v1.schema.userschema import User
from api.v1.service.authservice import get_current_user

from typing import List, Optional

router = APIRouter(prefix="/api/v1/book")

@router.post(
    "/",
    tags=["book"],
    status_code=status.HTTP_201_CREATED,
    response_model=bookschema.Book,
    dependencies=[Depends(get_db)]
)
def create_book(
    book: bookschema.BookCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return bookservice.create_book(book, current_user)

@router.get(
    "/",
    tags=["book"],
    status_code=status.HTTP_200_OK,
    response_model=List[bookschema.Book],
    dependencies=[Depends(get_db)]
)
def get_books(
    is_lent: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return bookservice.get_books(current_user, is_lent)

@router.get(
    "/{book_id}",
    tags=["book"],
    status_code=status.HTTP_200_OK,
    response_model=bookschema.Book,
    dependencies=[Depends(get_db)]
)

def get_book(
    book_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return bookservice.get_book(book_id, current_user)

@router.patch(
    "/{task_id}/mark_done",
    tags=["to-do"],
    status_code=status.HTTP_200_OK,
    response_model=todo_schema.Todo,
    dependencies=[Depends(get_db)]
)
def mark_task_done(
    task_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return todo_service.update_status_task(True, task_id, current_user)

@router.patch(
    "/{task_id}/unmark_done",
    tags=["to-do"],
    status_code=status.HTTP_200_OK,
    response_model=todo_schema.Todo,
    dependencies=[Depends(get_db)]
)
def unmark_task_done(
    task_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return todo_service.update_status_task(False, task_id, current_user)

@router.delete(
    "/{task_id}/",
    tags=["to-do"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_task(
    task_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    todo_service.delete_task(task_id, current_user)

    return {
        'msg': 'Task has been deleted successfully'
    }