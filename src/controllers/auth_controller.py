from business.auth_business import AuthBusiness
from utils.custom_error import InvalidCredentials


class AuthController:
    '''
    LoginController class with Login method
    '''
    def __init__(self,login_data):
        self.username = login_data['username']
        self.password = login_data['password']
        self.obj_auth_business = AuthBusiness(self.username,self.password)

    def login(self): 
        '''Method for user login'''
        try:
            result = self.obj_auth_business.verify_user()

            if result:
                data = self.obj_auth_business.get_role()
                role = data["role"]
                user_id = data["user_id"]
                return self.obj_auth_business.login(role, user_id)
            
        except InvalidCredentials as e:
            return {"status" : 401 , "message": str(e)},401  