QUERY_TO_CREATE_USERS_TABLE = '''CREATE TABLE IF NOT EXISTS users(
                            user_id INTEGER,
                            username TEXT,
                            website TEXT,
                            email TEXT,
                            password TEXT,
                            PRIMARY KEY(username, website)
                            FOREIGN KEY (user_id) REFERENCES credentials(user_id) ON DELETE CASCADE
                        )'''


QUERY_TO_CREATE_CREDENTIALS_TABLE = '''CREATE TABLE IF NOT EXISTS credentials(
                                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        user_name TEXT,
                                        password TEXT,
                                        role TEXT,
                                        is_default INTEGER
                                    )'''


QUERY_TO_VIEW_ALL_USER_DATA = '''SELECT user_id, username, website, email FROM users
                            '''


QUERY_TO_VIEW_DATA_BY_USER = '''SELECT user_id, username, website, email FROM users WHERE user_id = ?
                            '''


QUERY_TO_VIEW_USER_DATA_BY_WEBSITE = '''SELECT user_id, username, website, email FROM users WHERE website = ?'''


QUERY_TO_CREATE_USER = '''INSERT INTO credentials (username, password) VALUES (?, ?)
                        '''


QUERY_TO_DELETE_USER = '''DELETE FROM users WHERE user_id = ?
                        '''


QUERY_TO_DELETE_USER_DATA = '''"DELETE FROM users WHERE website = ?
                            '''


QUERY_TO_ENALE_FOREIGN_KEY = '''PRAGMA foreign_keys = 1
                            '''


QUERY_TO_ADD_DATA = '''INSERT INTO users VALUES (?, ?, ?, ?, ?)
                    '''


QUERY_TO_VIEW_ALL_DATA = '''SELECT * FROM users WHERE user_id = ?
                        '''


QUERY_TO_VIEW_DATA_BY_WEBSITE = '''SELECT * FROM users WHERE user_id = ? AND website = ?
                                '''


QUERY_TO_DATA_BY_EMAIL ='''SELECT * FROM users WHERE user_id = ? AND email = ?
                        '''


QUERY_TO_DELETE_DATA = '''DELETE FROM users WHERE user_id = ? AND website = ? AND email = ?
                        '''


QUERY_TO_VERIFY_LOGIN = '''SELECT * FROM credentials WHERE username = ? AND password = ?
                        '''


QUERY_TO_UPDATE_DEFAULT_PASSWORD = '''UPDATE credentials
                                      SET password = ?, is_default = 1
                                      WHERE user_id = ?
                                   '''

QUERY_TO_CHECK_USERNAME = '''SELECT username FROM credentials 
                            WHERE username = ?'''
