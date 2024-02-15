from fastapi import HTTPException
from business.admin_business import AdminBusiness
from utils.custom_error import DataAlreadyExists, DataNotFoundError


class AdminController:
    """
    Admin Controller class with admin methods
    """

    def __init__(self):
        self.admin_business = AdminBusiness()

    def register(self, register_data):
        """Method to create a new user"""

        try:
            data = self.admin_business.fetch_username(register_data.username)
            if not data:
                self.admin_business.create_user(
                    register_data.username, register_data.password
                )
                return {"message": "User created successfully"}
        except DataAlreadyExists as e:
            raise HTTPException(status_code=409, detail=str(e))

    def view_all_user_data(self):
        """Method to view all users data"""

        try:
            data = self.admin_business.view_all_user_data()
            return data
        except DataNotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def view_data_by_user(self, user_id):
        """Method to view all users data"""

        try:
            data = self.admin_business.view_data_by_user(user_id)
            return data
        except DataNotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def view_user_data_by_website(self, website):
        """Method to view all users data"""

        try:
            data = self.admin_business.view_user_data_by_website(website)
            return data
        except DataNotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def delete_user_data(self, user_id):
        """Method to view all users data"""

        try:
            data = self.admin_business.view_data_by_user(user_id)
            if data:
                return self.admin_business.delete_user(user_id)
        except DataNotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
