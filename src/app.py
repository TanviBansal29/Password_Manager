from fastapi import FastAPI
from routes.auth import router as AuthRouter
from routes.admin import router as AdminRouter
from routes.user import router as UserRouter

# create_user_table()
# create_credentials_table()
app = FastAPI(title = "Password Manager")

@app.get("/healthy")
def health_check():
    return {"status":"Healthy"}

app.include_router(AdminRouter, prefix='/v1')
app.include_router(AuthRouter, prefix='/v1')
app.include_router(UserRouter, prefix='/v1')
