import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import ExpiredSignatureError, JWTError, jwt
from typing import Annotated, Dict

SECRET_KEY = "e0c5bd2b7eaece2c1f7a4e3b94a3d0e558fe6a0733a9af30d0d5f0c73d4e4d87"
ALGORITHM = 'HS256'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/login")

def create_access_token(identity:str, fresh: bool, additional_claims: Dict):
    '''Create access token'''

    iat = datetime.utcnow()
    exp = iat + timedelta(minutes=15)
    payload = {
        'fresh': fresh,
        'iat': iat,
        'type': 'access',
        'sub': identity,
        'exp': exp
    }
    payload.update(additional_claims)
    access_token = jwt.encode(payload, SECRET_KEY, ALGORITHM )
    return access_token


def create_refresh_token(identity:str, additional_claims: Dict):
    'Create a refresh token'

    iat = datetime.utcnow()
    exp = iat + timedelta(minutes=30)
    payload = {
        'fresh': False,
        'iat': iat,
        'type': 'refresh',
        'sub': str(identity),
        'exp': exp
    }
    payload.update(additional_claims)
    refresh_token = jwt.encode(payload, SECRET_KEY)
    return refresh_token

def get_jwt(token: Annotated[str, Depends(oauth2_scheme)]):
    '''Returns claims of a jwt token'''
    payload = jwt.decode(token, SECRET_KEY)
    return payload