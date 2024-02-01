from fastapi import APIRouter, HTTPException
from controllers import admin_controller
from utils.menu.menu_function import fetch_username
from schemas.schemas import UserSchema

router =APIRouter(tags=['Admin'])

# def access_control(*role):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             jwt = get_jwt()
#             get_role = jwt["role"]
#             if get_role in role:
#                 return func(*args, **kwargs)
#             else:
#                 abort(401, message = "You are not authorized to access these resource.")
#         return wrapper
#     return inner


@router.post("/users")
def create_user(request_data: UserSchema):
    request_data = dict(request_data)
    username = request_data["username"]
    password = request_data["password"]
    user = fetch_username(username)
    if user:
        raise HTTPException(400, "User already exists")
        # abort(400, message = "User already exists.")
    admin_controller.create_user(username, password)
    return {'message' : 'User created'}


@router.get("/users")
# @jwt_required()
# @access_control("admin")
def view_all_user_data():
    data = admin_controller.view_all_user_data()
    if not data:
        raise HTTPException(404, "No data found for users.")
    return data


@router.get("/users/{user_id}")
# @jwt_required()
# @access_control("admin")
def view_data_by_user(user_id: int):
    data = admin_controller.view_data_by_user(user_id)
    if not data:
        raise HTTPException(404, f"No data found for user_id = {user_id}.")
    return data


@router.get("/users/website/{website}")
# @access_control("admin")
def view_user_data_by_website(website: str):
    print("hi")
    data = admin_controller.view_user_data_by_website(website)
    print(data)
    if not data:
        raise HTTPException(404, f"No data found for {website}.")
    return data 


@router.delete("/users/{user_id}")
# @jwt_required()
# @access_control("admin")
def delete_user(user_id: int):
    data = admin_controller.view_data_by_user(user_id)
    if data:
        admin_controller.delete_user(user_id)
        return {f'User with user_id = {user_id} deleted'}
    else:
        return {f'Data does not exists for user_id = {user_id}'}


@router.delete("/website/{website}")
# @jwt_required()
# @access_control("admin")
def delete_website_data(website : str):
    admin_controller.delete_website_data(website)
    return {'message': 'Users deleted'}

