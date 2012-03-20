from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.login import LoginManager

# configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../feedback.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.setup_app(app)

app.config.from_object(__name__)
