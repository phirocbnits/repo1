from flask1 import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    email_id = db.Column(db.String(length=50), nullable=False, unique=True)
    passwd = db.Column(db.String(length=106), nullable=False)
    def __init__(self,name,email_id,passwd):
        self.name=name
        self.email_id=email_id
        self.passwd=passwd
def __repr__(self):
        return f'User{self.name}'

class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)