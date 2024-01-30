from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str 
    password: str

class InformationSchema(BaseModel):
    username : str
    website : str
    email : str
    password : str