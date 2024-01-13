from flask import request
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt
from utils.menu.menu_function import fetch_user
from blocklist import BLOCKLIST

blp = Blueprint("login", __name__)

@blp.post("/login")
def login_user():
    request_data = request.get_json()
    username = request_data["username"]
    password = request_data["password"]
    data = fetch_user(username, password)
    if not data:
        abort(401, message = "Invalid credentials.")
    else:
        access_token = create_access_token(identity = data[0], fresh = True, additional_claims= {"role" : data[4]})   #fresh token generated from login in 
        refresh_token = create_refresh_token(identity = data[0],additional_claims= {"role" : data[4]} )
        return {"access_token": access_token, "refresh_token": refresh_token}


@blp.post("/refresh")
@jwt_required(refresh=True)
def token_refresh():
    current_user = get_jwt_identity()  #retrieves the identity of the current user from the JWT. 
    #The identity is typically a unique identifier for the user, and it's stored in the JWT during authentication.
    new_token = create_access_token(identity = current_user, fresh = False) #creates a new access token for the current user. 
    #fresh is set to False, indicating that this token is not a fresh token. 
    #Fresh tokens used for actions that require a higher level of authentication, and are obtained during the initial login
    jti = get_jwt()["jti"]
    BLOCKLIST.add(jti)
    return {"access_token": new_token}