# Pydantic
from pydantic import BaseModel
from pydantic import Field


class AddBook(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=60,
        example="The life book"
    )
    author: str = Field(...)
    subject: str = Field(...)
    is_lent: bool = Field(default=False)
    released_at: int = Field(...)

class Book(AddBook):
    id: int = Field(...)
    user: str = Field(...)
