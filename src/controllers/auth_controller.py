from business.auth_business import AuthBusiness
from utils.custom_error import InvalidCredentials

class AuthController:
    '''
    LoginController class with Login method
    '''
    def __init__(self, login_data=None):
        self.login_data = login_data
        self.obj_auth_business = AuthBusiness()

    def login(self): 
        '''Method for user login'''
        try:
            data = self.obj_auth_business.fetch_user(self.login_data)

            if data:
                role = data[3]
                user_id = data[0]
                return self.obj_auth_business.login(role, user_id)
            
        except InvalidCredentials as e:
            return {"status" : 401 , "message": str(e)},401  
        
    def refresh(self, user_id: str, role: str):
        '''Method to get non fresh access token from refresh token'''
        data = self.obj_auth_business.refresh(user_id, role)
        return data