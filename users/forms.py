# Python library packages
from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError

# Application level packages/modules
from users.models import Users



class RegisterForm(Form):
	first_name = StringField('First Name', [
		validators.Required(),
		validators.Length(max=50)
		])
	last_name = StringField('Last Name', [
		validators.Required(),
		validators.Length(max=50)
		])
	username = StringField('Username', [
		validators.Required(),
		validators.Length(min=2, max=20)
		])
	email = EmailField('Email address', [
		validators.Required(),
		validators.Length(max=40)
		])
	password = PasswordField('New Password', [
		validators.Required(),
		validators.EqualTo('confirm', message='Passwords must match'),
		validators.Length(min=8, max=60)
		])
	confirm = PasswordField('Repeat Password')
	
	def validate_username(form, field):
		if Users.query.filter_by(username=field.data).first():
			raise ValidationError("Username is already in use. Please choose a different one.")
			
	def validate_email(form, field):
		if Users.query.filter_by(email=field.data).first():
			raise ValidationError("Email is already in use. Please choose a different one.") 

