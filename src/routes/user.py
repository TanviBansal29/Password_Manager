from typing import Annotated
from fastapi import APIRouter, Depends
from schemas.schemas import InformationSchema
from controllers.user_controller import UserController
from utils.tokens import get_jwt

router = APIRouter(tags=['User'])
user_dependency = Annotated[dict, Depends(get_jwt)]

@router.post("/users/data")
def add_data(claims: user_dependency, new_data : InformationSchema):
    'user will add own data'
    user_id = claims.get('sub')
    user_obj = UserController(user_id, dict(new_data))
    return user_obj.add_data()


@router.get("/users/mydata")
def view_all_data(claims: user_dependency):
    'user will see own data'
    user_id = claims.get('sub')
    user_obj = UserController(user_id)
    return user_obj.view_all_data()


@router.get("/users/mydata/website/<website>")
def view_data_by_website(claims: user_dependency , website :str):
    'user will see own data by website'
    user_id = claims.get('sub')
    user_obj = UserController(user_id)
    return user_obj.view_data_by_website(website)


