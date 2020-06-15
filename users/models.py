from application import db
from datetime import datetime


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True)
	password = db.Column(db.String()) 
	email = db.Column(db.String(35), unique=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	created = db.Column(db.DateTime, default=datetime.utcnow)
	bio = db.Column(db.String(60)) 
	
	def __init__(self, username, password, email, first_name, last_name, bio, created=None):
		self.username = username
		self.password = password
		self.email = email
		self.first_name = first_name
		self.last_name = last_name
		if self.created is None:
			self.created = datetime.utcnow()
		else:
			self.created = self.created
		self.bio = bio
		
	def __repr__(self):
		return '<Users {}>'.format(self.username)
		
		
