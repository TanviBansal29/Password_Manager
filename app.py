from controllers import user_controller
from controllers import admin_controller
from utils.menu import menu_function
from config.config import Config
# from utils import encrypt

def menu():
    print(Config.WELCOME_MESSAGE)
    while True:
        username = input(Config.ENTER_USERNAME)
        password = input(Config.ENTER_PASSWORD)
        # cipher_password = encrypt.encrypt_password(password)
        role = menu_function.fetch_user(username,password)
        if role != None:
            break
    if role[4] == 'admin':
        # admin logic
        print(Config.WELCOME_ADMIN)
        admin_input = input(Config.ADMIN_PROMPTS)
        while admin_input != 'q' :
            match admin_input:
                case '1':
                    menu_function.admin_view_input()
                case '2':
                    while True:
                        username = input(Config.SET_USERNAME)
                        if menu_function.fetch_username(username):
                            print(Config.USERNAME_ERROR)
                        else:
                            break    
                    password = input(Config.SET_PASSWORD)
                    # cipher_password = encrypt.encrypt_password(password)
                    admin_controller.create_user(username,password)
                case '3':
                    menu_function.admin_delete_input()
                case _:
                    print(Config.INVALID_PROMPT)      

            admin_input = input(Config.ADMIN_PROMPTS)
    else:
        # user logic
        is_default = role[3]
        user_id = role[0]
        if is_default == 0:
            print(Config.UPDATE_PASSWORD)
            new_password = input(Config.NEW_PASSWORD)
            # cipher_password = encrypt.encrypt_password(new_password)
            menu_function.update_password(user_id,new_password)
        else:    
            print(Config.WELCOME_USER)
            user_input = input(Config.USER_PROMPTS)
            while user_input != 'q':
                match user_input:
                    case '1':
                        menu_function.user_view_input(user_id)
                    case '2':
                        username = input(Config.ENTER_USERNAME)
                        website = input(Config.ENTER_WEBSITE)
                        email = input(Config.ENTER_EMAIL)
                        password = input(Config.PASSWORD)
                        user_controller.add_data(user_id, username, website, email, password)
                    case '3':
                        website = input(Config.ENTER_WEBSITE)
                        email = input(Config.ENTER_EMAIL)
                        user_controller.delete_data(user_id, website, email)
                    case _:
                        print(Config.INVALID_PROMPT)    

                user_input = input(Config.USER_PROMPTS)

if __name__ == "__main__":
    Config.load()
    Config.load_print_statement()
    Config.load_queries()
    user_controller.create_user_table()
    user_controller.create_credentials_table()
    menu()
