from fastapi import APIRouter, HTTPException
from controllers import admin_controller
# from utils.menu.menu_function import fetch_username
from schemas.schemas import InformationSchema
from controllers import user_controller
# from resources.admin import access_control

router = APIRouter(tags=['User'])

@router.post("/users/data")
# @jwt_required()
# @access_control("admin", "user")
def add_data(new_data : InformationSchema):
    new_data = dict(new_data)
    # user_id = get_jwt_identity()
    user_id = None
    username = new_data["username"]
    website = new_data["password"]
    email = new_data["email"]
    password = new_data["password"]
    user_controller.add_data(user_id, username, website, email, password)
    return {'message' : 'Successfully added data'}


@router.get("/users/mydata")
# @jwt_required()
# @access_control("admin", "user")
def view_all_data():
    # user_id = get_jwt_identity()
    user_id = None
    data = user_controller.view_all_data(user_id)
    if not data:
        raise HTTPException(404, "No data found")
    return data

