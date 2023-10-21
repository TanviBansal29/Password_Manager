from controllers import user_controller
from controllers import admin_controller

USER_PROMPTS = '''
Enter -
    1 - View data
    2 - Add new data
    3 - Delete your data 
    
    Press q to quit

Enter your choice: '''

USER_VIEW_PROMPTS = '''
Enter -
    1 - View all data
    2 - View data by website
    3 - View data by email
    
    Press q to quit

Enter your choice: '''

ADMIN_PROMPTS = '''
Enter -
    1 - View data
    2 - Create new user
    3 - Delete user data 
    
    Press q to quit

Enter your choice: '''

ADMIN_VIEW_PROMPTS = '''
Enter -
    1 - View data by user
    2 - View data by website
    
    Press q to quit

Enter your choice: '''

ADMIN_DELETE_PROMPTS = '''
Enter -
    1 - Delete user data
    2 - Delete data by website
    
    Press q to quit

Enter your choice: '''

credentials = [
    {
        'username' : 'Michael',
        'password': '123456',
        'role' : 'admin'
    },
    {
        'username' : 'David',
        'password': 'qwerty',
        'role' : 'user'
    },
    {
        'username' : 'John',
        'password': 'asdfg',
        'role' : 'user'
    }
]

isLoggedIn = False
role = 'user'

def menu():
    print("Welcome to Password Manager!\nPlease enter your credentials...\n")
    username = input("username: ")

    for cred in credentials:
        if cred['username'] == username:
            password = input("password: ")
            if cred['password'] == password:
                print("Logged in successfully.")
                isLoggedIn = True
                role = cred['role']
                break
    else:
        print("Invalid credentials!")

    if isLoggedIn:
        # your logic
        if role == 'admin':
            # admin logic
            admin_input=input(ADMIN_PROMPTS)
            while admin_input != 'q' :
                match admin_input:
                    case '1':
                        admin_view_input = input(ADMIN_VIEW_PROMPTS)
                        while admin_view_input != 'q':
                            match admin_view_input :
                                case '1':
                                    admin_controller.view_data_by_user()
                                case '2':
                                    admin_controller.view_user_data_by_website()
                    case '2':
                        admin_controller.create_user()
                    case '3':
                        admin_delete_input = input(ADMIN_DELETE_PROMPTS) 
                        while admin_delete_input != 'q':
                            match admin_delete_input :
                                case '1':
                                    admin_controller.delete_user()
                                case '2':
                                    admin_controller.delete_website_data()
    
        else:
            # user logic
            user_input = input(USER_PROMPTS)
            while user_input != 'q':
                match user_input:
                    case '1':
                        user_view_input = input(USER_VIEW_PROMPTS)
                        while user_view_input != 'q':
                            match user_view_input:
                                case '1':
                                    user_controller.view_all_data()
                                case '2':
                                    user_controller.view_data_by_website()
                                case '3':
                                    user_controller.view_data_by_email()
                                case _:
                                    print("Invalid input. Please try again...")
                    case '2':
                        user_controller.add_data()
                    case '3':
                        user_controller.delete_data()


if __name__ == "__main__":
    menu()