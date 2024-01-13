from controllers import user_controller

def test_create_user_table(mocker):
    moc_db_conn = mocker.patch("controllers.user_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    mocker.patch("controllers.user_controller.Config").QUERY_TO_CREATE_USERS_TABLE = "test_query"
    mocker.patch("controllers.user_controller.Config").QUERY_TO_ENALE_FOREIGN_KEY = "test_query1"
    user_controller.create_user_table()

def test_create_credentials_table(mocker):
    moc_db_conn = mocker.patch("controllers.user_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    mocker.patch("controllers.user_controller.Config").QUERY_TO_CREATE_CREDENTIALS_TABLE = "test_query"
    mocker.patch("controllers.user_controller.Config").QUERY_TO_ENALE_FOREIGN_KEY = "test_query1"
    user_controller.create_credentials_table()

def test_add_data(mocker):
    moc_db_conn = mocker.patch("controllers.user_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    mocker.patch("controllers.user_controller.Config").QUERY_TO_ADD_DATA = "test_query"
    mocker.patch("controllers.user_controller.Config").QUERY_TO_ENALE_FOREIGN_KEY = "test_query1"
    user_controller.add_data("user_id", "username", "website", "email", "password")

def test_view_all_data(mocker, capsys):
    moc_db_conn = mocker.patch("controllers.user_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    moc_cursor.fetchall.return_value = [("tanvi",),("bansal",)]
    mocker.patch("controllers.user_controller.Config").QUERY_TO_VIEW_ALL_DATA = "test_query"

    user_controller.view_all_data("user_id")

    captured = capsys.readouterr()
    assert str([('tanvi',), ('bansal',)]) in captured.out

def test_view_data_by_website(mocker, capsys):
    moc_db_conn = mocker.patch("controllers.user_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    moc_cursor.fetchall.return_value = [("tanvi",),("bansal",)]
    mocker.patch("controllers.user_controller.Config").QUERY_TO_VIEW_ALL_DATA = "test_query"

    result = user_controller.view_data_by_website("user_id", "website")
    assert result == [("tanvi",),("bansal",)]

def test_view_data_by_email(mocker, capsys):
    moc_db_conn = mocker.patch("controllers.user_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    moc_cursor.fetchall.return_value = [("tanvi",),("bansal",)]
    mocker.patch("controllers.user_controller.Config").QUERY_TO_VIEW_ALL_DATA = "test_query"

    user_controller.view_data_by_email("user_id", "email")

    captured = capsys.readouterr()
    assert str([('tanvi',), ('bansal',)]) in captured.out

def test_delete_data(mocker):
    moc_db_conn = mocker.patch("controllers.user_controller.DatabaseConnection")
    moc_cursor = mocker.MagicMock()
    moc_db_conn.return_value.__enter__.return_value.cursor.return_value = moc_cursor
    mocker.patch("controllers.user_controller.Config").QUERY_TO_DELETE_DATA = "test_query"
    mocker.patch("controllers.user_controller.Config").QUERY_TO_ENALE_FOREIGN_KEY = "test_query1"
    user_controller.delete_data("user_id", "website", "email")



