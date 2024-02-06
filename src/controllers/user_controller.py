import sqlite3

from fastapi import HTTPException
from business.user_business import UserBusiness
from utils.custom_error import DataAlreadyExists, DataNotFoundError


class UserController:
    """
    User Controller class with user methods"""

    def __init__(self, user_id, user_data=None):
        self.user_data = user_data
        self.user_id = user_id
        self.obj_user_business = UserBusiness(self.user_id)

    def add_data(self):
        """Method to add user data"""
        try:
            user_id = self.user_id
            username = self.user_data["username"]
            website = self.user_data["website"]
            email = self.user_data["email"]
            password = self.user_data["password"]

            self.obj_user_business.add_data(user_id, username, website, email, password)
            return {"message": "Successfully added data"}
        except DataAlreadyExists as e:
            raise HTTPException(status_code=409, detail=str(e))

    def view_all_data(self):
        """Method to add user data"""

        try:
            data = self.obj_user_business.view_all_data()
            return data
        except DataNotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def view_data_by_website(self, website):
        """Method to view user data by website"""

        try:
            data = self.obj_user_business.view_data_by_website(website)
            return data
        except DataNotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
