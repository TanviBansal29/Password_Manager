import sqlite3
from utils.custom_error import DataAlreadyExists, DataNotFoundError
from utils.database_connection import DatabaseConnection
from config.config import Config


class UserBusiness:

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def create_user_table():
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
            cursor.execute(Config.QUERY_TO_CREATE_USERS_TABLE)

    @staticmethod
    def create_credentials_table():
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
            cursor.execute(Config.QUERY_TO_CREATE_CREDENTIALS_TABLE)

    def add_data(self, user_id, username, website, email, password):
        try:
            with DatabaseConnection(Config.DATABASE_NAME) as connection:
                cursor = connection.cursor()
                cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
                cursor.execute(
                    Config.QUERY_TO_ADD_DATA,
                    (
                        user_id,
                        username,
                        website,
                        email,
                        password,
                    ),
                )
        except sqlite3.IntegrityError as e:
            raise DataAlreadyExists("Same username with website already exists")

    def view_all_data(self):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            data = cursor.execute(
                Config.QUERY_TO_VIEW_ALL_DATA, (self.user_id,)
            ).fetchall()
            if not data:
                raise DataNotFoundError("No data found")
            return data

    def view_data_by_website(self, website):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            data = cursor.execute(
                Config.QUERY_TO_VIEW_DATA_BY_WEBSITE,
                (
                    self.user_id,
                    website,
                ),
            ).fetchall()
            if not data:
                raise DataNotFoundError("No data found")
            return data

    def view_data_by_email(user_id, email):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()

            row = cursor.execute(
                Config.QUERY_TO_DATA_BY_EMAIL,
                (
                    user_id,
                    email,
                ),
            )
            if row.rowcount == -1:
                print(Config.NO_DATA)
            else:
                data = cursor.fetchall()
                print(data)

    def delete_data(user_id, website, email):
        with DatabaseConnection(Config.DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(Config.QUERY_TO_ENALE_FOREIGN_KEY)
            cursor.execute(
                Config.QUERY_TO_DELETE_DATA,
                (
                    user_id,
                    website,
                    email,
                ),
            )
