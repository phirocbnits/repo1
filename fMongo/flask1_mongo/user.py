from flask1_mongo import db
import datetime

class User(db.Document):
   # id = db.IntField(primary_key=True, autoincrement=True)#, primary_key=True)
    name = db.StringField(required=True)
    email_id = db.StringField(required=True, unique=True)
    passwd = db.StringField(required=True)
    """def __init__(self,name,email_id,passwd):
        self.name=name
        self.email_id=email_id
        self.passwd=passwd
def __repr__(self):
        return f'User{self.name}'"""

class BlacklistToken(db.Document):
    """
    Blacklisted Token list for storing JWT tokens
    """
    token = db.StringField(unique=True, required=True)
    blacklisted_on = db.DateTimeField(default=datetime.datetime.utcnow, required=True)

class CurrentToken(db.Document):
    """
    Active Token list for storing JWT tokens
    """
    token = db.StringField(unique=True, required=True)
    created_on = db.DateTimeField(default=datetime.datetime.utcnow, required=True)
