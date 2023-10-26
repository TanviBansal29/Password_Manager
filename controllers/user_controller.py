from utils.database_connection import DatabaseConnection
from queries import queries

def create_user_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_ENALE_FOREIGN_KEY)
        cursor.execute(queries.QUERY_TO_CREATE_USERS_TABLE)
        


def create_credentials_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_ENALE_FOREIGN_KEY)
        cursor.execute(queries.QUERY_TO_CREATE_CREDENTIALS_TABLE)
        

def add_data(user_id, username, website, email, password):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_ENALE_FOREIGN_KEY)
        cursor.execute(queries.QUERY_TO_ADD_DATA, (user_id, username, website, email, password, ))
        

def view_all_data(user_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_VIEW_ALL_DATA, (user_id, ))
        data = cursor.fetchall()

    return data    


def view_data_by_website(user_id, website):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_VIEW_DATA_BY_WEBSITE, (user_id, website, ))
        data = cursor.fetchall()
        
    return data  
          

def view_data_by_email(user_id, email):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(queries.QUERY_TO_DATA_BY_EMAIL, (user_id, email, ))
        data = cursor.fetchall()
        
    return data  


def delete_data(user_id, website, email):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(queries.QUERY_TO_ENALE_FOREIGN_KEY)
        cursor.execute(queries.QUERY_TO_DELETE_DATA, (user_id, website, email, ))    
    