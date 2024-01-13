from utils.menu import menu_function

def test_admin_view_input(mocker, capsys):
    mocker.patch('builtins.input', side_effect = ['1', '2', 'test_user_id', '3', 'test_website_name', 't', 'q'])
    mocker.patch('utils.menu.menu_function.admin_controller.view_all_user_data', return_value = "test_data")
    mocker.patch('utils.menu.menu_function.admin_controller.view_data_by_user', return_value = "test_data1")
    mocker.patch('utils.menu.menu_function.admin_controller.view_user_data_by_website', return_value = "test_data2")
    menu_function.admin_view_input()
    captured = capsys.readouterr()
    assert "test_data" in captured.out
    assert "test_data1" in captured.out

def test_admin_delete_input(mocker):
    mocker.patch('builtins.input', side_effect = ['1', 'test_user_id', '2', 'test_website_name', 't', 'q'])
    mocker.patch('utils.menu.menu_function.admin_controller.delete_user', return_value = "test_data")
    mocker.patch('utils.menu.menu_function.admin_controller.delete_website_data', return_value = "test_data1")
    menu_function.admin_delete_input()

def test_user_view_input(mocker):
    mocker.patch('builtins.input', side_effect = ['1', '2', 'test_website', '3', 'test_email', 't', 'q'])
    mocker.patch('utils.menu.menu_function.user_controller.view_all_data', return_value = "test_data")
    mocker.patch('utils.menu.menu_function.user_controller.view_data_by_website', return_value = "test_data1")
    mocker.patch('utils.menu.menu_function.user_controller.view_data_by_email', return_value = "test_data2")
    menu_function.user_view_input("test_user_id")

def test_fetch_user(mocker):
    mock_db_conn = mocker.patch('utils.menu.menu_function.DatabaseConnection')
    mock_cursor = mocker.MagicMock()
    mock_db_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor
    mocker.patch('utils.menu.menu_function.Config').QUERY_TO_VERIFY_LOGIN
    mock_cursor.fetchone.return_value = "test_result"
    result = menu_function.fetch_user("test_username", "test_password")
    assert result == "test_result"

def test_update_password(mocker):
    mock_db_conn =  mocker.patch("utils.menu.menu_function.DatabaseConnection")
    mock_cursor = mocker.MagicMock()
    mock_db_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor
    mocker.patch('utils.menu.menu_function.Config').QUERY_TO_UPDATE_DEFAULT_PASSWORD = "test_query"
    menu_function.update_password("test_user_id", "test_password")

def test_fetch_username(mocker):
    mock_db_conn =  mocker.patch("utils.menu.menu_function.DatabaseConnection")
    mock_cursor = mocker.MagicMock()
    mock_db_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor
    mocker.patch('utils.menu.menu_function.Config').QUERY_TO_CHECK_USERNAME = "test_query"
    mock_cursor.fetchone.return_value = "test_record"
    result = menu_function.fetch_username("test_username")
    assert result == "test_record"





