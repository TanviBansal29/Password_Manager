from controllers import admin_controller

def test_view_all_user_data(mocker):
    moc_db_conn = mocker.patch("controllers.admin_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    moc_cursor.fetchall.return_value = [("tanvi"),("bansal")]
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_VIEW_ALL_USER_DATA = "test_query"

    result = admin_controller.view_all_user_data()
    assert result == [("tanvi"),("bansal")]


def test_view_data_by_user(mocker, capsys):
    moc_db_conn = mocker.patch("controllers.admin_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    moc_cursor.fetchall.return_value = [("tanvi",),("bansal",)]
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_VIEW_ALL_USER_DATA = "test_query"

    admin_controller.view_data_by_user("test_user_id")

    captured = capsys.readouterr()
    assert str([('tanvi',), ('bansal',)]) in captured.out

def test_view_user_data_by_website(mocker, capsys):
    moc_db_conn = mocker.patch("controllers.admin_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    moc_cursor.fetchall.return_value = [("tanvi",),("bansal",)]
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_VIEW_ALL_USER_DATA = "test_query"

    admin_controller.view_user_data_by_website("test_website")

    captured = capsys.readouterr()
    assert str([('tanvi',), ('bansal',)]) in captured.out

def test_create_user(mocker):
    moc_db_conn = mocker.patch("controllers.admin_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_VIEW_ALL_USER_DATA = "test_query"
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_ENALE_FOREIGN_KEY = "test_query1"
    admin_controller.create_user("username", "password")

def test_delete_user(mocker):
    moc_db_conn = mocker.patch("controllers.admin_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_DELETE_USER = "test_query"
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_ENALE_FOREIGN_KEY = "test_query1"
    admin_controller.delete_user("user_id")


def test_delete_website_data(mocker):
    moc_db_conn = mocker.patch("controllers.admin_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_VIEW_ALL_USER_DATA = "test_query"
    mocker.patch("controllers.admin_controller.Config").QUERY_TO_ENALE_FOREIGN_KEY = "test_query1"
    admin_controller.delete_website_data("wesbite")
    
# @pytest.fixture
# def mock_database_connection(mocker):
#     return mocker.patch('your_module.DatabaseConnection')

# def test_create_user(mock_database_connection, mocker):
#     # Mock the execute method of the cursor
#     mock_cursor = mocker.MagicMock()
#     mock_database_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

#     # Mock the execute method to simulate the successful execution
#     mock_cursor.execute.side_effect = [None, None]  # You can customize this based on your needs

#     # Call the function under test
#     create_user("test_user", "test_password")

#     # Ensure that the DatabaseConnection class is instantiated
#     mock_database_connection.assert_called_once_with(Config.DATABASE_NAME)

#     # Ensure that __enter__ is called on the DatabaseConnection instance
#     mock_db_conn_instance = mock_database_connection.return_value.__enter__.return_value
#     mock_db_conn_instance.cursor.assert_called_once()

#     # Ensure that execute is called on the cursor with the correct queries and parameters
#     expected_calls = [
#         mocker.call(Config.QUERY_TO_ENALE_FOREIGN_KEY),
#         mocker.call(Config.QUERY_TO_CREATE_USER, ("test_user", "test_password"))
#     ]
#     mock_cursor.execute.assert_has_calls(expected_calls, any_order=False)

#     # Ensure that __exit__ is called on the DatabaseConnection instance
#     mock_db_conn_instance.__exit__.assert_called_once_with(None, None, None)
