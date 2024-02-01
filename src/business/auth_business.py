from utils.custom_error import InvalidCredentials
from utils.menu.menu_function import fetch_user
from utils.tokens import create_access_token, create_refresh_token


class AuthBusiness:
    def login(login_data):
        username = login_data["username"]
        password = login_data["password"]

        data = fetch_user(username, password)
        if not data:
            raise InvalidCredentials
        
        access_token = create_access_token(
            identity = data[0],
            fresh = True,
            additional_claims = {"role" : data[3]}
        )
        
        refresh_token = create_refresh_token(
            identity = data[0],
            additional_claims = {"role": data[3]}
        )
        