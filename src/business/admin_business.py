from utils.custom_error import DataAlreadyExists
from utils.database_connection import DatabaseConnection
from config.config import Config

class AdminBusiness:
    def view_all_user_data():
        print(Config.DATABASE_NAME)
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
    
            row= cursor.execute(Config.QUERY_TO_VIEW_ALL_USER_DATA)
            if row.rowcount == 0:
                print(Config.NO_DATA)
            data = cursor.fetchall()
            return data

    def view_data_by_user(user_id):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()     
            row = cursor.execute(Config.QUERY_TO_VIEW_DATA_BY_USER, (user_id, ))
            if row.rowcount == 0:
                return
            else:
                data = cursor.fetchall()
                return data 

    def view_user_data_by_website(website):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            data = cursor.execute(Config.QUERY_TO_VIEW_USER_DATA_BY_WEBSITE, (website, )).fetchall()
            return data

    def create_user(self, username, password):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
            cursor.execute(Config.QUERY_TO_CREATE_USER,(username,password,))
        
    def delete_user(user_id):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
            cursor.execute(Config.QUERY_TO_DELETE_USER, (user_id, ))

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
                raise DataAlreadyExists("Useranme already exists")
            return      
    