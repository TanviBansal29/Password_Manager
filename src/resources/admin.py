from flask_smorest import Blueprint, abort
from controllers import admin_controller

blp = Blueprint("admin", __name__)


@blp.route("/users")
def view_all_user_data():
    data = admin_controller.view_all_user_data()
    if not data:
        abort(404, message = "No data found for users.")
    print(data)
    return data


@blp.route("/users/<int:user_id>")
def view_data_by_user(user_id):
    # user_id = int(user_id)
    data = admin_controller.view_data_by_user(user_id)
    if not data:
        abort(404, message = f"No data found for user_id = {user_id}.")

    return data

@blp.route("/users/<string:website>")
def view_user_data_by_website(website):
    data = admin_controller.view_user_data_by_website(website)
    if not data:
        abort(404, message = f"No data found for {website}.")
    return data 


    


