from controllers import user_controller
from controllers import admin_controller
from utils.menu import menu_function

USER_PROMPTS = '''
Enter -
    1 - View data
    2 - Add new data
    3 - Delete your data 
    
    Press q to quit

Enter your choice: '''

ADMIN_PROMPTS = '''
Enter -
    1 - View data
    2 - Create new user
    3 - Delete user data 
    
    Press q to quit

Enter your choice: '''

user_controller.create_user_table()
user_controller.create_credentials_table()

def menu():
    print("Welcome to Password Manager!\nPlease enter your credentials...\n")
    while True:
        username = input("Enter your username:- ")
        password = input("Enter your password:- ")
        role = menu_function.fetch_user(username,password)
        if role != None:
            break
    if role[4] == 'admin':
        # admin logic
        print("WELCOME ADMIN!")
        admin_input = input(ADMIN_PROMPTS)
        while admin_input != 'q' :
            match admin_input:
                case '1':
                    menu_function.admin_view_input()
                case '2':
                    while True:
                        username = input("Set username:- ")
                        if menu_function.fetch_username(username):
                            print("Username already exists! Please try new username...")
                        else:
                            break    
                    password = input("Set password:- ")

                    admin_controller.create_user(username, password)
                case '3':
                    menu_function.admin_delete_input()
                case _:
                    print("Invalid input. Please try again...")      

            admin_input = input(ADMIN_PROMPTS)
    else:
        # user logic
        is_default = role[3]
        user_id = role[0]
        if is_default == 0:
            print("PLEASE UPDATE YOUR PASSWORD!")
            new_password = input("Enter new password:- ")
            menu_function.update_password(user_id, new_password)
    
        else:    
            print("WELCOME USER!")
            user_input = input(USER_PROMPTS)
            while user_input != 'q':
                match user_input:
                    case '1':
                        menu_function.user_view_input(user_id)
                    case '2':
                        username = input("Enter your username: ")
                        website = input("Enter website name: ")
                        email = input("Enter email: ")
                        password = input("Enter password: ")
                        user_controller.add_data(user_id, username, website, email, password)
                    case '3':
                        website = input("Enter website name: ")
                        email = input("Enter email: ")
                        user_controller.delete_data(user_id, website, email)
                    case _:
                        print("Invalid input. Please try again...")    

                user_input = input(USER_PROMPTS)

if __name__ == "__main__":
    menu()
