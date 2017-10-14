from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import Required, EqualTo, Email, Length
from wtforms import ValidationError
from .models import User

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[Required()])
    password = PasswordField('New password', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[Required()])
    submit = SubmitField('Update Password')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('New Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')

class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[Required(), Length(1, 64),
                        Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

class EditProdAndLocForm(FlaskForm):

    product_name1 = StringField('Product Name', validators=[Length(0,64)])
    price1 = StringField('Price', validators=[Length(0,10)])
    product_name2 = StringField('Product Name', validators=[Length(0,64)])
    price2 = StringField('Price', validators=[Length(0,10)])
    product_name3 = StringField('Product Name', validators=[Length(0,64)])
    price3 = StringField('Price', validators=[Length(0,10)])
    product_name4 = StringField('Product Name', validators=[Length(0,64)])
    price4 = StringField('Price', validators=[Length(0,10)])
    product_name5 = StringField('Product Name', validators=[Length(0,64)])
    price5 = StringField('Price', validators=[Length(0,10)])
    location = StringField('Location', validators=[Length(0,10)])
    submit = SubmitField('Update')


