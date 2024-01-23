from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from controllers import user_controller
from resources.admin import access_control

blp = Blueprint("user", __name__)

@blp.post("/users/data")
@jwt_required()
@access_control("admin", "user")
def add_data():
    request_data = request.get_json()
    user_id = get_jwt_identity()
    username = request_data["username"]
    website = request_data["password"]
    email = request_data["email"]
    password = request_data["password"]
    user_controller.add_data(user_id, username, website, email, password)
    return {'message' : 'Successfully added data'}

@blp.route("/users/mydata")
@jwt_required()
@access_control("admin", "user")
def view_all_data():
    user_id = get_jwt_identity()
    data = user_controller.view_all_data(user_id)
    if not data:
        abort(404, message = "No data found")
    return data

