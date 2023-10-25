from utils.database_connection import DatabaseConnection

def view_all_user_data():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, username, website, email FROM users")
        data = cursor.fetchall()
        return data


def view_data_by_user(user_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, username, website, email FROM users WHERE user_id = ?", (user_id, ))
        data = cursor.fetchall()
        return data
    

def view_user_data_by_website(website):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, username, website, email FROM users WHERE website = ?", (website, ))
        data = cursor.fetchall()
        return data
    
    
def create_user():
    pass

def delete_user():
    pass

def delete_website_data():
    pass