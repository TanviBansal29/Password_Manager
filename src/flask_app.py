from flask import Flask
from resources.admin import blp as AdminBlp
from resources.auth import blp as LoginBlp
from flask_smorest import Api
from config.config import Config
from controllers import user_controller
from flask_jwt_extended import JWTManager

app =  Flask(__name__)  #creating flask app

app.config["PROPAGATE_EXCEPTIONS"] = True 
app.config["API_TITLE"] = "Password Manager"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app) #connecting flask smorest to flask app

app.config["JWT_SECRET_KEY"] = "DEMO_JWT_SECRET_KEY"
jwt = JWTManager(app)

api.register_blueprint(AdminBlp) #Adminblp gets connected to Flask app
api.register_blueprint(LoginBlp)


if __name__ == "__main__":
    Config.load()
    Config.load_print_statement()
    Config.load_queries()
    user_controller.create_user_table()
    user_controller.create_credentials_table()
    app.run(debug = True)
