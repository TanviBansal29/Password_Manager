from fastapi import APIRouter, HTTPException, Depends, Response
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from controllers.auth_controller import AuthController
from blocklist import BLOCKLIST
from utils.tokens import get_jwt


router = APIRouter(tags=['Authentication'])
user_dependency = Annotated[dict, Depends(get_jwt)]

@router.post('/login')
def login(login_data : Annotated[OAuth2PasswordRequestForm, Depends()]):
    'Login method'
    auth_obj = AuthController(login_data)
    return auth_obj.login()


@router.post("/refresh")
def token_refresh(claims: user_dependency):
    '''Issue a non fresh access token from a refresh token'''

    user_id = claims.get("sub")
    role = claims.get("role")
    auth_obj = AuthController()
    return auth_obj.refresh(user_id, role)


# @router.post('/logout')
# def logout():
#     '''Method to log out currently logged in user'''


#     auth_obj = AuthController()
#     return auth_obj.logout()
