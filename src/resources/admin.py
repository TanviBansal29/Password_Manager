from fastapi import APIRouter, HTTPException
from controllers import admin_controller
from utils.menu.menu_function import fetch_username

router =APIRouter(prefix='/admin', tags=['admin'])

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


@blp.route("/users")
@jwt_required()
@access_control("admin")
def view_all_user_data():
    data = admin_controller.view_all_user_data()
    if not data:
        abort(404, message = "No data found for users.")
    return data


@blp.route("/users/<int:user_id>")
@jwt_required()
@access_control("admin")
def view_data_by_user(user_id):
    data = admin_controller.view_data_by_user(user_id)
    if not data:
        abort(404, message = f"No data found for user_id = {user_id}.")
    return data


@blp.route("/users/<string:website>")
@access_control("admin")
def view_user_data_by_website(website):
    data = admin_controller.view_user_data_by_website(website)
    if not data:
        abort(404, message = f"No data found for {website}.")
    return data 


@blp.delete("/users/<int:user_id>")
@jwt_required()
@access_control("admin")
def delete_user(user_id):
    admin_controller.delete_user(user_id)
    return {f'message': 'User with user_id = {user_id} deleted'}


@blp.delete("/website/<string:website>")
@jwt_required()
@access_control("admin")
def delete_website_data(website):
    admin_controller.delete_website_data(website)
    return {'message': 'Users deleted'}

