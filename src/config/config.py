import yaml

class Config:
    USER_VIEW_PROMPTS = None
    ADMIN_VIEW_PROMPTS = None
    ADMIN_DELETE_PROMPTS = None
    USER_PROMPTS = None
    ADMIN_PROMPTS = None
    DATABASE_NAME = None
    WELCOME_MESSAGE = None
    ENTER_USERNAME = None
    ENTER_PASSWORD = None
    WELCOME_ADMIN =None
    SET_USERNAME =None
    USERNAME_ERROR = None
    SET_PASSWORD = None
    INVALID_PROMPT = None
    UPDATE_PASSWORD = None
    NEW_PASSWORD = None
    WELCOME_USER = None
    ENTER_WEBSITE = None
    ENTER_EMAIL = None
    PASSWORD = None
    INVALID_LOGIN = None
    ENTER_USERID = None
    NO_DATA = None
    QUERY_TO_VIEW_ALL_DATA = None
        

    @classmethod
    def load(cls):
        with open('config\\config.yml','r') as f:
            data = yaml.safe_load(f)
            cls.USER_VIEW_PROMPTS = data['USER_VIEW_PROMPTS']
            cls.ADMIN_VIEW_PROMPTS = data['ADMIN_VIEW_PROMPTS']
            cls.ADMIN_DELETE_PROMPTS = data['ADMIN_DELETE_PROMPTS']
            cls.USER_PROMPTS = data['USER_PROMPTS']
            cls.ADMIN_PROMPTS = data['ADMIN_PROMPTS']
            cls.DATABASE_NAME = data['DATABASE_NAME']

    @classmethod
    def load_print_statement(cls):
        with open('config\\print_statements.yml','r') as f:
            data = yaml.safe_load(f)
            cls.WELCOME_MESSAGE = data['WELCOME_MESSAGE']
            cls.ENTER_USERNAME = data['ENTER_USERNAME'] 
            cls.ENTER_PASSWORD = data['ENTER_PASSWORD'] 
            cls.WELCOME_ADMIN = data['WELCOME_ADMIN'] 
            cls.SET_USERNAME = data['SET_USERNAME'] 
            cls.USERNAME_ERROR = data['USERNAME_ERROR'] 
            cls.INVALID_PROMPT = data['INVALID_PROMPT'] 
            cls.UPDATE_PASSWORD = data['UPDATE_PASSWORD']
            cls.NEW_PASSWORD = data['NEW_PASSWORD']
            cls.WELCOME_USER = data['WELCOME_USER']
            cls.ENTER_WEBSITE = data['ENTER_WEBSITE'] 
            cls.ENTER_EMAIL = data['ENTER_EMAIL'] 
            cls.PASSWORD = data['PASSWORD'] 
            cls.INVALID_LOGIN = data['INVALID_LOGIN'] 
            cls.ENTER_USERID = data['ENTER_USERID']
            cls.NO_DATA = data['NO_DATA']
            cls.SET_PASSWORD = data['SET_PASSWORD']

    @classmethod
    def load_queries(cls):
        with open('config\\queries.yml','r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_TO_CREATE_USERS_TABLE = data['QUERY_TO_CREATE_USERS_TABLE']
            cls.QUERY_TO_CREATE_CREDENTIALS_TABLE = data['QUERY_TO_CREATE_CREDENTIALS_TABLE']
            cls.QUERY_TO_VIEW_ALL_USER_DATA = data['QUERY_TO_VIEW_ALL_USER_DATA']
            cls.QUERY_TO_VIEW_DATA_BY_USER = data['QUERY_TO_VIEW_DATA_BY_USER']
            cls.QUERY_TO_VIEW_USER_DATA_BY_WEBSITE = data['QUERY_TO_VIEW_USER_DATA_BY_WEBSITE']
            cls.QUERY_TO_CREATE_USER= data['QUERY_TO_CREATE_USER']
            cls.QUERY_TO_DELETE_USER = data['QUERY_TO_DELETE_USER']
            cls.QUERY_TO_ENALE_FOREIGN_KEY = data['QUERY_TO_ENALE_FOREIGN_KEY']
            cls.QUERY_TO_ADD_DATA = data['QUERY_TO_ADD_DATA']
            cls.QUERY_TO_VIEW_ALL_DATA = data['QUERY_TO_VIEW_ALL_DATA']
            cls.QUERY_TO_VIEW_DATA_BY_WEBSITE = data['QUERY_TO_VIEW_DATA_BY_WEBSITE']
            cls.QUERY_TO_DATA_BY_EMAIL = data['QUERY_TO_DATA_BY_EMAIL']
            cls.QUERY_TO_DELETE_DATA = data['QUERY_TO_DELETE_DATA']
            cls.QUERY_TO_VERIFY_LOGIN = data['QUERY_TO_VERIFY_LOGIN']
            cls.QUERY_TO_UPDATE_DEFAULT_PASSWORD = data['QUERY_TO_UPDATE_DEFAULT_PASSWORD']
            cls.QUERY_TO_CHECK_USERNAME = data['QUERY_TO_CHECK_USERNAME']
            cls.QUERY_TO_DELETE_WEBSITE_DATA = data['QUERY_TO_DELETE_WEBSITE_DATA']


Config.load_print_statement()
Config.load_queries()
Config.load()