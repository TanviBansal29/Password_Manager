from fastapi import APIRouter, HTTPException, Depends, Response
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from utils.menu.menu_function import fetch_user
from blocklist import BLOCKLIST
from schemas.schemas import UserSchema
from schemas.schemas import LoginResponse
from starlette import status
from datetime import datetime, timedelta
from jose import jwt

router = APIRouter(tags=['Authentication'])
SECRET_KEY = "e0c5bd2b7eaece2c1f7a4e3b94a3d0e558fe6a0733a9af30d0d5f0c73d4e4d87"
ALGORITHM = 'HS256'


def create_access_token(user_id:int,role:str,expires_delta:timedelta):
    encode = {'sub':user_id, 'role':role}
    expires=datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY,algorithm = ALGORITHM)


@router.post("/login" ,response_model = LoginResponse, status_code = status.HTTP_200_OK )
def login_user(login_data: UserSchema):
    login_data = login_data.model_dump()
    username = login_data["username"]
    print(username)
    password = login_data["password"]
    print(password)
    data = fetch_user(username, password)
    print(data)
    if data:
        access_token = create_access_token(data[0],data[3] ,timedelta(minutes = 20))
        return {"access_token": access_token, "token_type": "Bearer"}
    #     raise HTTPException(401, "Invalid credentials.")
    else:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail= 'Invalid credentials')

    #     access_token = None   #fresh token generated from login in 
    #     refresh_token = None
    #     return {"access_token": access_token, "refresh_token": refresh_token}

# @router.post('/logout')
# def logout(claims)


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