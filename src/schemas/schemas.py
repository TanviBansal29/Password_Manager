from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str 
    password: str

class InformationSchema(BaseModel):
    username : str
    website : str
    email : str
    password : str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str