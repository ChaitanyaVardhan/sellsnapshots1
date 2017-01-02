from flask import Flask, render_template, redirect, url_for, request,\
	flash, session

from app import app, db

from .models import User

from .emails import send_email


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/photos')
def photos():
	return render_template('photos.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')

	first_name = request.form['firstName']
	last_name = request.form['lastName']
	city = request.form['city']
	country = request.form['country']
	email = request.form['email']
	user = User.query.filter_by(email=email).first()
	if user is None:
		user = User(firstname = first_name, lastname = last_name, city = city, country = country, email = email)
		db.session.add(user)
		db.session.commit()
		send_email(user.email, 'Thank You', 'thank', user)
		flash('Thank you %s %s for your interest in sellsnapshots. Your information has been registered with us'\
		 % ((user.firstname), (user.lastname)))
	else:
		flash('Thank you %s %s for your interest in sellsnapshots. Your information has already been registered with us'\
		 % ((user.firstname), (user.lastname)))
	return render_template('register.html')


@app.route('/header')
def header():
	return render_template('header.html')


@app.route('/footer')
def footer():
	return render_template('footer.html')


@app.route('/menu')
def menu():
	return render_template('menu.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')
