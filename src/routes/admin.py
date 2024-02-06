from fastapi import APIRouter
from controllers.admin_controller import AdminController
from schemas.schemas import UserSchema
from starlette import status

router = APIRouter(tags=["Admin"])


@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(register_data: UserSchema):
    """Create a new user"""

    admin_obj = AdminController()
    return admin_obj.register(register_data)


@router.get("/users", status_code=status.HTTP_200_OK)
def view_all_user_data():
    """View all user data"""
    admin_obj = AdminController()
    return admin_obj.view_all_user_data()


@router.get("/users/user_id/{user_id}", status_code=status.HTTP_200_OK)
# # @access_control("admin")
def view_data_by_user(user_id: str):
    """View user data by user_id"""
    admin_obj = AdminController()
    return admin_obj.view_data_by_user(user_id)


@router.get("/users/website/{website}", status_code=status.HTTP_200_OK)
# # @access_control("admin")
def view_user_data_by_website(website: str):
    """View users data by website"""
    admin_obj = AdminController()
    return admin_obj.view_user_data_by_website(website)


@router.delete("/users/{user_id}")
# # @access_control("admin")
def delete_user(user_id: str):
    """Delete a user"""

    admin_obj = AdminController()
    return admin_obj.delete_user_data(user_id)


# @router.delete("/website/{website}")
# # # @jwt_required()
# # # @access_control("admin")
# def delete_website_data(website : str):
#     '''Delete data by website'''
#     admin_obj =
# #     admin_controller.delete_website_data(website)
# #     return {'message': 'Users deleted'}
