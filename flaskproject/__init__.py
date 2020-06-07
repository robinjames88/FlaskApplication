import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# create loginmanage object
login_manager = LoginManager()


# create application
app = Flask(__name__)

#configuration
app.config['SECRET_KEY'] = 'mypassword'

basedir = os.path.abspath(os.path.dirname(__file__))

# configuration sqlalchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Create Database for application

db = SQLAlchemy(app)

Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'