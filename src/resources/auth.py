from fastapi import APIRouter, HTTPException, Depends, Response
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from utils.menu.menu_function import fetch_user
from blocklist import BLOCKLIST
from schemas.schemas import UserSchema

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login_user(login_data: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response):
    pass
    # login_data = dict(login_data)
    # username = login_data["username"]
    # password = login_data["password"]
    # data = fetch_user(username, password)
    # if not data:
    #     raise HTTPException(401, "Invalid credentials.")
    # else:
    #     access_token = None   #fresh token generated from login in 
    #     refresh_token = None
    #     return {"access_token": access_token, "refresh_token": refresh_token}


@router.post("/refresh")
# @jwt_required(refresh=True)
def token_refresh():
    # current_user = get_jwt_identity()  #retrieves the identity of the current user from the JWT. 
    # #The identity is typically a unique identifier for the user, and it's stored in the JWT during authentication.
    # new_token = create_access_token(identity = current_user, fresh = False) #creates a new access token for the current user. 
    # #fresh is set to False, indicating that this token is not a fresh token. 
    # #Fresh tokens used for actions that require a higher level of authentication, and are obtained during the initial login
    # jti = get_jwt()["jti"]
    # BLOCKLIST.add(jti)
    new_token = None
    return {"access_token": new_token}


@router.post('/logout')
def logout():
    # jti = get_jwt().get('jti')
    jti = None
    BLOCKLIST.add(jti)
    return {'message': 'Successfully logged out'}