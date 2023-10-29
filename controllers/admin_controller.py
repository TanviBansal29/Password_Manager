from utils.database_connection import DatabaseConnection
from queries import queries
from config.config import Config

def view_all_user_data():
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
            print(Config.NO_DATA)
        else:
            data = cursor.fetchall()
            print(data)

    

def view_user_data_by_website(website):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        row = cursor.execute(Config.QUERY_TO_VIEW_USER_DATA_BY_WEBSITE, (website, ))
        print(row.rowcount)
        if row.rowcount == -1:
            print(Config.NO_DATA)
        else:
            print("hello")
            data = cursor.fetchall()
            print(data)
    
    
def create_user(username, password):
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
    