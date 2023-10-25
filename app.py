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

credentials = [
    {
        'user_id' : 'Michael',
        'password': '123456',
        'role' : 'admin'
    },
    {
        'user_id' : 'David',
        'password': 'qwerty',
        'role' : 'user'
    },
    {
        'user_id' : 'John',
        'password': 'asdfg',
        'role' : 'user'
    }
]

user_controller.create_user_table()

isLoggedIn = False
role = 'user'

def menu():
    print("Welcome to Password Manager!\nPlease enter your credentials...\n")
    user_id = input("user_id: ")

    for cred in credentials:
        if cred['user_id'] == user_id:
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
            print("WELCOME ADMIN!")
            admin_input = input(ADMIN_PROMPTS)
            while admin_input != 'q' :
                match admin_input:
                    case '1':
                        menu_function.admin_view_input()
                    case '2':
                        admin_controller.create_user()
                    case '3':
                        menu_function.admin_delete_input()
                    case _:
                        print("Invalid input. Please try again...")      

                admin_input = input(ADMIN_PROMPTS)
        else:
            # user logic
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
                        user_controller.delete_data()
                    case _:
                        print("Invalid input. Please try again...")    

                user_input = input(USER_PROMPTS)

if __name__ == "__main__":
    menu()
