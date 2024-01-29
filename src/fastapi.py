from fastapi import FastAPI
from src.resources.auth import router as AuthRouter
from src.resources.admin import router as AdminRouter
from src.resources.user import router as UserRouter

def create_app():
    app = FastAPI()
    app.include_router(AdminRouter, prefix='/v1')
    app.include_router(AuthRouter, prefix='/v1')
    app.include_router(UserRouter, prefix='/v1')

    return app
