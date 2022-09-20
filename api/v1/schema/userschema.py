from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="namesurname@provider.co.uk"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="namesurname"
    )

class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )
    name: str = Field(...)
    surname: str = Field(...)
    is_active: bool = Field(...)

class AddUser(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="verystrongpass"
    )
