from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

# configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../feedback.db'
db = SQLAlchemy(app)

app.config.from_object(__name__)
