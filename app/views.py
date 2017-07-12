from flask import Flask, render_template, redirect, url_for, request,\
	flash, session

from flask_login import login_user, logout_user, login_required, current_user

from app import app, db

from .models import User

from .emails import send_email

from .forms import ChangePasswordForm, PasswordResetRequestForm, PasswordResetForm, ChangeEmailForm

from oauth import OAuthSignIn

from mlab import read_from_mlab

import json

CACHE = {}

@app.before_request
def before_request():
	if current_user.is_authenticated \
			and not current_user.confirmed \
			and request.endpoint != 'unconfirmed' \
			and request.endpoint !=  'logout' \
			and request.endpoint !=  'resend_confirmation' \
			and request.endpoint != 'confirm' \
			and request.endpoint != 'static':
		return redirect(url_for('unconfirmed'))

@app.route('/auth/unconfirmed')
def unconfirmed():
	if current_user.is_anonymous or current_user.confirmed:
		return redirect(url_for('index'))
	return render_template('unconfirmed.html')
	
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
	password = request.form['password']
	user = User.query.filter_by(email=email).first()
	if user is None:
		user = User(firstname = first_name, lastname = last_name, city = city, country = country, email = email\
			,password=password)
		db.session.add(user)
		db.session.commit()
		token = user.generate_confirmation_token()
		send_email(user.email, 'Confirm Your Account', 'confirm', user=user, token=token)
		flash('Thank you %s %s for your interest in sellsnapshots. A confirmation email has been sent to your\
		  email address' % ((user.firstname), (user.lastname)))
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

@app.route('/buy/<photo_id>')
def buy(photo_id):
	s3Path = 'https://s3.ap-south-1.amazonaws.com/sellsnapshots/preview/'
	path = s3Path + photo_id + '.jpg'
	return render_template('image.html', path=path)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html', next=request.args.get('next'))
	email = request.form['email']
	password = request.form['password']
	user = User.query.filter_by(email=email).first()
	next = request.form['next']
	if user is not None and user.verify_password(password):
		login_user(user)
		if next:
			return redirect(next)
		else:
			return redirect(url_for('user'))
	flash('Invalid username or password')
	return render_template('login.html',next=next)

@app.route('/auth/confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('user'))
	if current_user.confirm(token):
		flash('You have confirmed your account. Thanks!')
	else:
		flash('The confirmation link is invalid or has expired')
	return redirect(url_for('user'))

@app.route('/auth/confirm')
@login_required
def resend_confirmation():
	token = current_user.generate_confirmation_token()
	send_email(current_user.email, 'Confirm Your Account', 'confirm', user=current_user, token=token)
	flash('A new confirmation email has been sent to your registered email address.')
	return redirect(url_for('index'))

@app.route('/auth/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash('Your password has been updated.')
            return redirect(url_for('user'))
        else:
            flash('Invalid password.')
    return render_template("change_password.html", form=form)

@app.route('/auth/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            send_email(user.email, 'Reset Your Password',
                       'reset_password_email',
                       user=user, token=token,
                       next=request.args.get('next'))
        flash('An email with instructions to reset your password has been '
              'sent to you.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/auth/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            return redirect(url_for('index'))
        if user.reset_password(token, form.password.data):
            flash('Your password has been updated.')
            return redirect(url_for('login'))
        else:
            return redirect(url_for('index'))
    return render_template('reset_password.html', form=form)

@app.route('/auth/change-email', methods=['GET', 'POST'])
@login_required
def change_email_request():
	form = ChangeEmailForm()
	if form.validate_on_submit():
		if current_user.verify_password(form.password.data):
			new_email = form.email.data
			token = current_user.generate_email_change_token(new_email)
			send_email(new_email, 'Confirm your email address',
						'change_email_email',
						user=current_user, token=token)
			flash('An email with instructions to confirm your new email '
					'address has been sent to you.')
			return redirect(url_for('index'))
		else:
			flash('Invalid email or password.')
	return render_template("change_email.html", form=form)

@app.route('/auth/change-email/<token>')
@login_required
def change_email(token):
	if current_user.change_email(token):
		flash('Your email address has been updated.')
	else:
		flash('Invalid request.')
	return redirect(url_for('index'))

@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, social_name=username, email=email, confirmed=True)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))

@app.route('/user')
@login_required
def user():
	return render_template('user.html')

@app.route('/secret')
@login_required
def secret():
	return ("Stupid asshole %s" % current_user.email)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/api/v1/photos')
def api_v1_photos():
    key = 'FRONT'
    if key in CACHE:
        images = CACHE[key]
    else:
        images, status_code = read_from_mlab()
        CACHE[key] = images

    return json.dumps(images)
