from utils.database_connection import DatabaseConnection

def create_user_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                            user_id TEXT,
                            username TEXT,
                            website TEXT,
                            email TEXT,
                            password TEXT,
                            PRIMARY KEY(user_id, username, website)
                        )'''
                       )
        

def add_data(user_id, username, website, email, password):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (user_id, username, website, email, password))
        

def view_all_data(user_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id, ))
        data = cursor.fetchall()

    return data    


def view_data_by_website(user_id, website):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id = ? AND website = ?", (user_id, website))
        data = cursor.fetchall()
        
    return data  
          

def view_data_by_email(user_id, email):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id = ? AND email = ?", (user_id, email))
        data = cursor.fetchall()
        
    return data  


def delete_data(user_id, website, email):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM users WHERE user_id = ? AND website = ? AND email = ?", (user_id, website, email))    
    