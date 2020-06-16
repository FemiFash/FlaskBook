from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from application import db
from users.models import Users
from users.forms import RegisterForm

user_app = Blueprint('user_app', __name__)   # Anything named *_app is a Blueprint app

@user_app.route('/')
@user_app.route('/index/')
def index():
	return "Index Page"

@user_app.route('/login')
def login():
	return "User login"

@user_app.route('/register', methods=('GET', 'POST'))
def register():
	form = RegisterForm()
	
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=10) 
		user = Users(
			username = form.username.data,
			password = hashed_password,
			email = form.email.data,
			first_name = form.first_name.data,
			last_name = form.last_name.data,
			)
		db.session.add(user)
		db.session.flush() 
		if user.id:
			db.session.commit()
		else:
			db.session.rollback()
			error = 'Error creating user'
			return render_template('users/register.html',form=form)
		return "User Registered"
	return render_template('users/register.html',form=form)
