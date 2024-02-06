from typing import Annotated
from fastapi import APIRouter, Depends
from schemas.schemas import InformationSchema
from controllers.user_controller import UserController
from utils.tokens import get_jwt
from starlette import status

router = APIRouter(tags=["User"])
user_dependency = Annotated[dict, Depends(get_jwt)]


@router.post("/users/data", status_code=status.HTTP_201_CREATED)
def add_data(
    claims: user_dependency,
    new_data: InformationSchema,
):
    "user will add own data"
    user_id = claims.get("sub")
    user_obj = UserController(user_id, dict(new_data))
    return user_obj.add_data()


@router.get("/users/mydata", status_code=status.HTTP_200_OK)
def view_all_data(claims: user_dependency):
    print("ji")
    "user will see own data"
    user_id = claims.get("sub")
    user_obj = UserController(user_id)
    return user_obj.view_all_data()


@router.get("/users/mydata/website/{website}", status_code=status.HTTP_200_OK)
def view_data_by_website(claims: user_dependency, website: str):
    "user will see own data by website"
    user_id = claims.get("sub")
    user_obj = UserController(user_id)
    return user_obj.view_data_by_website(website)
