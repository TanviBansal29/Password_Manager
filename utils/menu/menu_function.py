from controllers import admin_controller, user_controller

# config, json, yaml

USER_VIEW_PROMPTS = '''
Enter -
    1 - View all data
    2 - View data by website
    3 - View data by email
    
    Press q to quit

Enter your choice: '''

ADMIN_VIEW_PROMPTS = '''
Enter -
    1 - View all user data
    2 - View data by user
    3 - View data by website
    
    Press q to quit

Enter your choice: '''

ADMIN_DELETE_PROMPTS = '''
Enter -
    1 - Delete user data
    2 - Delete data by website
    
    Press q to quit

Enter your choice: '''

def admin_view_input():
    admin_view_input = input(ADMIN_VIEW_PROMPTS)

    while admin_view_input != 'q':
        match admin_view_input :
            case '1':
                data = admin_controller.view_all_user_data()
                print(data)
            case '2':
                user_id = input("Enter user_id: ")
                data = admin_controller.view_data_by_user(user_id)
                print(data)
            case '3':
                website = input("Enter website name: ")
                data = admin_controller.view_user_data_by_website(website)
                print(data)
            case _:
                print("Invalid input. Please try again...")

        admin_view_input = input(ADMIN_VIEW_PROMPTS)        


def admin_delete_input():
    admin_delete_input = input(ADMIN_DELETE_PROMPTS) 

    while admin_delete_input != 'q':
        match admin_delete_input :
            case '1':
                admin_controller.delete_user()
            case '2':
                admin_controller.delete_website_data()
            case _:
                print("Invalid input. Please try again...")

        admin_delete_input = input(ADMIN_DELETE_PROMPTS)


def user_view_input(user_id):
    user_view_input = input(USER_VIEW_PROMPTS)

    while user_view_input != 'q':
        match user_view_input:
            case '1':
                data = user_controller.view_all_data(user_id)
                print(data)
            case '2':
                website = input("Enter website name: ")
                data = user_controller.view_data_by_website(user_id, website)
                print(data)
            case '3':
                email = input("Enter email: ")
                data = user_controller.view_data_by_email(user_id, email)
                print(data)
            case _:
                print("Invalid input. Please try again...")

        user_view_input = input(USER_VIEW_PROMPTS)        