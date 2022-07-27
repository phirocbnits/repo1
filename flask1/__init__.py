from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://{}:{}@{}:{}/{}'.format(environ.get('USER_NAME'),environ.get('MYSQL_ROOT_PASSWORD'),environ.get('HOST'),,environ.get('PORT')environ.get('DB'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY'] = '9b3eeae24ff5b6a5ca11c479'
db = SQLAlchemy(app)

from flask1 import routes
