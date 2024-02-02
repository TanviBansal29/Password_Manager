from config.config import Config
from utils.custom_error import InvalidCredentials
from utils.database_connection import DatabaseConnection
# from utils.menu.menu_function import fetch_user
from utils.tokens import create_access_token, create_refresh_token


class AuthBusiness:

    def login(self,role, user_id):
        '''Method to login user'''

        access_token = create_access_token(
            identity = user_id,
            fresh = True,
            additional_claims = {"role" : role}
        )
        
        refresh_token = create_refresh_token(
            identity = user_id,
            additional_claims = {"role": role}
        )

        token_data = {'access_token': access_token, 'refresh_token': refresh_token, 'message': "LOGGED IN SUCCESSFULLY"}
        return token_data

    def refresh(self, user_id, role):
        '''Method to get non fresh access token from refresh token'''

        new_access_token = create_access_token(
            identity = user_id,
            fresh = False,
            additional_claims = {"role" : role}
        )
        print(new_access_token)

        return {"access_token": new_access_token}

    def fetch_user(self, login_data):
        '''Method to fetch data if login credentials are valid'''

        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_VERIFY_LOGIN, (login_data.username, login_data.password, ))
            result = cursor.fetchone()
            if not result:
                raise InvalidCredentials("Invalid Credentials")
            return result 
        
        
