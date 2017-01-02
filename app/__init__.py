from flask import Flask, render_template, redirect, url_for, request,\
	flash, session

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['SECRET_KEY'] = 'you will never guess'
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)

from app import views, models
