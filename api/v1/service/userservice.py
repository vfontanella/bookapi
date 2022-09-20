from fastapi import HTTPException, status

from api.v1.model.usermodel import User as UserModel
from api.v1.schema import userschema
from api.v1.service.authservice import get_password_hash

def add_user(user: userschema.AddUser):
    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered!"
        if get_user.username == user.username:
            msg = "Username already registered!"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        name=user.name,
        surname=user.surname,
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )
    db_user.save()

    return userschema.User(
        id = db_user.id,
        name = db_user.name,
        surname = db_user.surname,
        username = db_user.username,
        email = db_user.email
    )