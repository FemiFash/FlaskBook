import os

SECRET_KEY = 'change_this_so_that_it_is_set_from_the_random_secret_key_generator'
DEBUG = True # remember to change to false when uploading

DB_USERNAME = 'postgres'
DB_PASSWORD = '10Blessed1'
DB_HOST = 'localhost:5432'
BLOG_DATABASE_NAME = 'flaskbook'
DB_URI = "postgresql://{}:{}@{}/{}".format(DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

UPLOADED_IMAGES_DEST = os.path.dirname(os.path.abspath(__file__)) + "\static\images"
UPLOADED_IMAGES_URL = '\static\images\\'

"""
Above 2 settings may be ....
UPLOADED_IMAGES_DEST = os.path.dirname(os.path.abspath(__file__)) + "/static/images"
UPLOADED_IMAGES_URL = '/static/images'
.....for a ubuntu/linux server
"""
