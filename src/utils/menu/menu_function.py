from controllers import admin_controller, user_controller
from utils.database_connection import DatabaseConnection
from config.config import Config


def admin_view_input():
    admin_view_input = input(Config.ADMIN_VIEW_PROMPTS)

    while admin_view_input != 'q':
        match admin_view_input :
            case '1':
                data = admin_controller.view_all_user_data()
                print(data)
            case '2':
                user_id = input(Config.ENTER_USERID)
                data = admin_controller.view_data_by_user(user_id)
                print(data)
                
            case '3':
                website = input(Config.ENTER_WEBSITE)
                admin_controller.view_user_data_by_website(website)
            case _:
                print(Config.INVALID_PROMPT)

        admin_view_input = input(Config.ADMIN_VIEW_PROMPTS)        


def admin_delete_input():
    admin_delete_input = input(Config.ADMIN_DELETE_PROMPTS) 

    while admin_delete_input != 'q':
        match admin_delete_input :
            case '1':
                user_id = input(Config.ENTER_USERID)
                admin_controller.delete_user(user_id)
            case '2':
                website = input(Config.ENTER_WEBSITE)
                admin_controller.delete_website_data(website)
            case _:
                print(Config.INVALID_PROMPT)

        admin_delete_input = input(Config.ADMIN_DELETE_PROMPTS)


def user_view_input(user_id):
    user_view_input = input(Config.USER_VIEW_PROMPTS)

    while user_view_input != 'q':
        match user_view_input:
            case '1':
                user_controller.view_all_data(user_id)
            case '2':
                website = input(Config.ENTER_WEBSITE)
                user_controller.view_data_by_website(user_id, website)
            case '3':
                email = input(Config.ENTER_EMAIL)
                user_controller.view_data_by_email(user_id, email)
            case _:
                print(Config.INVALID_PROMPT)

        user_view_input = input(Config.USER_VIEW_PROMPTS)    

        
def update_password(user_id, password):
    with DatabaseConnection(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_UPDATE_DEFAULT_PASSWORD, (password, user_id, ))

        





       
