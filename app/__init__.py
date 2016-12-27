from flask import Flask, render_template, redirect, url_for, request,\
	flash, session


app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['SECRET_KEY'] = 'you will never guess'

from app import views




