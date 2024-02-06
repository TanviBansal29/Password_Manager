import pytest
from business.user_business import UserBusiness

from config.config import Config
from utils.database_connection import DatabaseConnection


@pytest.fixture(scope="package", autouse=True)
def create_test_db(package_mocker):
    package_mocker.patch.object(Config, "DATABASE_NAME", "tests/test_routes/testdb.db")
    UserBusiness.create_user_table()
    UserBusiness.create_credentials_table()


@pytest.fixture(scope="package", autouse=True)
def insert_into_table():
    with DatabaseConnection("tests/test_routes/testdb.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO credentials (username, password, role, is_default) VALUES (?, ?, ?, ?)",
            ("Tanvibansal", "Tanvibansal12@", "role", "1"),
        )
        cursor.execute(
            Config.QUERY_TO_ADD_DATA,
            (
                1,
                "tbansal",
                "amazon",
                "Tanvibansal2020@gmail.com",
                "tbansal12@",
            ),
        )

    yield
    with DatabaseConnection("tests/test_routes/testdb.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE credentials")
        cursor.execute("DROP TABLE users")
