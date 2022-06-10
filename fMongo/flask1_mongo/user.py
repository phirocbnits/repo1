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
    Token Document for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.IntField(primary_key=True, autoincrement=True)
    token = db.StringField(unique=True, required=True)
    blacklisted_on = db.DateTimeField(default=datetime.datetime.utcnow, required=True)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)