# Python library packages
from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, BooleanField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
import re  # regular expressions library

# Application level packages/modules
from users.models import Users



class BaseUserForm(FlaskForm):
	first_name = StringField('First Name', [
		validators.DataRequired(),
		validators.Length(max=50)
		])
	last_name = StringField('Last Name', [
		validators.DataRequired(),
		validators.Length(max=50)
		])
	username = StringField('Username', [
		validators.DataRequired(),
		validators.Length(min=2, max=20)
		])
	email = EmailField('Email address', [
		validators.DataRequired(),
		validators.Length(max=40)
		])
	bio = StringField('Bio',
		widget=TextArea(),
		validators=[validators.Length(max=160)]
		)
	
class RegisterForm(BaseUserForm):
	password = PasswordField('New Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords must match'),
		validators.Length(min=8, max=60)
		])
	confirm = PasswordField('Repeat Password')
	
	def validate_username(form, field):
		if Users.query.filter_by(username=field.data).first():
			raise ValidationError("Username is already in use. Please choose a different one.")
		if not re.match("^[a-zA-Z0-9_-]{2,20}$", field.data):
			raise ValidationError("Username must consist of only alphabets, numbers, \"_\" or \"-\". ")
			
	def validate_email(form, field):
		if Users.query.filter_by(email=field.data).first():
			raise ValidationError("Email is already in use. Please choose a different one.") 

class LoginForm(FlaskForm):
	username = StringField('Username', [
		validators.DataRequired(),
		validators.Length(min=2, max=20)
		])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.Length(min=8, max=60)
		])
	remember = BooleanField('Remember Me')
	
class EditForm(BaseUserForm):
	pass
