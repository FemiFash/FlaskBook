from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash

from application import db
from users.models import Users
from users.forms import RegisterForm, LoginForm

user_app = Blueprint('user_app', __name__)   # Anything named *_app is a Blueprint app

@user_app.route('/')
@user_app.route('/index/')
def index():
	return "Index Page"

@user_app.route('/login', methods=('GET', 'POST'))
def login():
	form = LoginForm()
	error = None
	
	if request.method == 'GET' and request.args.get('next'): #Code to help send user back to the page on application...
		session['next'] = request.args.get('next')           #..after user successfully logs in. URL saved in next
	
	if form.validate_on_submit():
		user = Users.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password,form.password.data):
				session['username'] = form.username.data
				if 'next' in session:
					next = session.get('next')
					session.pop('next')	
					return redirect(next)
				else:
					return 'User logged in'
			else:
				user = None
		if not user:
			error = 'Login was Unsuccessful. Incorect username and/or password'	
	return render_template('users/login.html', form=form, error=error )

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
