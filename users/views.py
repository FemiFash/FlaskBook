from flask import Blueprint, render_template, redirect, url_for, flash, request, session, abort
from werkzeug.security import generate_password_hash, check_password_hash

from application import db
from users.models import Users
from users.forms import RegisterForm, LoginForm, EditForm

user_app = Blueprint('user_app', __name__)   # Anything named *_app is a Blueprint app

@user_app.route('/')
@user_app.route('/index/')
def index():
	form = LoginForm()
	return render_template('users/login.html',form=form)

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
					return redirect(url_for('user_app.login'))
			else:
				user = None
		if not user:
			error = 'Login was Unsuccessful. Incorect username and/or password'	
	return render_template('users/login.html', form=form, error=error )

@user_app.route('/logout', methods=('GET', 'POST'))
def logout():
	session.pop('username')
	return redirect(url_for('user_app.login'))

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

@user_app.route('/<username>', methods=('GET', 'POST'))
def profile(username):
	edit_profile = False
	user = Users.query.filter_by(username=username).first()
	if session.get('username') and user.username == session.get('username'):
		edit_profile = True
	if user:
		return render_template('users/profile.html', user=user, edit_profile=edit_profile)
	else:
		abort(404)
	
@user_app.route('/edit', methods=('GET', 'POST'))
def edit():
	error = None
	message = None
	user = Users.query.filter_by(username=session.get('username')).first()
	if user:
		form = EditForm(obj=user) # prepopulates form with values in user
		if form.validate_on_submit():
			if user.username != form.username.data: # user is changing their username
				if Users.query.filter_by(username=form.username.data).first():
					error = "\"" + form.username.data + "\" is already in use"
				else:
					session['username'] = form.username.data
			if user.email != form.email.data.lower(): # user is changing their email
				if Users.query.filter_by(email=form.email.data.lower()).first():
					error = "\"" + form.email.data + "\" is already in use"
				else:
					form.email.data = form.email.data.lower()
			if not error:
				form.populate_obj(user)
				db.session.add(user)
				db.session.commit()
				message = "Your profile has been successfully updated"
		return render_template("users/edit.html", form=form, error=error, message=message )
	else:
		abort(404)	
					
				
		
	
