from business.admin_business import AdminBusiness
from utils.custom_error import DataAlreadyExists


class AdminController:
    
    def __init__(self):
        self.admin_business = AdminBusiness()

    def register(self, register_data):
        '''Method to create a new user'''
        print("hello")
        try:
            data = self.admin_business.fetch_username(register_data.username)
            if not data:
                self.admin_business.create_user(register_data.username, register_data.password)
                return {"message": "User created successfully"}
        except DataAlreadyExists:
            return {"message" : "User"}