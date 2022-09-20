from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from api.v1.schema import userschema
from api.v1.service import userservice
from api.v1.service import authservice
from api.v1.schema.token import Token

from api.v1.utils.db import get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["users"]
)

@router.post(
    "/user/",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def add_user(user: userschema.AddUser = Body(...)):
    """
    ## Add a new user to database

    ### Args
    Receives fields in JSON format
    - name: User name
    - surname: User surname
    - email:  e-mail format username@provider.sufix
    - username: Unique username
    - password: Strong password for authentication
    - is_active: true or false

    ### Returns
    - user: User information
    """
    return userservice.add_user(user)

@router.post(
    "/login",
    tags=["users"],
    response_model=Token
)

async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Login to generate access token

    ### Args
    Receives as data:
    - username: username or email
    - password: password

    ### Returns
    - Access token and type
    """
    
    access_token = authservice.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")