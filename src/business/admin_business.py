from utils.custom_error import DataAlreadyExists, DataNotFoundError
from utils.database_connection import DatabaseConnection
from config.config import Config

class AdminBusiness:
    '''
    Admin Business class ti handle db call for admin routes'''

    def view_all_user_data(self):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            data = cursor.execute(Config.QUERY_TO_VIEW_ALL_USER_DATA).fetchall()
            if not data:
                raise DataNotFoundError("No data found")
            return data


    def view_data_by_user(self, user_id):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()     
            data = cursor.execute(Config.QUERY_TO_VIEW_DATA_BY_USER, (user_id, )).fetchall()
            if not data:
                raise DataNotFoundError("No data found")
            return data
            

    def view_user_data_by_website(self, website):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            data = cursor.execute(Config.QUERY_TO_VIEW_USER_DATA_BY_WEBSITE, (website, )).fetchall()
            if not data:
                raise DataNotFoundError("No data found")
            return data

    def create_user(self, username, password):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
            cursor.execute(Config.QUERY_TO_CREATE_USER,(username,password,))
        
    def delete_user(self, user_id):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
            cursor.execute(Config.QUERY_TO_DELETE_USER, (user_id, ))
            return {"message" : "User deleted successfully"}

    def delete_website_data(website):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
            cursor.execute(Config.QUERY_TO_DELETE_WEBSITE_DATA, (website, ))

    def fetch_username(self, username):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_CHECK_USERNAME, (username, ))
            record = cursor.fetchone()
            if record:
                raise DataAlreadyExists("Username already exists")
            return      
    