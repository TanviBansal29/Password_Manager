# from app import FastAPI
from fastapi import FastAPI
from controllers.user_controller import create_credentials_table, create_user_table
from resources.auth import router as AuthRouter
from resources.admin import router as AdminRouter
from resources.user import router as UserRouter

create_user_table()
create_credentials_table()
# def create_app():
app = FastAPI()
app.include_router(AdminRouter, prefix='/v1')
app.include_router(AuthRouter, prefix='/v1')
app.include_router(UserRouter, prefix='/v1')

#     return app

# create_app()