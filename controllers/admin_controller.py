from utils.database_connection import DatabaseConnection
from queries import queries

def view_all_user_data():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
  
        cursor.execute(queries.QUERY_TO_VIEW_ALL_USER_DATA)
        data = cursor.fetchall()
        return data


def view_data_by_user(user_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute(queries.QUERY_TO_VIEW_DATA_BY_USER, (user_id, ))
        data = cursor.fetchall()
        return data
    

def view_user_data_by_website(website):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_VIEW_USER_DATA_BY_WEBSITE, (website, ))
        data = cursor.fetchall()
        return data
    
    
def create_user(username, password):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_ENALE_FOREIGN_KEY)
        cursor.execute(queries.QUERY_TO_CREATE_USER,(username,password,))
    

def delete_user(user_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_ENALE_FOREIGN_KEY)
        cursor.execute(queries.QUERY_TO_DELETE_USER, (user_id, ))

def delete_website_data(website):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_ENALE_FOREIGN_KEY)
        cursor.execute(queries.QUERY_TO_DELETE_USER_DATA, (website, ))
    