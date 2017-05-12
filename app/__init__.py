from flask import Flask, render_template, redirect, url_for, request,\
	flash, session

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['SECRET_KEY'] = 'you will never guess'
app.config.from_object('config')
app.config['SESSION_PROTECTION'] = 'strong'
db = SQLAlchemy(app)
mail = Mail(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app) 

from app import views, models
